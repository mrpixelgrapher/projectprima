# 03 - pricing

Status: BUILT (session S003, 2026-09-28)

**Purpose:** price every sub-task in the scope: effort × the client's rate for that kind of work, plus pass-through costs, in the client's currency and tax treatment. There is no price book; the price is the work.

**Use when:** a task arrives from `02 - scope`.

## Stages (run in order: each stage folder's `00 - ENTRY.md` is its instruction)

| # | Stage folder | One job | Writes |
|---|---|---|---|
| 1 | `01 - rates/` | Get the client's rate per kind of work, currency, tax treatment and cost figures from the operator (or reuse the client's) | `13-pricing/01-rates.md` |
| 2 | `02 - costs/` | Add the pass-through costs per deliverable | `13-pricing/02-costs.md` |
| 3 | `03 - lines/` | Compute every priced line and the totals: setup, monthly base, each add-on | `13-pricing/03-lines.md` |
| 4 | `04 - gate/` | Check; carry forward; publish the rates; advance | the `CONTEXT.md` section, `13-pricing/gate.md`, `clients/<client>/rates.md` |
| — | `work/` | Tasks at this node | — |

## Writes (checked by `00 - control/02 - tools/task.py check`)

| File in the task folder | Stage |
|---|---|
| `13-pricing/01-rates.md` | 1 |
| `13-pricing/02-costs.md` | 2 |
| `13-pricing/03-lines.md` | 3 |
| `CONTEXT.md#13-pricing` | 4 |
| `13-pricing/gate.md` | 4 |

## Passes to

`01 - commercial/04 - proposal`.
