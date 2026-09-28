# 02 - shots

Status: BUILT (session S003, 2026-09-28)

**Purpose:** design every shot of every video so precisely that an image model can render its keyframes and a motion model can move between them: what is in the frame, how it is framed and lit, how the camera moves, how the shot hands over to the next (a cut, a match cut, a morph, stop-motion), and one continuity bible that keeps the same product, person and look across all shots.

**Use when:** a task arrives from `01 - script`.

## Stages (run in order: each stage folder's `00 - ENTRY.md` is its instruction)

| # | Stage folder | One job | Writes |
|---|---|---|---|
| 1 | `01 - shot-list/` | Every frame of every shooting script becomes one or more fully described shots | `32-shots/<V-id>-shot-list.md` |
| 2 | `02 - continuity/` | The continuity bible: what must look the same across shots, and which stills are keyframes | `32-shots/01-continuity.md` |
| 3 | `03 - gate/` | Check; carry forward; advance | the `CONTEXT.md` section, `32-shots/gate.md` |
| — | `work/` | Tasks at this node | — |

## Writes (checked by `00 - control/02 - tools/task.py check`)

| File in the task folder | Stage |
|---|---|
| `32-shots/01-continuity.md` | 2 |
| `CONTEXT.md#32-shots` | 3 |
| `32-shots/gate.md` | 3 |

## Passes to

`03 - video-factory/03 - stills`.
