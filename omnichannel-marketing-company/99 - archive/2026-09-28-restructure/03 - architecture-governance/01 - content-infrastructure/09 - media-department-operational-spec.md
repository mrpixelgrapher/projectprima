# 09 — Media Department Operational Spec

Type: department spec

## Status

COMPLETE — the first department built in the sequential deployment model. Its outputs provide the foundation for the Writing Department and all subsequent departments.

## Core Function

Visual asset production, content creation systems, and media workflows. The department converts creative requests into production-ready outputs through documented, repeatable processes.

## Capability Registry

| Capability | CE Location | Status |
|---|---|---|
| `generate-image-prompts` pipeline | `.\..\..\..\..\..\03 - work-projects\02 - company\04 - domains\02 - nano-banana\`generate-image-prompts`-pipeline\` | OPERATIONAL |
| Narrative engine | `.\..\..\..\..\..\03 - work-projects\02 - company\02 - working-companies\design-visual-artist-brand\01 - foundation\13-media-department\03 - media-production\NARRATIVE_ENGINE\` | OPERATIONAL |
| Prompt bank (image) | `.\..\..\..\..\..\03 - work-projects\02 - company\03 - company-creation-protocol\02 - prompt-bank\01 - organs\19 - nb\` | OPERATIONAL |
| Image creation | Via `generate-image-prompts` pipeline + browser execution layer | OPERATIONAL |

## Outputs That Feed Downstream Departments

| Output | Consumed By | How |
|---|---|---|
| Visual assets (graphics, carousels, diagrams) | Writing Department | Integrated into articles and platform derivatives |
| Production workflows | All departments | Template for repeatable creative processes |
| Prompt bank | Writing Department | Content generation prompts derived from `generate-image-prompts` patterns |
| Narrative engine | All content production | Sequential processing stages for content derivation |
| Brand consistency framework | Design, Branding | Visual identity rules and consistency anchors |

## Quality Standards

- Every visual output has a named consistency anchor
- Production follows canonical reference template (v1 → v2 active run pattern)
- Prompt quality governed by PROMPT_ENGINEERING_CANON.md
- Browser execution layer produces verifiable outputs (image files with metadata)

## Validation

The Media Department's completion validates the sequential deployment model:
- Department was built in isolation (no prior department existed)
- Its outputs are now consumed by other work in progress
- The pattern (reverse-engineer → document → deploy → validate) is proven
