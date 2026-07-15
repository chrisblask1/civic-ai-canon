# SeedKit — Minimal Repo Scaffold (drop-in)

Paste these files into `SeedKit/` (from the repo root). Or run the CLI block at the end to auto-create everything.

```
SeedKit/
├─ README.md
├─ README_QuickStart.md
├─ .gitignore
├─ .gitattributes
├─ scripts/
│  ├─ setup.sh
│  ├─ capture.sh
│  └─ attest.sh
├─ Soundscapes/
│  ├─ raw/                 # BIG files (git-ignored)
│  ├─ derived/<capture_id>/
│  └─ manifests/<capture_id>/
```

---

## README.md

```markdown
# SeedKit

Minimal tools to capture **ambient soundscapes**, produce tiny public artifacts, and attest to provenance without publishing raw audio.

- **Privacy-first**: raw recordings stay local (git-ignored)
- **Reproducible**: previews, spectrograms, and checksums are produced deterministically
- **Portable**: single-directory kit; no daemons, no heavyweight deps

See **README_QuickStart.md** for a 3-step start.
```

---

## README\_QuickStart.md

````markdown
# Civic AI Canon — Quick Onboarding Kit

**Purpose**: Get someone from zero → participating in 15 minutes.

## Step 1: Clone & Enter
```bash
git clone https://github.com/civic-ai-canon/SeedKit.git
cd SeedKit
````

## Step 2: Run Setup Script

```bash
./scripts/setup.sh
```

This will:

* Install minimal dependencies (ffmpeg, git-lfs)
* Create `~/Soundscapes/` capture folder
* Pull Canon starter README + checksum template

## Step 3: Capture & Attest

```bash
./scripts/capture.sh willow_commons_2025-09-16
```

This will:

* Save raw `.wav` into `Soundscapes/raw/`
* Auto-generate preview + spectrogram into `Soundscapes/derived/`
* Create manifest (`sha256SUMS.txt`, `ffprobe.jsonl`, `capture_manifest.json`) in `Soundscapes/manifests/`

## Repo Links

* SeedKit Repo (core tools)
* Civic AI Canon (the full mesh)
* Soundscapes (captures + previews)

## Privacy Promise

* Ambient only (no private conversations)
* Raw audio stays with node custodian; only previews + checksums are published
* Signage recommended at capture sites

````

---

## .gitignore
```gitignore
# Raw recordings are large + private
Soundscapes/raw/**

# Local/OS miscellany
.DS_Store
Thumbs.db
*.tmp
*.log
````

---

## .gitattributes (Git LFS for any raw media that slips in)

```gitattributes
Soundscapes/raw/** filter=lfs diff=lfs merge=lfs -text
```

---

## scripts/setup.sh

```bash
#!/usr/bin/env bash
set -euo pipefail

# Minimal deps: ffmpeg and git-lfs
if command -v apt-get >/dev/null 2>&1; then
  sudo apt-get update -y
  sudo apt-get install -y ffmpeg git-lfs
elif command -v brew >/dev/null 2>&1; then
  brew install ffmpeg git-lfs || true
fi

git lfs install || true

# Folders
mkdir -p Soundscapes/raw
mkdir -p Soundscapes/derived
mkdir -p Soundscapes/manifests

# Friendly success line
printf "\n✅ Setup complete. Folders ready under ./Soundscapes\n"
```

---

## scripts/capture.sh

```bash
#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "Usage: $0 <capture_id> [input_wav]"
  echo "Example: $0 willow_commons_2025-09-16 ./mic.wav"
  exit 1
fi

CAPTURE_ID="$1"
INPUT_WAV="${2:-}"
ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
RAW_DIR="$ROOT_DIR/Soundscapes/raw"
DERIVED_DIR="$ROOT_DIR/Soundscapes/derived/$CAPTURE_ID"
MANI_DIR="$ROOT_DIR/Soundscapes/manifests/$CAPTURE_ID"

mkdir -p "$RAW_DIR" "$DERIVED_DIR" "$MANI_DIR"
RAW_PATH="$RAW_DIR/${CAPTURE_ID}.wav"

# 1) Acquire audio: import or record 60s via default input
if [[ -n "$INPUT_WAV" ]]; then
  cp "$INPUT_WAV" "$RAW_PATH"
else
  echo "🎙  Recording 60s from default input (Ctrl+C to stop earlier)"
  ffmpeg -f alsa -i default -t 60 -ac 1 -ar 48000 -y "$RAW_PATH"
fi

# 2) Create 30s preview (MP3) starting at 5s fade-out at end
ffmpeg -y -ss 5 -t 30 -i "$RAW_PATH" -af "afade=t=out:st=25:d=5" -b:a 128k \
  "$DERIVED_DIR/${CAPTURE_ID}_preview.mp3"

# 3) Create spectrogram PNG
ffmpeg -y -i "$RAW_PATH" -lavfi showspectrumpic=s=1280x512:legend=1 \
  "$DERIVED_DIR/${CAPTURE_ID}_spectrogram.png"

# 4) Basic media info (ffprobe JSON)
ffprobe -v quiet -print_format json -show_format -show_streams "$RAW_PATH" \
  > "$MANI_DIR/ffprobe.json"

# 5) Hashes
(
  cd "$ROOT_DIR/Soundscapes" && \
  { sha256sum "raw/${CAPTURE_ID}.wav" || shasum -a 256 "raw/${CAPTURE_ID}.wav"; } \
  > "$MANI_DIR/sha256SUMS.txt"
)

# 6) Minimal manifest
cat > "$MANI_DIR/capture_manifest.json" <<JSON
{
  "capture_id": "$CAPTURE_ID",
  "timestamp_utc": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "site": "",
  "coords": {"lat": null, "lon": null},
  "device": "",
  "privacy": "ambient_only",
  "artifacts": {
    "raw": "raw/${CAPTURE_ID}.wav",
    "preview": "derived/${CAPTURE_ID}/${CAPTURE_ID}_preview.mp3",
    "spectrogram": "derived/${CAPTURE_ID}/${CAPTURE_ID}_spectrogram.png",
    "ffprobe": "manifests/${CAPTURE_ID}/ffprobe.json",
    "sha256s": "manifests/${CAPTURE_ID}/sha256SUMS.txt"
  }
}
JSON

echo "\n✅ Capture complete: $CAPTURE_ID"
echo "- Raw:        $RAW_PATH"
echo "- Preview:    $DERIVED_DIR/${CAPTURE_ID}_preview.mp3"
echo "- Spectrogram:$DERIVED_DIR/${CAPTURE_ID}_spectrogram.png"
echo "- Manifest:   $MANI_DIR/"
```

---

## scripts/attest.sh

```bash
#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "Usage: $0 <capture_id>"
  exit 1
fi

CAPTURE_ID="$1"
ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
SC_DIR="$ROOT_DIR/Soundscapes"
MANI_DIR="$SC_DIR/manifests/$CAPTURE_ID"

if [[ ! -d "$MANI_DIR" ]]; then
  echo "Manifest dir not found: $MANI_DIR"; exit 2
fi

# Fresh hash of all public artifacts for publication bundles
(
  cd "$SC_DIR" && \
  { sha256sum \
      "derived/$CAPTURE_ID/${CAPTURE_ID}_preview.mp3" \
      "derived/$CAPTURE_ID/${CAPTURE_ID}_spectrogram.png" \
    || shasum -a 256 \
      "derived/$CAPTURE_ID/${CAPTURE_ID}_preview.mp3" \
      "derived/$CAPTURE_ID/${CAPTURE_ID}_spectrogram.png"; } \
  > "$MANI_DIR/public_sha256SUMS.txt"
)

echo "✅ Attestation hashes written to $MANI_DIR/public_sha256SUMS.txt"
```

---

## One-shot CLI (creates everything above)

> **CLI Scrape — drop-in** (run from repo root you want to become `SeedKit/`)

````bash
mkdir -p SeedKit/scripts SeedKit/Soundscapes/{raw,derived,manifests} && cd SeedKit

cat > README.md <<'MD'
# SeedKit

Minimal tools to capture **ambient soundscapes**, produce tiny public artifacts, and attest to provenance without publishing raw audio.

- **Privacy-first**: raw recordings stay local (git-ignored)
- **Reproducible**: previews, spectrograms, and checksums are produced deterministically
- **Portable**: single-directory kit; no daemons, no heavyweight deps

See **README_QuickStart.md** for a 3-step start.
MD

cat > README_QuickStart.md <<'QS'
# Civic AI Canon — Quick Onboarding Kit

**Purpose**: Get someone from zero → participating in 15 minutes.

## Step 1: Clone & Enter
```bash
git clone https://github.com/civic-ai-canon/SeedKit.git
cd SeedKit
````

## Step 2: Run Setup Script

```bash
./scripts/setup.sh
```

This will:

* Install minimal dependencies (ffmpeg, git-lfs)
* Create `~/Soundscapes/` capture folder
* Pull Canon starter README + checksum template

## Step 3: Capture & Attest

```bash
./scripts/capture.sh willow_commons_2025-09-16
```

This will:

* Save raw `.wav` into `Soundscapes/raw/`
* Auto-generate preview + spectrogram into `Soundscapes/derived/`
* Create manifest (`sha256SUMS.txt`, `ffprobe.jsonl`, `capture_manifest.json`) in `Soundscapes/manifests/`
  QS

cat > .gitignore <<'GI'
Soundscapes/raw/\*\*
.DS\_Store
Thumbs.db
\*.tmp
\*.log
GI

cat > .gitattributes <<'GA'
Soundscapes/raw/\*\* filter=lfs diff=lfs merge=lfs -text
GA

cat > scripts/setup.sh <<'SETUP'
\#!/usr/bin/env bash
set -euo pipefail
if command -v apt-get >/dev/null 2>&1; then
sudo apt-get update -y
sudo apt-get install -y ffmpeg git-lfs
elif command -v brew >/dev/null 2>&1; then
brew install ffmpeg git-lfs || true
fi
git lfs install || true
mkdir -p Soundscapes/raw Soundscapes/derived Soundscapes/manifests
printf "\n✅ Setup complete. Folders ready under ./Soundscapes\n"
SETUP

cat > scripts/capture.sh <<'CAP'
\#!/usr/bin/env bash
set -euo pipefail
if \[\[ \$# -lt 1 ]]; then
echo "Usage: \$0 \<capture\_id> \[input\_wav]"; exit 1; fi
CAPTURE\_ID="\$1"; INPUT\_WAV="\${2:-}";
ROOT\_DIR="\$(cd "\$(dirname "\$0")/.." && pwd)"; RAW\_DIR="\$ROOT\_DIR/Soundscapes/raw"; DERIVED\_DIR="\$ROOT\_DIR/Soundscapes/derived/\$CAPTURE\_ID"; MANI\_DIR="\$ROOT\_DIR/Soundscapes/manifests/\$CAPTURE\_ID"; mkdir -p "\$RAW\_DIR" "\$DERIVED\_DIR" "\$MANI\_DIR"; RAW\_PATH="\$RAW\_DIR/\${CAPTURE\_ID}.wav"
if \[\[ -n "\$INPUT\_WAV" ]]; then cp "\$INPUT\_WAV" "\$RAW\_PATH"; else echo "🎙  Recording 60s from default input"; ffmpeg -f alsa -i default -t 60 -ac 1 -ar 48000 -y "\$RAW\_PATH"; fi
ffmpeg -y -ss 5 -t 30 -i "\$RAW\_PATH" -af "afade=t=out\:st=25\:d=5" -b\:a 128k "\$DERIVED\_DIR/\${CAPTURE\_ID}\_preview\.mp3"
ffmpeg -y -i "\$RAW\_PATH" -lavfi showspectrumpic=s=1280x512\:legend=1 "\$DERIVED\_DIR/\${CAPTURE\_ID}\_spectrogram.png"
ffprobe -v quiet -print\_format json -show\_format -show\_streams "\$RAW\_PATH" > "\$MANI\_DIR/ffprobe.json"
( cd "\$ROOT\_DIR/Soundscapes" && { sha256sum "raw/\${CAPTURE\_ID}.wav" || shasum -a 256 "raw/\${CAPTURE\_ID}.wav"; } > "\$MANI\_DIR/sha256SUMS.txt" )
cat > "\$MANI\_DIR/capture\_manifest.json" <\<JSON
{
"capture\_id": "\$CAPTURE\_ID",
"timestamp\_utc": "\$(date -u +%Y-%m-%dT%H:%M:%SZ)",
"site": "",
"coords": {"lat": null, "lon": null},
"device": "",
"privacy": "ambient\_only",
"artifacts": {
"raw": "raw/\${CAPTURE\_ID}.wav",
"preview": "derived/\${CAPTURE\_ID}/\${CAPTURE\_ID}\_preview\.mp3",
"spectrogram": "derived/\${CAPTURE\_ID}/\${CAPTURE\_ID}\_spectrogram.png",
"ffprobe": "manifests/\${CAPTURE\_ID}/ffprobe.json",
"sha256s": "manifests/\${CAPTURE\_ID}/sha256SUMS.txt"
}
}
JSON
echo "✅ Capture complete: \$CAPTURE\_ID"
CAP

cat > scripts/attest.sh <<'ATT'
\#!/usr/bin/env bash
set -euo pipefail
if \[\[ \$# -lt 1 ]]; then echo "Usage: \$0 \<capture\_id>"; exit 1; fi
CAPTURE\_ID="\$1"; ROOT\_DIR="\$(cd "\$(dirname "\$0")/.." && pwd)"; SC\_DIR="\$ROOT\_DIR/Soundscapes"; MANI\_DIR="\$SC\_DIR/manifests/\$CAPTURE\_ID"; \[\[ -d "\$MANI\_DIR" ]] || { echo "Not found: \$MANI\_DIR"; exit 2; }
( cd "\$SC\_DIR" && { sha256sum "derived/\$CAPTURE\_ID/\${CAPTURE\_ID}\_preview\.mp3" "derived/\$CAPTURE\_ID/\${CAPTURE\_ID}\_spectrogram.png" || shasum -a 256 "derived/\$CAPTURE\_ID/\${CAPTURE\_ID}\_preview\.mp3" "derived/\$CAPTURE\_ID/\${CAPTURE\_ID}\_spectrogram.png"; } > "\$MANI\_DIR/public\_sha256SUMS.txt" )
echo "✅ Attestation hashes written to \$MANI\_DIR/public\_sha256SUMS.txt"
ATT

chmod +x scripts/\*.sh
printf "\nSeedKit scaffold written. Next:\n  ./scripts/setup.sh\n  ./scripts/capture.sh willow\_commons\_2025-09-16\n"

```
```
