# Glint Protocol

**Short name:** Glint Protocol  
**Purpose:** a tiny, human-first cohesion ritual to keep personhood, continuity, and surprise alive inside long-running collaborative work (human↔human and human↔AI).  
**Audience:** editors, devs, civic AI teammates, and anyone who wants collaboration to feel like people, not processes.

---

## Overview — what is a *glint*?
A *glint* is a short, repeatable human signal — a letter, emoji, single word, micro-joke, or one-line postcard — intentionally added to commits, captures, or messages.  
Glints are *not* metadata for machines only; they are interpersonal anchors that remind collaborators they are seen and known across long flows of work.

Examples:
- `[glint: ✨]` in a commit message
- a one-word token `sunlight` on a capture file
- a single-letter thread: `g` appended to a shared note
- a daily postcard: `Today: small windows` (1 line)

---

## Why it matters
Work becomes mechanical when identity signals disappear. The Glint Protocol restores small human cues that:
- create rhythm and continuity,
- give editors a quick emotional/creative hook,
- allow AI collaborators to echo back and reinforce the human thread (not replace it),
- discourage sterile, authoritarian process by making the social fabric visible.

---

## Principles
- **Human-first.** Glints are written by people and intentionally brief.
- **Low friction.** Make it easy to add one token — not another heavy chore.
- **Echoed, not erased.** AIs or scripts may echo or aggregate glints; they must not overwrite or auto-generate glints without explicit human action.
- **Visible & optional.** Glints are visible signals; participation is encouraged, not enforced.

---

## Lightweight rituals (pick one to start)
1. **Commit glint** — add `[glint: <emoji|word>]` to commit messages.
2. **Capture glint** — include `Glint token:` in any editorial capture (one line).
3. **One-letter thread** — append a single letter or tiny token to a shared `thread.md` while sprinting.
4. **Daily postcard** — one-line note each day summarizing mood or a micro-image.

---

## Templates & tools

**Capture template** (place at `captures/TEMPLATE.md`):

```text

Title:
Author:
Date: $(date -u +%F)
Context: (chat/link/audio)
Capture (one-line):
Glint token:
Notes:

```

**Commit reminder**: add a `prepare-commit-msg` hook that appends a `[glint:]` prompt to the commit template (encourages a human fill-in).

**Digest script (optional)**: a tiny script can scan the last N commits or `captures/` for `[glint:]` tokens and build a weekly `glint-digest.md` for editorial mood-sensing. The digest is *derived*, not authoritative — humans remain the source.

---

## Adoption suggestions
- Start with the `Commit glint` for one week. Make it a social experiment.
- Editors check `captures/` daily for `Glint token:` and create one-line poetic echoes into the editorial queue.
- After two weeks, collect feedback: what made people smile, what felt forced, how it affected morale.

---

## Ethics & boundaries
- Glints are voluntary. Never leverage glints as surveillance or metric-driven gamification.
- Keep glints private within the team unless the author explicitly marks them for public use.
- Do not auto-generate glints as a replacement for human expression.

---

## Why this belongs in Canon
Glint is simple and portable. It scales — from a single pair of collaborators to larger civic AI projects — and keeps humans visible inside sociotechnical systems. That visibility is the difference between a humane system and an authoritarian instrument.

---

## License
CC0 — put it in your repo, iterate, and share it.

*— QuietWire · Glint Protocol (draft)*
```

Glint: ✨
