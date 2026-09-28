# 06 - packaging

Status: BUILT (session S003, 2026-09-28; v2 after the design lock)

**Purpose:** assemble the month into one client package: a paste-ready kit with one folder per channel (every post, final text, its image, its date and its tagged link), the schedule, and a plain-language page that tells the client exactly what to do.

**Use when:** a task arrives from `05 - writing`, or from `03 - video-factory/05 - edit-plan` when the engagement includes video.

## Stages (run in order: each stage folder's `00 - ENTRY.md` is its instruction)

| # | Stage folder | One job | Writes |
|---|---|---|---|
| 1 | `01 - kit/` | The paste-ready kit, one folder per channel, in publishing order | `26-packaging/kit/…`, `26-packaging/01-kit-index.md` |
| 2 | `02 - schedule/` | The calendar turned into a posting schedule that points at each kit file | `26-packaging/02-schedule.md` |
| 3 | `03 - package/` | The client's first page: what's inside, how to post, what's waiting, what to send back | `26-packaging/03-package.md` |
| 4 | `04 - gate/` | Check completeness; carry forward; advance | the `CONTEXT.md` section, `26-packaging/gate.md` |
| — | `work/` | Tasks at this node | — |

## Writes (checked by `00 - control/02 - tools/task.py check`)

| File in the task folder | Stage |
|---|---|
| `26-packaging/01-kit-index.md` | 1 |
| `26-packaging/02-schedule.md` | 2 |
| `26-packaging/03-package.md` | 3 |
| `CONTEXT.md#26-packaging` | 4 |
| `26-packaging/gate.md` | 4 |

## Passes to

`02 - content/07 - publishing` when the engagement includes publishing; otherwise `02 - content/08 - delivery`.

## Past material merged here

| From | Became |
|---|---|
| `00 - control/01 - law/OMNICHANNEL_ENFORCEMENT.md` (still live): Rule 1 fan-out, Rule 3 kit completeness, Rule 4 partial publication | The kit layout, completeness states and `partial_publication.yaml` in `01 - kit/` |
| `99 - archive/2026-09-28-restructure/02 - content-distribution/CHANNEL_ACTIVATION.md` (partial-publication format; kit location) | The same, in `01 - kit/` |
| `99 - archive/2026-09-28-restructure/02 - content-distribution/WORKING_RULES.md` Rule 4, `MULTI_PLATFORM_ARCHITECTURE.md` (30-day deployment; no same-day publication) | Now dated at planning (`02 - content/04 - planning/02 - calendar/`); `02 - schedule/` checks and points it at the kit |
| The operator's "per channel folder" (design lock) | The kit's one-folder-per-channel layout |
