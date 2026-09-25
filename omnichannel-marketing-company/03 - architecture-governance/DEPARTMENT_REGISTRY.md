# Department Registry

Type: governance document — the canonical inventory of all departments in the sequential deployment model.

## Authority

This file is the single source of truth for department status, dependencies, and function folder locations. When any department is built, completed, or restructured, update this file first.

## Deployment Model

Departments are built in sequence, not simultaneously. Each department's output creates the foundation the next department needs. This is a factory pipeline.

## Registry

| # | Department | Status | Function Folder | Core Output | Depends On |
|---|---|---|---|---|---|
| 1 | Media | COMPLETE | `.\..\..\02 - working-companies\lumina-arts\13-media-department\` (template origin) + `.\..\..\02 - working-companies\design-visual-artist-brand\01 - foundation\13-media-department\03 - media-production\` (operational) | Visual assets, production workflows, prompt bank | — |
| 2 | Writing | ACTIVE | `.\..\01 - writing-department\` | Research-first articles, newsletters, knowledge production | 1 |
| 3 | Content Distribution | ACTIVE | `.\..\02 - content-distribution\` | Platform-native derivatives, 30-day deployment, audience capture | 1, 2 |
| 4 | Law | OPERATIONAL | `.\..\..\02 - working-companies\lexbridge\06 - law-work\` (informal area; not yet formalized as Function Node) | Legal services, contracts, compliance frameworks | — |
| 5 | Design | PLANNED | `.\..\..\02 - working-companies\design-visual-artist-brand\` (build-out in progress) | Brand identity, visual systems, design templates | 1, 2, 4 |
| 6 | Branding | PLANNED | — | Strategic positioning, market identity, brand architecture | 1, 2, 4, 5 |
| 7 | Operations | PLANNED | — | Cross-department coordination, resource allocation | All above |

## Topology Reconciliation (2026-08-18, D1 EXECUTED)

Previously this registry cited `.\02 - working-companies\writing-department\`, `.\02 - working-companies\content-distribution\`, and `.\03 - work-projects\02 - company\05 - architecture-governance\` — all phantom on disk. Actual topology at that date (verified 2026-08-18): Writing and Content Distribution sat inside `omnichannel-marketing-company\01-foundation\` — a NON-LIVE generated attempt. Status ACTIVE while the hosting company is not live was a structural contradiction.

**Resolution (hygiene audit D1, executed 2026-08-18):** the registry's multi-entity model says departments serve multiple legal entities — implying a shared home. Re-homed to the working-companies level:

- Writing → `.\..\01 - writing-department\` (shared-level function folder)
- Content Distribution → `.\..\02 - content-distribution\` (shared-level function folder)
- This registry + COMPANY_DEPENDENCY_GRAPH + content-infrastructure specs → `.\01 - content-infrastructure\` in this directory (shared governance unit; omitted from the rows above because it is not a department)

The audit trail lives in `02 - WORKSPACE_META\02 - audits-and-history\01 - ce-drift-audits\2026-08-18-working-companies-hygiene-audit\00 - REPORT.md`. Media remains split: `lumina-arts\13-media-department` (template origin) + `design-visual-artist-brand\01 - foundation\13-media-department` (operational production).

## Status Definitions

| Status | Meaning | Action |
|---|---|---|
| COMPLETE | Function folder exists, working rules enforced, outputs verified | Maintain and feed downstream departments |
| ACTIVE | Function folder exists, being built out and validated | Continue building, verify outputs |
| OPERATIONAL | Department works but lacks formalized function folder | Prioritize formalization when upstream dependencies complete |
| PLANNED | Not yet started — waiting for upstream departments | Document requirements, wait for dependency chain |

## Dependency Rules

1. A department cannot start until ALL departments it depends on are at least OPERATIONAL.
2. A department cannot be COMPLETE until its outputs are consumed and validated by at least one downstream department.
3. Shared infrastructure (research methodology, distribution architecture) is available to all departments regardless of their position in the chain.

## Multi-Entity Support

All departments serve multiple legally distinct entities:

| Entity | Departments Used | Positioning |
|---|---|---|
| Legal services firm | Law, Writing, Content Distribution | Subject-matter authority |
| Consulting practice | Writing, Content Distribution, Branding | Demonstrable expertise |
| Creative agency / media brand | Media, Design, Branding, Content Distribution | Visual portfolio + process |
| Design studio | Design, Branding, Media | Brand identity systems |

## Update Rule

When a department status changes:
1. Update this file first
2. Update the department's function folder `00 - ENTRY.md`
3. Update `.\..\..\..\..\02 - WORKSPACE_META\06 - human-readable\CANONICAL_PATHS.md` if paths changed
4. Update `.\..\00 - ENTRY.md`

## Cross-References

- Governance rule: `.\..\..\..\..\02 - WORKSPACE_META\03 - folder-governance\RESEARCH_FIRST_CONTENT_PRODUCTION.md`
- Staging pattern: `.\..\..\..\..\02 - WORKSPACE_META\03 - folder-governance\DETERMINISTIC_COGNITIVE_WORKSPACE_STAGING.md`
- Spec provenance: `.\01 - content-infrastructure\07 - department-dependency-model.md`

## Topology Update (2026-09-25, session S001)

By operator directive (`.\..\00-control\source-intent\02 - operator-directives-2026-09-25.md`), Writing, Content Distribution and this governance unit moved into `omnichannel-marketing-company/` in the `projectprima` repository. For this repo only, that reverses the placement chosen in the 2026-08-18 D1 reconciliation above. The Writing and Content Distribution paths in the Registry table still resolve, because the three folders remain siblings.

Status caveat for this repo:
- Media, Law, Design, Branding and Operations have no folder here. Their statuses are CE-workspace claims (`.\EXTERNAL_DEPENDENCY_REGISTER.md` X-04, X-12).
- Dependency Rule 1 cannot be verified here for Writing or Content Distribution, because Media is absent. Their ACTIVE status means built, not exercised: on 2026-09-25 no research folder or distribution draft exists.
- The company's capability ledger (build Phase C) becomes the authority on what this company can deliver (`.\INSTRUCTION_GAP_REGISTER.md` G-C09).
