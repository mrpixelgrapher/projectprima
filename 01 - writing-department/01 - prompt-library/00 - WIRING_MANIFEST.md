# Prompt Library — Wiring Manifest

**Installed:** 2026-06-14
**Source:** `05 - INPUT/01 - intake/01 - gaps/06 - mission-blueprint/07 - WRITING_ENGINE/`
**Authority:** Carbon's writing method, transmitted via EXTERNAL_ENTITY S211

## What This Is

Five executable stage-prompts that run the diamond methodology for content production. Each prompt IS the tool that executes one stage of the writing department's workflow. The department's `OUTPUT_CONTRACT.md` describes WHAT each stage must produce; these prompts are HOW to produce it.

## Stage → Workflow → Output Contract Mapping

| # | Prompt File | Workflow Stage | OUTPUT_CONTRACT Artifact | Gate |
|---|-------------|---------------|--------------------------|------|
| 01 | `01 - PROMPT_boundary_research.md` | Research expansion | `research-[slug]/sources/` + `observations/` | Gate 3 (depth: 3+ source categories) |
| 02 | `02 - PROMPT_synthesis_middle.md` | Synthesis | `research-[slug]/synthesis/` | Gate 2 (originality: 1+ insight not in any source) |
| 03 | `03 - PROMPT_draft_apex.md` | Drafting | `research-[slug]/outputs/DRAFT.md` | Gate 4 (structure) + Gate 5 (SEO) |
| 04 | `04 - PROMPT_voice_humanization.md` | Quality review | `research-[slug]/outputs/ARTICLE.md` | Gate 6 (collapse: no speculative content) |
| 05 | `05 - PROMPT_perfection_gate.md` | Pre-publish gate | PASS/FAIL verdict | All 6 gates checked |

## Execution Chain

```
INPUT: topic + author name (+ 3-5 writing samples for voiceprint)
  │
  ├─[01 BOUNDARY]  → sources/ + observations/     (draws the full edge)
  │
  ├─[02 SYNTHESIS] → synthesis/SPINE.md           (the MIDDLE — where value is MADE)
  │
  ├─[03 DRAFT]     → outputs/DRAFT.md             (written FROM the spine, never cold)
  │
  ├─[04 VOICE]     → outputs/ARTICLE.md           (humanization toward named author)
  │
  └─[05 GATE]      → PASS → publish kit
                     FAIL → named defect → back to failing stage
```

Each arrow is a file handoff that lands in the `research-[slug]/` structure the OUTPUT_CONTRACT already declares.

## Voiceprint Requirement

Stage 04 (`04 - PROMPT_voice_humanization.md`) requires an **author voiceprint** as hard input. This is 3-5 samples of the author's real writing used to calibrate humanization. No piece humanizes toward "human in general" — only toward a specific named author.

**Create `voiceprints/` folder** when the first production run occurs. Store the author's writing samples there. The voiceprint is load-bearing — without it, Stage 04 produces detectable AI slop.

## Perfection Gate Binding

Stage 05 (`05 - PROMPT_perfection_gate.md`) IS the department's quality review step. It checks:
1. Traceability (every claim → research artifact)
2. Originality (at least 1 unique insight)
3. Depth (3+ source categories)
4. Structure (subheadings, links, graphics)
5. SEO (keyword placement)
6. Collapse (no unsupported claims)

This gate is **enforced, not advisory.** A FAIL verdict names the specific defect and routes back to the failing stage. Do not publish on a FAIL.

## Relationship to Existing Governance

| Document | Role | This Library's Role |
|----------|------|---------------------|
| `OUTPUT_CONTRACT.md` | WHAT must exist | Prompts produce those artifacts |
| `WORKING_RULES.md` | HOW the department operates | Prompts execute within those rules |
| `00 - ENTRY.md` | Department workflow (stages named, no executors) | This library provides the executors |
| `templates/` | Article structure templates | Prompts consume these templates during drafting |
| Source MANIFEST (`06 - mission-blueprint/07 - WRITING_ENGINE/00 - MANIFEST.md`) | Install instructions + cognitive-build reasoning | This file is the installed wiring; source remains as lineage |

## First Production Run

To execute the first piece through this engine:

1. Choose a topic from the content calendar or Carbon direction
2. Create `research-[topic-slug]/` with the 4-subfolder structure
3. Run Stage 01 with the topic → fills `sources/` + `observations/`
4. Run Stage 02 → fills `synthesis/SPINE.md`
5. Run Stage 03 → fills `outputs/DRAFT.md`
6. Provide voiceprint (3-5 author writing samples)
7. Run Stage 04 → fills `outputs/ARTICLE.md`
8. Run Stage 05 → PASS or named FAIL
9. On PASS: decompose to content-distribution for platform variants
