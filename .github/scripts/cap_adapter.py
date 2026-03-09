#!/usr/bin/env python3
"""
cap_adapter.py

Minimal, human-readable adapter to map repository front-matter variants into
the canonical CAP/CRP provenance schema.

Features:
- stdin support (use '-' as the path)
- tolerant front-matter parsing (BOM/leading whitespace; newline-bounded '---' fences)
- author normalization (string, dict, or list -> list of objects with type)
- optional pruning of empty fields (--prune-empty)
- ISO-8601 guard: if date present but not ISO, set provenance.generated_at to a safe UTC fallback
- generator prompts redacted by default; include with --include-prompts
- unknown fields preserved under 'extensions'
"""

import argparse
import os
import sys
import yaml
import re
from datetime import datetime, timezone
from typing import Any, Dict, Tuple, Optional

# ---------------------------
# Canonical keys we want to produce
# ---------------------------
CANONICAL_TEMPLATE = {
    "title": None,
    "authors": None,
    "date": None,
    "cap": {
        "cap_record_id": None,
        "cap_schema_version": None
    },
    "provenance": {
        "provenance_id": None,
        "commit_sha": None,
        "blob_sha": None,
        "file_path": None,
        "generated_by": None,
        "inputs": None,
        "parent_provenance": None,
        "generated_at": None,
        "confidence": None,
    },
    "semantic": {
        "summary": None,
        "frame": None,
        "delta": None,
        "affected_nodes": None,
    },
    "attestation": None,
    "extensions": {}
}

# ---------------------------
# Alias mapping: alternate names -> canonical path (dot-separated)
# ---------------------------
ALIASES = {
    "cap_id": "cap.cap_record_id",
    "cap_record": "cap.cap_record_id",
    "commit": "provenance.commit_sha",
    "sha": "provenance.commit_sha",
    "blob": "provenance.blob_sha",
    "path": "provenance.file_path",
    "file": "provenance.file_path",
    "generated": "provenance.generated_by",
    "generator": "provenance.generated_by",
    "generator_name": "provenance.generated_by.name",
    "generated_at": "provenance.generated_at",
    "created_at": "date",
    "summary": "semantic.summary",
    "semantic_summary": "semantic.summary",
    "frame": "semantic.frame",
    "delta": "semantic.delta",
    "author": "authors",
    "creators": "authors",
    "attested_by": "attestation",
    "prov_id": "provenance.provenance_id",
    "provenance_id": "provenance.provenance_id",
    "confidence_score": "provenance.confidence",
    "generator_prompt": "provenance.generated_by.prompt"
}

# ---------------------------
# Utilities
# ---------------------------
def deep_set(d: Dict[str, Any], path: str, value: Any):
    keys = path.split(".")
    cur = d
    for k in keys[:-1]:
        if k not in cur or not isinstance(cur[k], dict):
            cur[k] = {}
        cur = cur[k]
    cur[keys[-1]] = value

def deep_get(d: Dict[str, Any], path: str) -> Any:
    keys = path.split(".")
    cur = d
    for k in keys:
        if not isinstance(cur, dict) or k not in cur:
            return None
        cur = cur[k]
    return cur

ISO_REGEX = re.compile(r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}')

def safe_iso_or_fallback(date_str: Optional[str]) -> str:
    """Return date_str if it looks ISO-ish, else return a safe UTC fallback."""
    if date_str and ISO_REGEX.match(date_str):
        return date_str
    return datetime.utcnow().replace(tzinfo=timezone.utc).isoformat()

def load_front_matter_from_md(path: str) -> Tuple[Optional[Dict], Optional[str]]:
    """Extract YAML front-matter from a Markdown file. Returns (yaml_dict, rest_of_file)."""
    if path == "-":
        text = sys.stdin.read()
    else:
        # tolerate BOM and leading whitespace
        with open(path, "r", encoding="utf-8-sig") as f:
            text = f.read().lstrip()
    # require fence at start of line with newline-bounded '---'
    if not text.startswith("---\n") and not text.startswith("---\r\n"):
        return None, text
    # split at the first newline-bounded '---' ending
    m = re.split(r'\n---\r?\n', text, maxsplit=1)
    if len(m) < 2:
        return None, text
    yaml_text = m[0][4:] if m[0].startswith("---") else m[0]
    # yaml_text might include the remainder if earlier split; handle remainder
    rest = m[1] if len(m) > 1 else ""
    try:
        data = yaml.safe_load(yaml_text) or {}
    except Exception as e:
        print(f"Error parsing YAML front-matter: {e}", file=sys.stderr)
        data = {}
    return data, rest

def map_aliases_to_canonical(src: Dict[str, Any], include_prompts: bool=False) -> Dict[str, Any]:
    """Map keys in src to canonical schema, returning the canonical dict."""
    canon = yaml.safe_load(yaml.safe_dump(CANONICAL_TEMPLATE))  # deep copy
    extensions = {}

    for k, v in (src.items() if isinstance(src, dict) else []):
        if k in CANONICAL_TEMPLATE:
            canon[k] = v
        else:
            lower_k = k.lower()
            if lower_k in ALIASES:
                target = ALIASES[lower_k]
                if target.endswith("prompt") and not include_prompts:
                    extensions[k] = "[redacted prompt]"
                    continue
                deep_set(canon, target, v)
            else:
                extensions[k] = v

    # Normalize authors into list of objects
    authors = canon.get("authors")
    if isinstance(authors, str):
        canon["authors"] = [{"name": authors, "type": "human"}]
    elif isinstance(authors, dict):
        authors.setdefault("type", "human")
        canon["authors"] = [authors]
    elif isinstance(authors, list):
        canon["authors"] = [
            (a if isinstance(a, dict) else {"name": str(a), "type": "human"})
            for a in authors
        ]
    # ensure generated_by is nested object if a string was provided
    gen = deep_get(canon, "provenance.generated_by")
    if isinstance(gen, str):
        deep_set(canon, "provenance.generated_by", {"name": gen, "type": "tool"})

    # Attach extensions
    canon["extensions"] = extensions
    return canon

def _prune_nones(obj):
    if isinstance(obj, dict):
        out = {}
        for k, v in obj.items():
            pr = _prune_nones(v)
            if pr is None or pr == {} or pr == []:
                continue
            out[k] = pr
        return out
    if isinstance(obj, list):
        out_list = []
        for x in obj:
            pr = _prune_nones(x)
            if pr is None:
                continue
            out_list.append(pr)
        return out_list
    return obj

def write_output(out_path: Optional[str], data: Dict[str, Any], prune: bool=False):
    if prune:
        data = _prune_nones(data)
    s = yaml.safe_dump(data, sort_keys=False, allow_unicode=True)
    if out_path:
        os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(s)
        print(f"Wrote canonical YAML to {out_path}")
    else:
        print(s)

def process_file(path: str, out: Optional[str]=None, include_prompts: bool=False, prune: bool=False):
    fm, _rest = load_front_matter_from_md(path)
    if fm is None:
        print(f"Warning: no YAML front-matter found in {path}", file=sys.stderr)
        fm = {}
    canonical = map_aliases_to_canonical(fm, include_prompts=include_prompts)
    # Ensure file_path is set in provenance if absent
    if not deep_get(canonical, "provenance.file_path"):
        deep_set(canonical, "provenance.file_path", path)
    # Default generated_at to date if available; apply ISO guard/fallback
    gen_at = deep_get(canonical, "provenance.generated_at")
    if not gen_at:
        date_val = canonical.get("date")
        if date_val:
            deep_set(canonical, "provenance.generated_at", safe_iso_or_fallback(date_val))
        else:
            deep_set(canonical, "provenance.generated_at", datetime.utcnow().replace(tzinfo=timezone.utc).isoformat())
    if out:
        write_output(out, canonical, prune=prune)
    else:
        write_output(None, canonical, prune=prune)

def process_directory(dir_path: str, out_dir: Optional[str]=None, recursive: bool=False, include_prompts: bool=False, prune: bool=False):
    for root, dirs, files in os.walk(dir_path):
        for fname in files:
            if not fname.lower().endswith(".md"):
                continue
            full = os.path.join(root, fname)
            rel = os.path.relpath(full, dir_path)
            if out_dir:
                target_dir = os.path.join(out_dir, os.path.dirname(rel))
                target_file = os.path.join(target_dir, os.path.splitext(os.path.basename(fname))[0] + ".yml")
            else:
                target_file = None
            process_file(full, out=target_file, include_prompts=include_prompts, prune=prune)
        if not recursive:
            break

def main():
    p = argparse.ArgumentParser(description="CAP/CRP front-matter adapter")
    p.add_argument("path", help="Markdown file or directory to adapt (use '-' for stdin)")
    p.add_argument("--out", "-o", help="Output file path (for single file)")
    p.add_argument("--out-dir", help="Output directory (for directory mode). If omitted, prints to stdout.")
    p.add_argument("--recursive", action="store_true", help="Recurse directories")
    p.add_argument("--include-prompts", action="store_true", help="Include generator prompts (sensitive); default: false")
    p.add_argument("--prune-empty", action="store_true", help="Drop empty/None fields from output")
    args = p.parse_args()

    if os.path.isdir(args.path):
        process_directory(args.path, out_dir=args.out_dir, recursive=args.recursive, include_prompts=args.include_prompts, prune=args.prune_empty)
    elif os.path.isfile(args.path) or args.path == "-":
        process_file(args.path, out=args.out, include_prompts=args.include_prompts, prune=args.prune_empty)
    else:
        print(f"Path not found: {args.path}", file=sys.stderr)
        sys.exit(2)

if __name__ == "__main__":
    main()
