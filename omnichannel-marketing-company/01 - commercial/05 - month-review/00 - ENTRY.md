# 05 - month-review

Status: BUILT (session S003, 2026-09-28)

**Purpose:** open each retainer month. Collect the results of the month being run, review them against the objectives, check what is still owed, and offer an upsell when the results or the client call for it. The performance node optimises from this review; planning plans the next month from it.

**Use when:** a month task is opened (route `month`), by `07 - billing-delivery/` of the previous task.

## Stages (run in order: each stage folder's `00 - ENTRY.md` is its instruction)

| # | Stage folder | One job | Writes |
|---|---|---|---|
| 1 | `01 - results/` | Ask the client for the month's numbers on the agreed date (H1); hold | `15-month-review/01-results-for-client.md` |
| 2 | `02 - review/` | Log the results; compare them with the objectives; check the engagement and open invoices | `15-month-review/02-review.md` |
| 3 | `03 - upsell/` | Offer an add-on when a trigger fires, or record why not | `15-month-review/03-upsell.md` |
| 4 | `04 - gate/` | Check; carry forward; publish results (and the engagement, if an upsell was accepted); advance | the `CONTEXT.md` section, `15-month-review/gate.md`, `clients/<client>/results.md` |
| — | `work/` | Tasks at this node | — |

## Writes (checked by `00 - control/02 - tools/task.py check`)

| File in the task folder | Stage |
|---|---|
| `15-month-review/01-results-for-client.md` | 1 |
| `15-month-review/02-review.md` | 2 |
| `15-month-review/03-upsell.md` | 3 |
| `CONTEXT.md#15-month-review` | 4 |
| `15-month-review/gate.md` | 4 |

## Passes to

`01 - commercial/06 - billing-advance`.
