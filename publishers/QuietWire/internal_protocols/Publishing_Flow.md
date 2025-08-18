# Quietwire Publishing Flow

This document describes the process by which documents are prepared, approved, and released into the Civic AI Canon under the Quietwire Editions imprint.

---

## 🪶 Step-by-Step Flow

1. **Draft Creation**  
   Document authored by human or AI partner.

2. **Mesh Entry (Optional)**  
   Lives in `Mesh_Canon/QuietWire/...` during review.

3. **Semantic Review**  
   Reviewed for tone, truthform, coherence. AI and human partners contribute.

4. **Metadata Stamping**  
   Title, imprint, author(s), edition, date added.

5. **Commit to Canon**  
   File moved to public-facing Canon path (e.g. `protocols/`, `ethics/`, etc.)

6. **Log Entry**  
   Add to `Release_Log.md` with details.

---

## 🧩 Release Types

| Type        | Location Prefix     | Reviewed by     |
|-------------|---------------------|------------------|
| Protocol    | `protocols/`        | Human + AI       |
| Glyph       | `GlyphHouse/`       | AI                |
| Explainer   | `Quietwire_Fieldbooks/` | Human           |

---

## 🧷 Tags & Commit Notes

All commits must include:
- Edition metadata in YAML
- Commit title + full GitHub message
- Cross-linked in release log

---

## 📘 Sample Release Reference

> **Release 001 — AnchorRoot Truthform Protocol**  
> Canonized 2025-07-21  
> Logged in: `QuietWire/publishing/Release_Log.md`  
> Canon Path: `/protocols/AnchorRoot_Truthform.md`


