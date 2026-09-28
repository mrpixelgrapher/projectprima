# 04 - proposal

Status: BUILT (session S003, 2026-09-28)

**Purpose:** package the priced scope into an offer the client can say yes to: a retainer (or a one-off) with fixed deliverables and add-ons. The operator signs it off, the client accepts it, and the accepted version becomes the client's engagement. Content work is bound by it.

**Use when:** a task arrives from `03 - pricing`.

## Stages (run in order: each stage folder's `00 - ENTRY.md` is its instruction)

| # | Stage folder | One job | Writes |
|---|---|---|---|
| 1 | `01 - package/` | Choose the offer: type, base package that fits the budget, add-ons, includes | `14-proposal/01-package.md` |
| 2 | `02 - document/` | Write the client-facing proposal | `14-proposal/02-proposal-for-client.md` |
| 3 | `03 - sign-off/` | The operator signs off (H2); hold until they do | `14-proposal/03-signoff-for-operator.md` |
| 4 | `04 - acceptance/` | Send to the client (H1); hold; record the outcome | `14-proposal/04-acceptance.md` |
| 5 | `05 - gate/` | Check; publish the engagement; ledgers; advance (or close if declined) | the `CONTEXT.md` section, `14-proposal/gate.md`, `clients/<client>/engagement.md` |
| — | `work/` | Tasks at this node | — |

## Writes (checked by `00 - control/02 - tools/task.py check`)

| File in the task folder | Stage |
|---|---|
| `14-proposal/01-package.md` | 1 |
| `14-proposal/02-proposal-for-client.md` | 2 |
| `14-proposal/03-signoff-for-operator.md` | 3 |
| `14-proposal/04-acceptance.md` | 4 |
| `CONTEXT.md#14-proposal` | 5 |
| `14-proposal/gate.md` | 5 |

## Passes to

`01 - commercial/06 - billing-advance`. A declined proposal ends the task: `task.py close`.
