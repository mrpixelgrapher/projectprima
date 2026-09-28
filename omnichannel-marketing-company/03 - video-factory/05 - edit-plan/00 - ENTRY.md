# 05 - edit-plan

Status: BUILT (session S003, 2026-09-28)

**Purpose:** write the edit decision list for each video, so the operator or the client's team can assemble the final cut without deciding anything: clip order and timings, voice-over, on-screen text, music and sound, captions, and export settings per platform.

**Use when:** a task arrives from `04 - motion`.

## Stages (run in order: each stage folder's `00 - ENTRY.md` is its instruction)

| # | Stage folder | One job | Writes |
|---|---|---|---|
| 1 | `01 - edit-plan/` | The edit decision list per video | `35-edit-plan/<V-id>-edit-plan.md`, `35-edit-plan/00-edit-index.md` |
| 2 | `02 - gate/` | Check; carry forward; advance | the `CONTEXT.md` section, `35-edit-plan/gate.md` |
| — | `work/` | Tasks at this node | — |

## Writes (checked by `00 - control/02 - tools/task.py check`)

| File in the task folder | Stage |
|---|---|
| `35-edit-plan/00-edit-index.md` | 1 |
| `CONTEXT.md#35-edit-plan` | 2 |
| `35-edit-plan/gate.md` | 2 |

## Passes to

`02 - content/06 - packaging`, which puts each video's edit plan and clips in the kit.
