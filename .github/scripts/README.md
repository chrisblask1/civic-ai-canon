# CAP/CRP Adapter

`cap_adapter.py` maps variant front-matter into the Canonical CAP/CRP schema.

Common uses
- Single file → stdout:  
  `python3 .github/scripts/cap_adapter.py protocols/CRP-001_Canonical_Reflex_Protocol.md --prune-empty`
- Directory → `.provenance/` YAMLs:  
  `python3 .github/scripts/cap_adapter.py protocols/ --out-dir .provenance --recursive --prune-empty`

Privacy
- Prompts are **redacted by default**. Use `--include-prompts` only if policy allows.

Alias map
| Variant key | Canonical path |
|---|---|
| cap_id, cap_record | cap.cap_record_id |
| commit, sha | provenance.commit_sha |
| file, path | provenance.file_path |
| generator, generated | provenance.generated_by |
| semantic_summary | semantic.summary |
| author, creators | authors |
| attested_by | attestation |

Minimal Action step to run the adapter (optional)
```yaml
- name: Generate canonical provenance (.provenance/)
  run: |
    mkdir -p .provenance
    python3 .github/scripts/cap_adapter.py protocols/ --out-dir .provenance --recursive --prune-empty
- name: Upload provenance artifacts
  uses: actions/upload-artifact@v4
  with:
    name: provenance-yaml
    path: .provenance
```
