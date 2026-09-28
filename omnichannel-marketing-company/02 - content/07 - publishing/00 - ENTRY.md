# 07 - publishing

Status: BUILT (session S003, 2026-09-28)

**Purpose:** when the engagement includes publishing, get every post of the month scheduled on the client's accounts exactly as the kit and schedule say, and log every live link. The node prepares the run; the operator (who holds the account access) carries it out.

**Use when:** a task arrives from `06 - packaging` and its `includes` lists `publishing`. Otherwise the route passes over this node.

## Stages (run in order: each stage folder's `00 - ENTRY.md` is its instruction)

| # | Stage folder | One job | Writes |
|---|---|---|---|
| 1 | `01 - run-sheet/` | A run sheet the operator follows to schedule every post (H2); hold | `27-publishing/01-run-sheet-for-operator.md` |
| 2 | `02 - log/` | Log every scheduled post, and each live link as it goes up | `27-publishing/02-publish-log.md` |
| 3 | `03 - gate/` | Check every post is scheduled; carry forward; advance | the `CONTEXT.md` section, `27-publishing/gate.md` |
| — | `work/` | Tasks at this node | — |

## Writes (checked by `00 - control/02 - tools/task.py check`)

| File in the task folder | Stage |
|---|---|
| `27-publishing/01-run-sheet-for-operator.md` | 1 |
| `27-publishing/02-publish-log.md` | 2 |
| `CONTEXT.md#27-publishing` | 3 |
| `27-publishing/gate.md` | 3 |

## Passes to

`02 - content/08 - delivery`. Posts go live through the month; live links still arriving are collected by `01 - commercial/05 - month-review/`.
