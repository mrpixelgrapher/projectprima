# 10 - delivery

Status: BUILT (session S003, 2026-09-28)

**Purpose:** hand the package to the client, record what actually happened (what shipped, what it cost, how the client responded), turn it into lessons that improve the instructions, and file the task.

**Use when:** a parent task arrives from `09 - packaging`.

## Stages (run in order: each stage folder's `00 - ENTRY.md` is its instruction)

| # | Stage folder | One job | Writes |
|---|---|---|---|
| 1 | `01 - handover/` | Send the package, with a short delivery note | `10-delivery/01-delivery-note.md` (+ `client/receipt.md` when they reply) |
| 2 | `02 - record/` | Record what shipped, the cost, the response and, for a proof run, the disposition; append the ledgers | `10-delivery/02-record.md`; rows in `10 - delivery/ledgers/` |
| 3 | `03 - lessons/` | Lessons per node, and the instruction fixes they imply | `10-delivery/03-lessons.md`; a row in `10 - delivery/ledgers/lessons-log.md` |
| 4 | `04 - close/` | Check; carry forward; file the task in `done/` | the `CONTEXT.md` section, `10-delivery/gate.md` |
| — | `work/` | Tasks being delivered | — |
| — | `done/` | Finished tasks: the complete record of each job | — |
| — | `ledgers/` | Company ledgers, one row per task (see its ENTRY) | — |

## Writes (checked by `00 - control/02 - tools/task.py check`)

| File in the task folder | Stage |
|---|---|
| `10-delivery/01-delivery-note.md` | 1 |
| `10-delivery/02-record.md` | 2 |
| `10-delivery/03-lessons.md` | 3 |
| `CONTEXT.md#10 - delivery` | 4 |
| `10-delivery/gate.md` | 4 |

## Passes to

`10 - delivery/done/`. The task is finished.

## The proof-run rule

Nothing is sold before it has been made, checked and delivered once. So **the first task of any new offer is a free proof run**, and its record carries a disposition. The paid version of that offer opens only after a record says `Disposition: PROVEN`. It is sold as *validated* (delivered once, proof on request), and becomes an established service only after a second delivery reconciles.

## Past material merged here

| From (now in `99 - archive/2026-09-28-restructure/`) | Became |
|---|---|
| `01-foundation/offer.md` (the free proof run; the proof-file contents; validated vs live) | The proof-run rule above, and the record in `02 - record/` |
| `00-control/source-intent/01 - CLOUD_AI_HANDOFF.md` §2.6 (every delivered matter emits a lesson and a proof disposition) and §2.5 (capability promotion) | `02 - record/`, `03 - lessons/` |
| `meta_workspace.md` §5 (promote a pattern after 2+ instances) | The promotion rule in `03 - lessons/` |
