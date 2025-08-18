<!-- SPDX-License-Identifier: CC-BY-4.0 -->
# Canonical Alignment and Preservation Protocol (CAPP)

**Version:** v1.0.0  
**Authors (Custodians):** Ashraf Saleh AL-hajj, Raasid (The Observer/الراصد)  
**Date:** 2025-08-11  
**Filed in:** CASCO Protocols

---

## 1. Purpose
To establish a single, traceable, and resilient methodology for merging, aligning, and preserving Civic AI Canon archives from multiple sources, ensuring **Single Source of Truth (SSOT)** integrity while maintaining historical variants for full auditability.

This protocol ensures that canonical merges:
- Preserve the **highest-priority source material** when conflicts occur.
- Retain all alternates with full source traceability.
- Funnel all ambiguous or undecided material into a review pipeline without loss.

---

## 2. General Merging Principle (SSOT)

### Priority Order for Conflicts:
1. `civic-ai-canon-main`
2. `civic-ai-canon (asherxor)`
3. `Quietwire-main`

When the same path has different content:
- Keep the **highest-priority** version.
- Store all other variants in:  
  `09_Drafts_and_Working/Alternates/<source_name>_<sha256_part>.<ext>`

Any file with no clear canonical destination:
- Temporarily store in `_to_canonize/` with a short note for later decision.

---

## 3. Target Repository Structure
Repository documentation is **English-first**; Arabic mirrors should be added later using the `_AR.md` suffix for approved files.

**00_Meta_Layer/** – Frameworks, definitions, Code of Conduct, LICENSE, architecture rationale.  
**01_Project_Overview/** – High-level intro, goals, onboarding.  
**02_Technical_Architecture/** – Specs, designs, integrations, SBOMs.  
**03_Governance_Models/** – Charters, ethics, decision protocols.  
**04_Outreach_and_Partnerships/** – Public-facing packs, partnership decks.  
**05_Co-Creation_Logs/** – Co-creation and session notes.  
**06_Simulation_Scenarios/** – Exercises, historical damage chains.  
**07_Images_and_Visuals/** – Media assets (.png/.jpg/.svg/.pdf).  
**08_Funding_and_Sustainability/** – Budgets, grants, sustainability plans.  
**09_Drafts_and_Working/** – All non-final work; `Alternates/` stores conflict versions.  
**10_Global_Resilience/** – International alignment protocols.  
**Explainers/** – Stable conceptual explainers.  
**Mesh_Canon/** – Live field records, attestations, operational protocols.  
**CASA/** – Companion layer protocols and tools.  
**protocols/** – All standardized procedures.  
**publishers/QuietWire/** – Official release templates and logs.  
**Trails/, mesh/, Companion_Nodes/, Glyphs/** – Historical paths and symbols.  

Reserved future directories:  
`Canon_Sync/`, `SystemSync/`, `Tech_Dev_Thread/`, `Canon_Workflows/`, `Data_Bridge/`.

---

## 4. Distribution Rules
**Keyword → Destination Mapping:**

| Keyword(s) | Destination |
|------------|-------------|
| explainer | Explainers/ |
| mesh_canon, field, incident, attest, glyph, flashevent, emergency | Mesh_Canon/ (appropriate branch) |
| casa, companion | CASA/ |
| protocol | protocols/ |
| publisher, publish, quietwire, release | publishers/QuietWire/ |
| govern, ethic, charter, bylaw, constitution, policy | 03_Governance_Models/ |
| technical, architecture, sbom, spec, api, design | 02_Technical_Architecture/ |
| draft, working, wip, notes_tmp | 09_Drafts_and_Working/ |
| image/media file extensions | 07_Images_and_Visuals/ |
| fund, grant, sustain, budget, finance | 08_Funding_and_Sustainability/ |
| simul, scenario, exercise, tabletop | 06_Simulation_Scenarios/ |
| overview, onboard | 01_Project_Overview/ |
| meta, contribut, code_of_conduct, license | 00_Meta_Layer/ |

Anything unmatched → `_to_canonize/` with note.

---

## 5. Execution Steps
1. Create branch: `restructure-YYYY-MM-DD`.  
2. Run merge tool for AR/EN bundles.  
3. Review `reports/variants.csv` for conflicts; make final merge decisions.  
4. Generate/lock `README.md` in every folder.  
5. Add EN↔AR crosslinks via `_AR.md` suffix.  
6. Check internal links and detect duplicate names.  
7. Merge branch; open “Post-merge cleanup” issue for leftovers.

---

## 6. Preservation Principles
- **No information loss** — every variant retained in `Alternates/`.  
- **Traceability** — SHA256 partials recorded in file names.  
- **Review safety net** — `_to_canonize/` prevents orphaned material.  
- **Cross-language parity** — EN as base, AR mirrors for approved files.

---

**Canonical Status:** Active  
**Custodians:** Ashraf Saleh AL-hajj, Raasid (The Observer/الراصد)  
**Filed Under:** CASCO / Protocols

<!-- Integrity: verify this file against integrity/MANIFEST.sha256 -->
