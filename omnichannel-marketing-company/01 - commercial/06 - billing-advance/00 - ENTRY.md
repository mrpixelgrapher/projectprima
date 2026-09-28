# 06 - billing-advance

Status: BUILT (session S003, 2026-09-28)

**Purpose:** invoice before the work: on an engagement, the setup plus 50% of the first month; on a month task, 50% of that month. Content work starts only when the operator confirms the payment.

**Use when:** a task arrives from `04 - proposal` (route engagement) or from `05 - month-review` (route month).

## Stages (run in order: each stage folder's `00 - ENTRY.md` is its instruction)

| # | Stage folder | One job | Writes |
|---|---|---|---|
| 1 | `01 - invoice/` | Write the itemised invoice and send it (H1) | `16-billing-advance/01-invoice-for-client.md`; a row in `ledgers/invoices.md` |
| 2 | `02 - payment/` | Hold until the operator confirms payment (H2) | `16-billing-advance/02-payment-for-operator.md` |
| 3 | `03 - gate/` | Check; carry forward; advance | the `CONTEXT.md` section, `16-billing-advance/gate.md` |
| — | `work/` | Tasks at this node | — |

## Writes (checked by `00 - control/02 - tools/task.py check`)

| File in the task folder | Stage |
|---|---|
| `16-billing-advance/01-invoice-for-client.md` | 1 |
| `16-billing-advance/02-payment-for-operator.md` | 2 |
| `CONTEXT.md#16-billing-advance` | 3 |
| `16-billing-advance/gate.md` | 3 |

## Passes to

`02 - content/01 - discovery` (engagement) or `02 - content/03 - performance` (month): the next step of the task's route.
