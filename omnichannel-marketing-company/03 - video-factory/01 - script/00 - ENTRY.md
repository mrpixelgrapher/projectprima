# 01 - script

Status: BUILT (session S003, 2026-09-28)

**Purpose:** refine each video's script and storyboard from writing into a shooting script: every beat timed, every line said in the client's voice, every frame something a camera (or an image model) can show.

**Use when:** a task arrives from `02 - content/05 - writing` with `includes` listing `video`.

## Stages (run in order: each stage folder's `00 - ENTRY.md` is its instruction)

| # | Stage folder | One job | Writes |
|---|---|---|---|
| 1 | `01 - refine/` | Refine each script into a shooting script | `31-script/<V-id>-shooting-script.md`, `31-script/00-video-index.md` |
| 2 | `02 - gate/` | Check; carry forward; advance | the `CONTEXT.md` section, `31-script/gate.md` |
| — | `work/` | Tasks at this node | — |

## Writes (checked by `00 - control/02 - tools/task.py check`)

| File in the task folder | Stage |
|---|---|
| `31-script/00-video-index.md` | 1 |
| `CONTEXT.md#31-script` | 2 |
| `31-script/gate.md` | 2 |

## Passes to

`03 - video-factory/02 - shots`.
