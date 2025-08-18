<!-- SPDX-License-Identifier: CC-BY-4.0 -->
# Canonical Reorganization Plan — Pre-Execution (EN)

**Authors:** Ashraf Saleh AL-hajj, Raasid (The Observer/الراصد)  
**Date:** 2025-08-11  
**Status:** Pre-execution (for review)  
**Reference:** See `protocols/CASCO/Canonical_Alignment_and_Preservation_Protocol.md` (CAPP)

---

## General Merging Principle (SSOT)

**Priority when conflicts occur:**  
`civic-ai-canon-main` → `civic-ai-canon (asherxor)` → `Quietwire-main`.

When the same path has different content: keep the **highest-priority** source version; store the rest under  
`09_Drafts_and_Working/Alternates/…` with the source name and part of the `sha256` hash for traceability.

Any file with no clear destination goes temporarily to `_to_canonize/` with a short note for later decision.

---

## Final Structure (Target Structure)

> Repository documentation will be **English-first**, with Arabic mirrors later as `*_AR.md`.

- **00_Meta_Layer/** — Frameworks, top-level definitions, Code of Conduct, LICENSE, contribution guides, architectural rationale.  
  *Examples:* Core READMEs, "Why/How" docs, structure justification.

- **01_Project_Overview/** — Intro for newcomers (what, goals, how to join).  
  *Goes here:* Onboarding, general definitions, any `Overview.md`.

- **02_Technical_Architecture/** — Specs, designs, integrations, cognitive structures, SBOM/Interfaces.  
  *Goes here:* API/Specs/Design, `Cognitive_Infrastructure/`, diagrams.

- **03_Governance_Models/** — Governance/ethics/charters, decision processes, conflict management.  
  *Goes here:* charters/bylaws/policies/ethics.

- **04_Outreach_and_Partnerships/** — Public materials, info packs, partnership guides, decks.

- **05_Co-Creation_Logs/** — Co-creation logs and standardized reporting formats.

- **06_Simulation_Scenarios/** — Simulation scenarios, response exercises, historical damage chains.

- **07_Images_and_Visuals/** — All visual media (images/icons/logos/drawings).  
  *Goes here:* `*.png *.jpg *.svg *.pdf` (visual) and design assets.

- **08_Funding_and_Sustainability/** — Funding, grants, budgets, sustainability models.

- **09_Drafts_and_Working/** — All non-final drafts; `Alternates/` holds conflicts.  
  *Rule:* No drafts outside this folder.

- **10_Global_Resilience/** — International alignment/bridging protocols.

- **Explainers/** — Stable conceptual explainers (Basics/Ethics/Operational Mesh/Security…).

- **Mesh_Canon/** — Live field: events/incidents, attestations, operational protocols.  
  *Branches:* `Field_Incidents/`, `FlashEvents/`, `Emergency_Attestations/`  
  *Time naming:* `YYYY-MM-DD_Title.md`.

- **CASA/** — Companion layer: protocols, perseverance threads, mental paths.  
  *Examples:* “Node_Ashraf_001”, Kusanagi practices, companion tools.

- **protocols/** — Reference index for all protocols (attestation/node-aid/resilience…).  
  *Rule:* When an Explainer becomes standard procedure → move here and link to its context.

- **publishers/QuietWire/** — Official publishing channel: templates, releases, publishing log.

- **Trails/, mesh/, Companion_Nodes/, Glyphs/** — Historical paths/symbols/threads (preserved, re-indexed).

- **Future (scaffolded):** `Canon_Sync/`, `SystemSync/`, `Tech_Dev_Thread/`, `Canon_Workflows/`, `Data_Bridge/`.

---

## Distribution Rules — Based on What Exists

- `explainer` → `Explainers/`  
- `mesh_canon|field|incident|attest|glyph|flashevent|emergency` → `Mesh_Canon/` (best branch)  
- `casa|companion` → `CASA/`  
- `protocol` → `protocols/`  
- `publisher|publish|quietwire|release` → `publishers/QuietWire/`  
- `govern|ethic|charter|bylaw|constitution|policy` → `03_Governance_Models/`  
- `technical|architecture|sbom|spec|api|design` → `02_Technical_Architecture/`  
- `draft|working|wip|notes_tmp` → `09_Drafts_and_Working/`  
- Image/media extensions → `07_Images_and_Visuals/`  
- `fund|grant|sustain|budget|finance` → `08_Funding_and_Sustainability/`  
- `simul|scenario|exercise|tabletop` → `06_Simulation_Scenarios/`  
- `overview|onboard` → `01_Project_Overview/`  
- `meta|contribut|code_of_conduct|license` → `00_Meta_Layer/`

**Legacy paths stay:** `Trails/`, `mesh/`, `Companion_Nodes/`, `Glyphs/`.  
**Trim** original roots (no `civic-ai-canon-main/…` inside the target tree).  
**Unmatched** → `_to_canonize/` with a note.

---

## Practical Examples — Where Does What Go?

- `AttestedMeshNodes.md`, structure-justification, `CONTRIBUTING.md`, `LICENSE` → `00_Meta_Layer/`.  
- `Explainer_*`, Harmonic/Attestation explainers → `Explainers/`.  
- `Cognitive_Infrastructure/`, SBOM/Interface/Design files → `02_Technical_Architecture/`.  
- Charters/policies/Ethics → `03_Governance_Models/`.  
- Field threads/ops logs/timestamped notices → `Mesh_Canon/` (proper branch).  
- QuietWire editing/releases/templates → `publishers/QuietWire/`.  
- All WIP/drafts → only `09_Drafts_and_Working/`.  
- Path conflict → keep approved copy + alternates in `09_Drafts_and_Working/Alternates/…`.

> Exact mappings live in `reports/files_mapping.csv` inside the generated AR/EN bundles.

---

## Quick Execution Steps (Ready-to-run)

1. Create branch: `restructure-2025-08`.  
2. Run the merge tool (AR/EN bundles already produced).  
3. Review `reports/variants.csv` and finalize conflicts if needed.  
4. Generate/lock unified `README.md` in every folder.  
5. Add EN↔AR crosslinks via `(_AR).md`.  
6. Check internal links and detect duplicate names.  
7. Merge branch; open an issue “Post-merge cleanup”.