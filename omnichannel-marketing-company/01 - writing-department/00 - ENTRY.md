# Writing Department

Type: function folder — operational department in the sequential deployment model.

## Ancestry

- Parent: `.\..\00 - ENTRY.md`
- Dependency: Media Department (`.\..\lumina-arts\`) — completed, provides visual asset infrastructure
- Governance: `.\..\..\..\..\02 - WORKSPACE_META\03 - folder-governance\RESEARCH_FIRST_CONTENT_PRODUCTION.md`

## Status

ACTIVE — second department in sequential deployment. Media Department completed first; Writing Department builds on its visual production capabilities.

## Working Rules

See `.\WORKING_RULES.md`.

## Output Contract

See `.\OUTPUT_CONTRACT.md`.

## Templates

See `.\02 - templates\` for article structure, research domain, and content decomposition templates.

## Workflow

```
Topic received
  → Research domain check (Gate 8 KSE)
  → If LOW/CRITICAL: Arena research (expansion phase)
  → If SUFFICIENT: Verify research artifacts exist
  → Research expansion (sources → observations → synthesis)
  → Pre-drafting gate (4 checks)
  → Drafting (compression from accumulated research)
  → Quality review (traceability + collapse rules)
  → Output to content-distribution for platform decomposition
```

## Dependency Chain

| Input From | What | How Used |
|---|---|---|
| Media Department | Visual production pipeline | Graphics, carousels, diagrams integrated into articles |
| Media Department | Prompt bank | Content generation prompts derived from visual production patterns |
| Research methodology (Governance Rule 01) | Two-phase workflow | Mandatory research → drafting sequence |

## Output To

| Consumer | What | Format |
|---|---|---|
| Content Distribution | Published articles | Substack long-form + decomposition seeds |
| Content Distribution | Research artifacts | Reusable source collections for future content |
| All departments | Knowledge assets | Published content as organizational authority layer |

## Local Wiring (appended 2026-09-25, session S001)

This department now lives inside `omnichannel-marketing-company/` (operator directive: `.\..\00-control\source-intent\02 - operator-directives-2026-09-25.md`).

- Parent `.\..\00 - ENTRY.md` is the company ENTRY. Company state: `.\..\00-control\STATE.md`.
- Templates: `.\02 - templates\` holds only the research-domain starter. The article skeleton and the decomposition checklist live in `.\..\02 - content-distribution\05 - templates\` (`substack-article-template.md`, `decomposition-checklist.md`).
- The external references above (Media, KSE Gate 8, the RESEARCH_FIRST rule, Arena) are not in this repo. Use the substitutes in `.\..\03 - architecture-governance\EXTERNAL_DEPENDENCY_REGISTER.md`, rows X-01 to X-04.
- Status in this repo: built, **not exercised**. No `research-[slug]/` folder and no author voiceprint exist yet. Open gaps: G-C05, G-C07, G-M02, G-M03, G-X04 in `.\..\03 - architecture-governance\INSTRUCTION_GAP_REGISTER.md`.
