# Media Department Dependency — Writing Department

Type: dependency declaration — documents what the Writing Department consumes from the Media Department and why Media must be COMPLETE before Writing can start.

## Authority

This file is the durable record of the Writing → Media dependency edge. It does not redefine either department. The folder rules files are:

- Writing Department role and rules: `.\00 - ENTRY.md` + `.\WORKING_RULES.md` + `.\OUTPUT_CONTRACT.md`
- Media Department role and rules: `.\..\design-visual-artist-brand\01 - foundation\13-media-department\02 - media-department\00 - ENTRY.md` + `WORKING_RULES.md` + `OUTPUT_CONTRACT.md`
- Cross-entity dependency view: `.\..\03 - architecture-governance\COMPANY_DEPENDENCY_GRAPH.md`
- Department inventory: `.\..\03 - architecture-governance\DEPARTMENT_REGISTRY.md`

## Source intent

Derived from `.\..\..\..\..\99 - ARCHIVE\tech-bro\2026-06-13-lrp6-infrastructure-buildout\infrastructure\08 - build-writing-department.md`. The source declares that Writing is established only after Media's successful completion because Media's outputs, assets, and workflows provide foundational support for Writing operations. This file is the durable record of that dependency.

## Why Media before Writing

The deployment sequence is strict. The Writing Department cannot start until the Media Department is at least OPERATIONAL. Reasons:

| # | Reason | What Writing cannot do without Media |
|---|---|---|
| 1 | Visual asset infrastructure | Every Writing output (newsletter, article, social post) needs accompanying visual assets — custom graphics, visual frameworks, branded content. Media provides the production pipeline for these. |
| 2 | Production workflows | Media's documented `generate-image-prompts` workflows (canonical reference template + active run pattern) are consumed by Writing when decomposing a long-form article into platform-native derivatives. |
| 3 | Prompt-bank patterns | Media contributes visual-content prompt patterns to the prompt bank. Writing reuses these when producing visual companions to research articles. |
| 4 | Asset management infrastructure | Media's asset-intake discipline and indexing patterns are inherited by Writing for tracking the visual assets that accompany written content. |

## What Writing consumes from Media (concrete)

| Consumed artifact | Path | How Writing uses it |
|---|---|---|
| Media Department OUTPUT_CONTRACT | `.\..\design-visual-artist-brand\01 - foundation\13-media-department\02 - media-department\OUTPUT_CONTRACT.md` | Declares the structure of visual assets Writing can request; Writing's OUTPUT_CONTRACT references this for the visual-companion section. |
| Media Department WORKING_RULES | `.\..\design-visual-artist-brand\01 - foundation\13-media-department\02 - media-department\WORKING_RULES.md` | Rule 2 (foundation-for-downstream) governs how Media outputs must be consumable by Writing. |
| Lumina Arts `generate-image-prompts` patterns | `.\..\lumina-arts\13-media-department\` | Production templates, narrative-engine patterns, prompt-bank contributions that Writing reuses. |
| Prompt-bank visual organs | `.\..\..\03 - company-creation-protocol\02 - prompt-bank\01 - organs\19 - nb\` | Visual-content prompts Writing invokes when producing image companions to articles. |

## Diamond model (Writing's core operating philosophy)

The source declares: "The core operating philosophy must be centered on the 'Diamond Model' of content creation, where all writing originates from rigorous bottom-up development rather than top-down drafting."

**Expand phase (research):** systematically uncover every relevant angle, perspective, insight, and informational edge surrounding a topic. This creates the broad foundational base of the diamond.

**Compress phase (drafting):** synthesize, organize, and refine the accumulated research into a coherent, polished final output representing the diamond's apex.

**CE realization:** this is the same diamond model named in `.\..\03 - architecture-governance\01 - content-infrastructure\RESEARCH_METHODOLOGY_REFERENCE.md`. The Writing Department's WORKING_RULES.md Rule 1 (Research Before Drafting) is the mechanical enforcement. The RESEARCH_FIRST_CONTENT_PRODUCTION governance rule's 4-check pre-drafting gate and 5 anti-patterns are the failure-mode detectors.

**Non-negotiable:** research is the primary value-generating activity of the Writing Department. AI is an amplification mechanism, not a replacement for human investigation and judgment. Content generated without deep research lacks structural integrity, substantive insight, and long-term value.

## Compressed implementation window

The source declares: "AI, research systems, and pre-existing departmental frameworks enable the entire department to be designed, deployed, and operationalized within a compressed implementation window of approximately two days."

**Why this is possible:** the Writing Department does not build from scratch. It imports:
- Research-first discipline from `RESEARCH_FIRST_CONTENT_PRODUCTION.md` (governance rule already enforced workspace-wide).
- Diamond-model framing from `RESEARCH_METHODOLOGY_REFERENCE.md` (named concept, pointer document).
- Visual asset infrastructure from Media (already COMPLETE).
- KSE Gate 8 for 6-dimension confidence evaluation before every task (already operational).
- Prompt-bank organs for research, writing, and distribution (already populated).
- WORK_AXIOM_BANK CONTEXT→RULE→OUTCOME format for codifying writing patterns (already populated with 256+ axioms).

The two-day window is the time needed to assemble these pre-existing systems into the Writing Department's own function-folder structure (ENTRY + WORKING_RULES + OUTPUT_CONTRACT + templates + prompt-library) and verify them against a real production run.

## Integration into reverse-engineered infrastructure

The Writing Department is not a standalone operation. It is one function within a reverse-engineered organizational infrastructure:

- **Above:** the WORKSPACE_ORCHESTRATION_CONTRACT (11 sections of codified cognitive infrastructure that every department obeys).
- **Below:** the WORK_AXIOM_BANK (the transfer mechanism from tacit expertise to explicit replicable frameworks).
- **Across:** Media (upstream) + Content Distribution + Law + Design + Branding + Operations (downstream or peer).

The department is designed, deployed, and operationalized as an independent function with its own workflow architecture, quality standards, and production methodology — but it imports the cognitive infrastructure it depends on rather than rebuilding it.

## Verification

The Writing → Media dependency is satisfied when all of the following are true:

| # | Check | How |
|---|---|---|
| 1 | Media Department COMPLETE | `DEPARTMENT_REGISTRY.md` shows Media = COMPLETE |
| 2 | Media OUTPUT_CONTRACT consumable by Writing | Writing's OUTPUT_CONTRACT references Media's for visual-companion sections |
| 3 | Visual prompt patterns indexed | Writing can invoke Media-contributed prompts from the prompt bank without reconstruction |
| 4 | Asset-intake discipline inherited | Writing's visual-companion outputs follow Media's asset-indexing rules |

## Update rule

When the Writing → Media dependency edge changes (Media status changes, new consumed artifacts, new integration points), update this file first, then update `.\00 - ENTRY.md` if the change affects role or status, then update `COMPANY_DEPENDENCY_GRAPH.md` and `DEPARTMENT_REGISTRY.md`.
