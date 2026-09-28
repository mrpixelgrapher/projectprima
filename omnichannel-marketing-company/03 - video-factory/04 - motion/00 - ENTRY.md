# 04 - motion

Status: BUILT (session S003, 2026-09-28)

**Purpose:** get the motion between the stills: one cinematic prompt per transition (from a start still to an end still), which the operator runs in an image-to-video tool, and every returned clip checked against its shot.

**Use when:** a task arrives from `03 - stills`.

## Stages (run in order: each stage folder's `00 - ENTRY.md` is its instruction)

| # | Stage folder | One job | Writes |
|---|---|---|---|
| 1 | `01 - prompts/` | One motion prompt per transition; hand off (H5); hold | `34-motion/motion/<T-id>.prompt.md`, `34-motion/00-motion-index.md` |
| 2 | `02 - check/` | Check every returned clip; re-prompt failures | `34-motion/00-motion-index.md` (statuses) |
| 3 | `03 - gate/` | Check; carry forward; advance | the `CONTEXT.md` section, `34-motion/gate.md` |
| — | `work/` | Tasks at this node | — |

## Writes (checked by `00 - control/02 - tools/task.py check`)

| File in the task folder | Stage |
|---|---|
| `34-motion/00-motion-index.md` | 1 |
| `CONTEXT.md#34-motion` | 3 |
| `34-motion/gate.md` | 3 |

## Passes to

`03 - video-factory/05 - edit-plan`.
