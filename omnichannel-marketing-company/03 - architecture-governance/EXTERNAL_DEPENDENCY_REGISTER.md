# External Dependency Register

Type: governance register (Tier 2 — append rows, update Status/Substitute cells; never delete a row).
Created: 2026-09-25, session S001.
Operator: `00-control/tools/check_links.py` reads the table below. A path reference that leaves this repo and matches no row here FAILS the link check (class `UNREGISTERED`).

## Why this exists

The departments in this company were extracted from a larger CE workspace (FORGE, WORKSPACE_META, Arena, sibling companies). Their instructions still point at that workspace. None of it is in this repo. Rather than delete those paths (they are true lineage) or leave a cold instance to chase them, every external target is registered here with:

- **what it is** and **why the instructions need it**, and
- the **local substitute** a cold instance uses in this repo instead — or an honest `UNAVAILABLE` with what it blocks.

## Status values

| Status | Meaning |
|---|---|
| SUBSTITUTED | A file in this repo already performs the function. Use it. |
| STAGED-SUBSTITUTE | The substitute is defined but not yet built or exercised. The gap register tracks the build. |
| UNAVAILABLE | No substitute. Named work is blocked until one exists or a human supplies it. |
| LINEAGE | Provenance only. Nothing in this repo needs it at runtime. |

## Register

Match column: backticked path segments. The checker matches a reference when a segment equals one or more whole path components of it. Rows are matched top to bottom — specific rows sit above the general CE-root rows (X-13 to X-15).

| ID | Match | What it is | Why the instructions need it | Local substitute in this repo | Status |
|---|---|---|---|---|---|
| X-01 | `RESEARCH_FIRST_CONTENT_PRODUCTION.md` | CE governance rule: no drafting before research (4-check pre-drafting gate, anti-patterns) | Declared "Governance" parent of the writing and distribution departments | `03 - architecture-governance/01 - content-infrastructure/01 - research-first-content-production.md` (the spec it was realized from) + spec `13 - blog-as-knowledge-production.md` anti-pattern list + `01 - writing-department/WORKING_RULES.md` Rule 1 | SUBSTITUTED |
| X-02 | `knowledge_sufficiency_gate.py`, `09 - ingestion-and-knowledge` | KSE Gate 8: scores 6 research-sufficiency dimensions and refuses to dispatch when any is LOW | Named as the mechanical operator of research depth in writing ENTRY, specs 01/08/12/14, RESEARCH_METHODOLOGY_REFERENCE | The 4-check pre-drafting gate (`01 - writing-department/WORKING_RULES.md` Rule 1), checked against `research-[slug]/` on disk using `01 - writing-department/02 - templates/research-domain-starter.md`. No script operator yet — see gap G-M02 | STAGED-SUBSTITUTE |
| X-03 | `01 - arena`, `finalize_arena_run.py`, `06 - promoted-artifacts` | Arena research runs and the Arena → Company promotion pipeline | Research expansion when KSE scores LOW; promotion receipts | A RESEARCH_DOSSIER (numbered, self-contained, runnable queries) under `02-sourcing/01 - dossiers/`, executed by an agent with web access or by a human | STAGED-SUBSTITUTE |
| X-04 | `lumina-arts`, `design-visual-artist-brand`, `13-media-department`, `04 - domains`, `19 - nb` | Media Department: visual asset production, image prompt bank, narrative engine | Every output contract (Substack, LinkedIn, Twitter/Threads, Facebook) makes a custom Media-produced visual mandatory | None in repo. Diagram-class graphics (frameworks, flows) can be authored in-repo as SVG; photo/illustration-class needs a human or an image tool. Blocks every visual-asset check — see gap G-X04 | UNAVAILABLE |
| X-05 | `WORK_AXIOM_BANK.md` | 256+ CONTEXT→RULE→OUTCOME axioms; the tacit→explicit transfer mechanism | Research compounding, framework reuse across articles and verticals | `meta_workspace.md` §5 (patterns seen) now; `13 - memory/` lessons + patterns-to-promote once Phase G creates it | STAGED-SUBSTITUTE |
| X-06 | `DEPARTMENT_ROUTER.py`, `WORK_ROUTER.py`, `working_rules.py`, `domain-organ-map.md`, `00 - QUERY` | Deterministic dispatchers: objective → department + prerequisites + standards | `DEPARTMENT_FIRST_BUSINESS_MODEL.md` declares the router gap "CLOSED" on the strength of this script | Read `03 - architecture-governance/DEPARTMENT_REGISTRY.md` by hand. Rebuild a router only when a live objective must be routed across ≥2 departments (Build Order Law) | UNAVAILABLE |
| X-07 | `WORKSPACE_ORCHESTRATION_CONTRACT.md`, `CE_NATIVE_ORIENTATION.md`, `02 - orchestration-skill-creator`, `DETERMINISTIC_COGNITIVE_WORKSPACE_STAGING.md` | Workspace-level orchestration contract (gates, state ownership, anti-patterns, decision hierarchy) | "The workspace contract every company obeys" | `00-control/source-intent/01 - CLOUD_AI_HANDOFF.md` §2 (Company Law) and §5 (CE-native patterns) — the law inlined for this repo | SUBSTITUTED |
| X-08 | `session_end.py`, `session_seal.md`, `BODY_STATE.json`, `WAKE_STATE.md`, `run_pipeline.py`, `BOOT.py`, `BOOT_REPORT.md`, `REALIZED_FUNCTION_NODE.md` | CE boot and session-continuity chain | Cross-session inheritance | `00-control/STATE.md` + `meta_workspace.md` §3 session log (+ `HANDOFF.md` at build Phase I) | SUBSTITUTED |
| X-09 | `ce_worklist.py`, `CE_WORKLIST_SOURCES.json` | Deterministic worklist compiler | Prioritised next actions every session | `00-control/STATE.md` "Next actions" + `00-control/tools/derive_phase.py` | SUBSTITUTED |
| X-10 | `01 - cognitive-sequence` | 4-stage cognitive sequence (Grounding → Agent 1 → 2 → 3) that compiles sources into instructions | The compression step for research-dependent outputs | Articles: `01 - writing-department/01 - prompt-library/` stages 01–05. Business outputs (positioning, pitch, site): a compiler contract — not yet written (knowledge-work override, gap G-M06) | STAGED-SUBSTITUTE |
| X-11 | `03 - company-creation-protocol`, `01 - meta-company-template`, `01 - meta-company (copy this folder before modding)`, `CARBON_INTERFACE_PROTOCOL.md`, `00 - company tools` | Company-creation protocol: raw idea → packets → function folder; carbon interface; promotion to live company | This company's declared parent; the promotion route in the company ENTRY Runtime Law | Phase status: `00-control/tools/derive_phase.py`. Human input: CARBON_INPUT_FORM format (handoff §5 P3) in `00-control/carbon-input/`. The promotion route itself has no substitute — gap G-X11 | STAGED-SUBSTITUTE |
| X-12 | `lexbridge` | LexBridge company: the Law department, research-brief template, portability contract | Law dept OPERATIONAL claim; research brief template; engagement contracts for retained execution | None. Law status is unverifiable here; engagement/contract work (build Phases E–F) will need a human or a Law build | UNAVAILABLE |
| X-13 | `99 - ARCHIVE`, `05 - INPUT`, `06 - mission-blueprint` | Source intents: the archived design documents and Carbon's mission blueprint the departments and doctrines were derived from | Provenance ("Source intent" sections) | The realized documents in this repo are the operative text | LINEAGE |
| X-14 | `02 - WORKSPACE_META`, `01 - FORGE`, `SKILL_REGISTRY.md`, `CANONICAL_PATHS.md`, `TERMINOLOGY.md`, `PROMPT_ENGINEERING_CANON.md` | CE workspace roots: meta-governance, runtime, skills, canonical path map, terminology | Root maps and canonical terms | Root map: `00 - ENTRY.md` "Company Map" section. Terminology: none — terms are defined where used | LINEAGE |
| X-15 | `03 - work-projects`, `02 - working-companies`, `02 - working companies`, `02 - company` | Historical CE locations of this company, its departments and sibling companies (including phantom paths quoted in `DEPARTMENT_REGISTRY.md`'s topology note) | Navigation inside the original workspace | `00 - ENTRY.md` "Company Map" section | LINEAGE |

## Update rule

1. When `check_links.py` reports `UNREGISTERED`, either correct the path (if a local target exists) or add a row here. Never add a row for a path that has a local target.
2. When a substitute is built, update that row's Substitute and Status cells and note the date in `meta_workspace.md` §3.
3. General rows (X-13 to X-15) stay at the bottom so specific rows win.
