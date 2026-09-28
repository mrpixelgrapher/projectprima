# 09 - packaging

Status: BUILT (session S003, 2026-09-28)

**Purpose:** join every piece back into the parent task, and assemble one client package. It holds a paste-ready publish kit per piece (every channel in the plan, in publishing order), a dated schedule, and a plain-language index telling the client exactly what to do.

**Use when:** the parent arrives here from `04 - planning` (status WAITING-CHILDREN); children arrive from `08 - shaping`. **Join node:** the parent's work starts only when every child has arrived.

## Stages (run in order: each stage folder's `00 - ENTRY.md` is its instruction)

| # | Stage folder | One job | Writes |
|---|---|---|---|
| 1 | `01 - join/` | Absorb every child into the parent; report what each piece contains | `09-packaging/01-join-report.md` |
| 2 | `02 - kit/` | Build the paste-ready PUBLISH_KIT, per piece and per channel, with partial-publication logs | `09-packaging/PUBLISH_KIT/…`, `09-packaging/02-kit-index.md` |
| 3 | `03 - schedule/` | Lay every piece's 30-day deployment on one calendar | `09-packaging/03-schedule.md` |
| 4 | `04 - package/` | Write the client-facing index: what's inside, how to publish, what's waiting, what to send back | `09-packaging/00-package.md` |
| 5 | `05 - gate/` | Check completeness; carry forward; float | the `CONTEXT.md` section, `09-packaging/gate.md` |
| — | `work/` | The parent and the arriving children | — |

## Writes (checked by `00 - control/02 - tools/task.py check`)

| File in the task folder | Stage |
|---|---|
| `09-packaging/01-join-report.md` | 1 |
| `09-packaging/02-kit-index.md` | 2 |
| `09-packaging/03-schedule.md` | 3 |
| `09-packaging/00-package.md` | 4 |
| `CONTEXT.md#09 - packaging` | 5 |
| `09-packaging/gate.md` | 5 |

## Passes to

`10 - delivery`, as one parent task that holds everything.

## Past material merged here

| From (now in `99 - archive/2026-09-28-restructure/`) | Became |
|---|---|
| `00 - control/01 - law/OMNICHANNEL_ENFORCEMENT.md` (still live): Rule 1 fan-out, Rule 3 kit completeness, Rule 4 partial publication | The kit layout, completeness states and `partial_publication.yaml` in `02 - kit/` |
| `02 - content-distribution/CHANNEL_ACTIVATION.md` (the partial-publication format; the kit location) | The same, in `02 - kit/` |
| `02 - content-distribution/WORKING_RULES.md` Rule 4, `MULTI_PLATFORM_ARCHITECTURE.md` (30-day framework; no same-day publication) | `03 - schedule/` |
