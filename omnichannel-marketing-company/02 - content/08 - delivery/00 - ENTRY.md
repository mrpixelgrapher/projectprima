# 08 - delivery

Status: BUILT (session S003, 2026-09-28; v2 after the design lock)

**Purpose:** hand the month's package to the client, record what actually happened (what shipped, how long each node took, what came back), fix how results will be read (retainers), and turn every hold, return and correction into a specific fix to the instructions.

**Use when:** a task arrives from `06 - packaging` or `07 - publishing`.

## Stages (run in order: each stage folder's `00 - ENTRY.md` is its instruction)

| # | Stage folder | One job | Writes |
|---|---|---|---|
| 1 | `01 - handover/` | Send the package with a short delivery note (H1); log the client's receipt | `28-delivery/01-delivery-note-for-client.md` |
| 2 | `02 - record/` | What shipped, the time per node, the client's response; append the delivery ledger | `28-delivery/02-record.md` |
| 3 | `03 - results-plan/` | Retainer: when and which numbers come back. One-off: none | `28-delivery/03-results-plan.md` |
| 4 | `04 - lessons/` | One lesson per hold, return and correction, each naming the file to fix | `28-delivery/04-lessons.md` |
| 5 | `05 - gate/` | Check; carry forward; advance to the delivery invoice | the `CONTEXT.md` section, `28-delivery/gate.md` |
| — | `work/` | Tasks being delivered | — |
| — | `ledgers/` | The delivery ledger and the lessons log (see its ENTRY) | — |

## Writes (checked by `00 - control/02 - tools/task.py check`)

| File in the task folder | Stage |
|---|---|
| `28-delivery/01-delivery-note-for-client.md` | 1 |
| `28-delivery/02-record.md` | 2 |
| `28-delivery/03-results-plan.md` | 3 |
| `28-delivery/04-lessons.md` | 4 |
| `CONTEXT.md#28-delivery` | 5 |
| `28-delivery/gate.md` | 5 |

## Passes to

`01 - commercial/07 - billing-delivery`, which invoices the second half and closes the task. On the direct route (no commercials) there is no billing: this node's gate closes the task.

## Past material merged here

| From | Became |
|---|---|
| `00 - control/04 - source-intent/01 - CLOUD_AI_HANDOFF.md` §2.6 (every delivered matter emits a lesson) | `04 - lessons/` |
| `00 - control/03 - state/meta_workspace.md` §5 (promote a pattern after 2+ instances) | The promotion rule in `04 - lessons/` |
| Pipeline v1 `99 - archive/2026-09-28-pipeline-v1/10 - delivery/02 - record/` (the free proof run and its disposition) | Removed by the design lock: pricing and offers belong to `01 - commercial` |
