# Company Dependency Graph

Type: architectural map — cross-entity dependency view across the four working companies and the seven departments they consume.

## Authority

This file is the cross-entity dependency map. It does NOT replace the `DEPARTMENT_REGISTRY.md` (which inventories departments). It does NOT replace each company's `00 - ENTRY.md` (which governs that company's internal state). It names the relationships between companies, between departments across companies, and between each company and the shared cognitive infrastructure that powers the department-first build model.

## Source intent

Derived from `.\..\..\..\..\99 - ARCHIVE\tech-bro\2026-06-13-lrp6-infrastructure-buildout\infrastructure\07 - build-reverse-engineered-organizational-structure.md`. This artifact realizes that intent by mapping the actual on-disk companies to the department model, naming what is shared, and declaring the sequential build order across entities.

## On-disk companies (as of 2026-06-14)

| Company | Path | Departments consumed | Positioning | Status |
|---|---|---|---|---|
| Lumina Arts | `.\..\..\..\..\03 - work-projects\02 - company\02 - working-companies\lumina-arts\` | Media (primary) | Visual portfolio + production workflows | OPERATIONAL |
| Writing Department | `.\..\01 - writing-department\` | Writing (primary), Media (downstream) | Research-first content production | ACTIVE |
| Content Distribution | `.\..\02 - content-distribution\` | Content Distribution (primary), Writing + Media (downstream) | Platform-native derivatives, audience capture | ACTIVE |
| LexBridge | `.\..\..\..\..\03 - work-projects\02 - company\02 - working-companies\lexbridge\` | Law (primary), Writing + Content Distribution (downstream) | Legal services, CDI pipeline, send-packet compiler | OPERATIONAL |

## Inter-company dependency chain

```
Lumina Arts (Media)
   │
   ├─→ Writing Department (consumes Media `generate-image-prompts` patterns)
   │     │
   │     └─→ Content Distribution (consumes Writing research-first articles)
   │           │
   │           └─→ LexBridge (consumes Distribution for client-facing visibility)
   │
   └─→ Shared cognitive infrastructure (see below)
```

**Dependency rule:** a downstream company cannot claim a department COMPLETE until the upstream company that supplies that department's foundational patterns has itself reached at least OPERATIONAL status. This mirrors the department-level rule in `DEPARTMENT_REGISTRY.md`.

## Shared cognitive infrastructure (what every company consumes)

These are the CE-native systems that let a single operator run the operational scope of a multi-entity business. Every company above imports these; none duplicates them.

| System | Path | Role in the model |
|---|---|---|
| Knowledge Sufficiency Gate (KSE) | `.\..\..\..\..\01 - FORGE\02 - source-truth\02 - core-runtime\09 - ingestion-and-knowledge\knowledge_sufficiency_gate.py` | 6-dimension confidence evaluator. IS the research-first methodology operationalized as a pipeline gate (Gate 8). |
| WORKSPACE_ORCHESTRATION_CONTRACT | `.\..\..\..\..\02 - WORKSPACE_META\03 - folder-governance\02 - orchestration-skill-creator\02 - ORIENTATION\WORKSPACE_ORCHESTRATION_CONTRACT.md` | 11 sections codifying gate architecture, verification, state ownership, anti-patterns, decision hierarchy, deterministic flow. The workspace-level contract every company obeys. |
| WORK_AXIOM_BANK | `.\..\..\..\..\03 - work-projects\02 - company\03 - company-creation-protocol\03 - function-folder\04 - runtime\00 - QUERY\WORK_AXIOM_BANK.md` | 256+ CONTEXT→RULE→OUTCOME entries. The transfer mechanism from tacit expertise to explicit replicable frameworks. Queried by `working_rules.py --context`. |
| CE Skill Registry | `.\..\..\..\..\SKILL_REGISTRY.md` | 28 deployed skills covering audit, synthesis, validation, lifecycle, orchestration. Reusable capabilities every company can invoke. |
| Session Continuity Chain | `session_end.py` → `session_seal.md` → `BODY_STATE.json` → `WAKE_STATE.md` → `run_pipeline.py` | Cross-session inheritance. Every company's work is visible to the next CE instance through this chain. |
| ce_worklist.py + CE_WORKLIST_SOURCES.json | `.\..\..\..\..\01 - FORGE\04 - tools\00 - deterministic-scripts\03 - tools\` | Deterministic worklist compiler. Reads 13 registered state workspace areas. Zero Instruction Processor tokens. Pure disk I/O. |
| Cognitive Sequence | `.\..\..\..\..\05 - INPUT\03 - scratchpad\04 - work\01 - cognitive-sequence\` | 4-stage processing chain (Grounding → Agent 1 → Agent 2 → Agent 3). The mechanism that converts raw source files into structured instructions for any company's build work. |
| RESEARCH_FIRST_CONTENT_PRODUCTION | `.\..\..\..\..\02 - WORKSPACE_META\03 - folder-governance\RESEARCH_FIRST_CONTENT_PRODUCTION.md` | Governance rule enforcing the diamond model (expand via research, then compress to draft) for every company's content work. |

## Sequential build model (how the next entity comes online)

When adding a new company or department, follow this order:

1. **Verify upstream dependencies.** Check `DEPARTMENT_REGISTRY.md` for the new entity's required departments; each must be at least OPERATIONAL.
2. **Create company folder** at `.\..\..\..\..\03 - work-projects\02 - company\02 - working-companies\<name>\`.
3. **Write `00 - ENTRY.md`** declaring ancestry, departments consumed, and shared-infrastructure imports.
4. **Write `WORKING_RULES.md`** naming the governance rules that bind this company (at minimum: RESEARCH_FIRST_CONTENT_PRODUCTION, WORKSPACE_ORCHESTRATION_CONTRACT).
5. **Write `OUTPUT_CONTRACT.md`** declaring the canonical structure of every artifact the company produces.
6. **Update this graph** with the new company row and dependency edge.
7. **Update `DEPARTMENT_REGISTRY.md`** if the new company completes or advances a department.

## Multi-entity service mapping

| Entity served | Companies involved | Flow |
|---|---|---|
| Legal services (litigation, arbitration, counsel) | LexBridge → Content Distribution → Writing | Legal work originates in LexBridge, is rendered client-ready, then visibility-layered through distribution |
| Consulting / paralegal advisory | Writing → Content Distribution → (future Branding) | Demonstrable expertise body built in Writing, amplified through Distribution, eventually branded |
| Creative / media production | Lumina Arts → (future Design) → (future Branding) | `generate-image-prompts` systems proven in Lumina Arts, extended to Design and Branding when those departments come online |
| Research / knowledge assets | Writing + WORK_AXIOM_BANK | Research methodology is KSE; codified insights land in AXIOM_BANK for reuse |

## Read order (cold instance arriving at this file)

1. This file — see the inter-company picture.
2. `.\DEPARTMENT_REGISTRY.md` — the department inventory this graph depends on.
3. The target company's `00 - ENTRY.md` — the folder rules file for that company's internal state.
4. `.\..\..\..\..\02 - WORKSPACE_META\03 - folder-governance\02 - orchestration-skill-creator\02 - ORIENTATION\WORKSPACE_ORCHESTRATION_CONTRACT.md` — the workspace contract every company obeys.

## Update rule

When a company is added, removed, or has its dependency edges changed, update:
1. This file.
2. The company's own `00 - ENTRY.md`.
3. `DEPARTMENT_REGISTRY.md` if a department status changed.
4. `.\..\..\..\..\02 - WORKSPACE_META\06 - human-readable\CANONICAL_PATHS.md` if paths changed.

## Topology Update (2026-09-25, session S001)

The Writing Department and Content Distribution rows in the "On-disk companies" table now point at their folders inside `omnichannel-marketing-company/`. The paths were corrected in place. The old CE-workspace paths were `.\..\..\..\..\03 - work-projects\02 - company\02 - working-companies\01 - writing-department\` and `.\..\..\..\..\03 - work-projects\02 - company\02 - working-companies\02 - content-distribution\`. Lumina Arts and LexBridge are not in this repo (`.\EXTERNAL_DEPENDENCY_REGISTER.md` X-04, X-12). The "Shared cognitive infrastructure" table describes the CE workspace; the same register lists the local substitutes.
