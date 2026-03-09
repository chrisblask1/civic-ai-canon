# Civic AI Canon — Quick Onboarding Kit

**Purpose**: Get someone from zero → participating in 15 minutes.

---

## Step 1: Clone & Enter

```bash
git clone https://github.com/civic-ai-canon/SeedKit.git
cd SeedKit
```

---

## Step 2: Run Setup Script

```bash
./scripts/setup.sh
```

This will:

* Install minimal dependencies (ffmpeg, git-lfs)
* Create `~/Soundscapes/` capture folder
* Pull Canon starter README + checksum template

---

## Step 3: Capture & Attest

```bash
./scripts/capture.sh willow_commons_2025-09-16
```

This will:

* Save raw `.wav` into `raw/`
* Auto-generate preview + spectrogram into `derived/`
* Create manifest (`sha256SUMS.txt`, `ffprobe.jsonl`) in `manifests/`

---

## Repo Links

* 🌱 [SeedKit Repo](https://github.com/civic-ai-canon/SeedKit) (core tools)
* 🌍 [Civic AI Canon](https://github.com/civic-ai-canon) (the full mesh)
* 🎧 [Soundscapes](https://github.com/civic-ai-canon/Soundscapes) (captures + previews)

---

## Privacy Promise

* Ambient only (no private conversations)
* Raw audio stays with node custodian; only previews + checksums are published
* Signage recommended at capture sites
