# 02 - scope

Status: BUILT (session S003, 2026-09-28)

**Purpose:** turn what intake learned into a fixed list of deliverables, and break every deliverable into sub-tasks that each have one kind of work and an effort in hours. Pricing prices exactly these sub-tasks, and the proposal promises exactly these deliverables, so nothing is priced or promised that isn't here.

**Use when:** a task arrives from `01 - intake`.

## Stages (run in order: each stage folder's `00 - ENTRY.md` is its instruction)

| # | Stage folder | One job | Writes |
|---|---|---|---|
| 1 | `01 - deliverables/` | List every deliverable: setup items once, monthly items per month, and add-on candidates | `12-scope/01-deliverables.md` |
| 2 | `02 - breakdown/` | Break each deliverable into sub-tasks with a kind of work and an effort, from the effort table | `12-scope/02-breakdown.md` |
| 3 | `03 - gate/` | Check; carry forward; advance | the `CONTEXT.md` section, `12-scope/gate.md` |
| — | `work/` | Tasks at this node | — |

## Writes (checked by `00 - control/02 - tools/task.py check`)

| File in the task folder | Stage |
|---|---|
| `12-scope/01-deliverables.md` | 1 |
| `12-scope/02-breakdown.md` | 2 |
| `CONTEXT.md#12-scope` | 3 |
| `12-scope/gate.md` | 3 |

## Passes to

`01 - commercial/03 - pricing`.
