# 03 - stills

Status: BUILT (session S003, 2026-09-28)

**Purpose:** get every keyframe still the videos need from the image generation factory: one Nano Banana scene prompt per keyframe, sent in one hand-off, and every returned still checked against its shot and the continuity bible.

**Use when:** a task arrives from `02 - shots`.

## Stages (run in order: each stage folder's `00 - ENTRY.md` is its instruction)

| # | Stage folder | One job | Writes |
|---|---|---|---|
| 1 | `01 - prompts/` | One scene prompt per keyframe; hand off to the image factory (H4); hold | `33-stills/stills/<keyframe>.prompt.md`, `33-stills/00-still-index.md` |
| 2 | `02 - check/` | Check every returned still; re-prompt failures | `33-stills/00-still-index.md` (statuses) |
| 3 | `03 - gate/` | Check; carry forward; advance | the `CONTEXT.md` section, `33-stills/gate.md` |
| — | `work/` | Tasks at this node | — |

## Writes (checked by `00 - control/02 - tools/task.py check`)

| File in the task folder | Stage |
|---|---|
| `33-stills/00-still-index.md` | 1 |
| `CONTEXT.md#33-stills` | 3 |
| `33-stills/gate.md` | 3 |

## Passes to

`03 - video-factory/04 - motion`.
