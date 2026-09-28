# 08 - shaping

Status: BUILT (session S003, 2026-09-28)

**Purpose:** turn one passed article into everything the channels need: its six seeds, the hub-ready version, one native variant per channel in the plan, a visual brief for every image slot, and a gate for each variant. One source becomes channel-shaped variants, for every channel, every time.

**Use when:** a child task arrives from `07 - review` with a PASS. **Child tasks only.**

## Stages (run in order: each stage folder's `00 - ENTRY.md` is its instruction)

| # | Stage folder | One job | Writes |
|---|---|---|---|
| 1 | `01 - seeds/` | Extract the six decomposition seeds, and assign them to channels | `08-shaping/01-seeds.md` |
| 2 | `02 - hub/` | Make the hub-ready article with its metadata | `08-shaping/02-hub-article.md`, `08-shaping/02-hub-metadata.md` |
| 3 | `03 - channels/` | One native variant per channel in the plan: one subfolder per channel | `08-shaping/03-channels/<channel>.md`, `08-shaping/03-channel-index.md` |
| 4 | `04 - visuals/` | One brief per image slot, with the producer's status | `08-shaping/04-visuals/<channel>-<slot>.md`, `08-shaping/04-visual-index.md` |
| 5 | `05 - gate/` | Gate each variant on its own; carry forward; float | `08-shaping/05-variant-gates.md`, the `CONTEXT.md` section, `08-shaping/gate.md` |
| — | `work/` | Child tasks at this node | — |

## Writes (checked by `00 - control/02 - tools/task.py check`)

| File in the task folder | Stage |
|---|---|
| `08-shaping/01-seeds.md` | 1 |
| `08-shaping/02-hub-article.md` | 2 |
| `08-shaping/02-hub-metadata.md` | 2 |
| `08-shaping/03-channel-index.md` | 3 |
| `08-shaping/04-visual-index.md` | 4 |
| `08-shaping/05-variant-gates.md` | 5 |
| `CONTEXT.md#08 - shaping` | 5 |
| `08-shaping/gate.md` | 5 |

## Passes to

`09 - packaging`, where the parent is waiting.

## Rules every stage here obeys

1. **Translation, not syndication.** Every variant is a new piece in its channel's native register. A copied or lightly reformatted paragraph is a violation.
2. **The hub is the anchor.** Everything links back to the hub; the hub never depends on a spoke.
3. **Seed-based.** Every variant names the seeds it develops. Two channels sharing a seed take different angles on it.
4. **Every variant has an image slot.** With no producer, the slot's brief waits, and the variant is *text-complete*, never *complete*.
5. **Each variant passes its own gate** (`00 - control/01 - law/OMNICHANNEL_ENFORCEMENT.md` Rule 2) and names its own surplus.

## Past material merged here

| From (now in `99 - archive/2026-09-28-restructure/`) | Became |
|---|---|
| `02 - content-distribution/01 - substack-hub/OUTPUT_CONTRACT.md`, `WORKFLOW.md`, `05 - templates/substack-article-template.md` | `02 - hub/`, and `02 - hub/article-template.md` |
| `02 - content-distribution/02 - linkedin-layer/*`, `03 - twitter-threads-layer/*`, `04 - facebook-layer/*`, `05 - templates/linkedin-post-template.md`, `twitter-thread-template.md` | `03 - channels/01 - linkedin/` to `04 - facebook/`, with their templates |
| `03 - architecture-governance/01 - content-infrastructure/03`–`06` (decomposition, platform specs) | Seed rules in `01 - seeds/`; the Instagram and Medium rules in `03 - channels/` |
| `02 - content-distribution/05 - templates/decomposition-checklist.md` (seeds, the per-variant gate) | `01 - seeds/` and `05 - gate/` |
| `04 - media-department/00 - ENTRY.md`, `VISUAL_BRIEF_CONTRACT.md` | `04 - visuals/` |
| `02 - content-distribution/WORKING_RULES.md` Rules 1, 2, 3, 5, 6 | The rules above |
