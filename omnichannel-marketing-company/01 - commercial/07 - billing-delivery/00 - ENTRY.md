# 07 - billing-delivery

Status: BUILT (session S003, 2026-09-28)

**Purpose:** close a task: invoice the other 50% on delivery, record the task in the client's history and the ledgers, and, for a continuing retainer, open next month's task. It is the last node of every route.

**Use when:** a task arrives from `02 - content/08 - delivery`.

## Stages (run in order: each stage folder's `00 - ENTRY.md` is its instruction)

| # | Stage folder | One job | Writes |
|---|---|---|---|
| 1 | `01 - invoice/` | Write the delivery invoice and send it (H1) | `17-billing-delivery/01-invoice-for-client.md`; a row in `ledgers/invoices.md` |
| 2 | `02 - close/` | Record the task in the client's history; open next month's task for a continuing retainer | `17-billing-delivery/02-close.md` |
| 3 | `03 - gate/` | Check; carry forward; advance (the task is filed in `clients/<client>/done/`) | the `CONTEXT.md` section, `17-billing-delivery/gate.md` |
| — | `work/` | Tasks at this node | — |

## Writes (checked by `00 - control/02 - tools/task.py check`)

| File in the task folder | Stage |
|---|---|
| `17-billing-delivery/01-invoice-for-client.md` | 1 |
| `17-billing-delivery/02-close.md` | 2 |
| `CONTEXT.md#17-billing-delivery` | 3 |
| `17-billing-delivery/gate.md` | 3 |

## Passes to

`clients/<client>/done/`. The task is finished.
