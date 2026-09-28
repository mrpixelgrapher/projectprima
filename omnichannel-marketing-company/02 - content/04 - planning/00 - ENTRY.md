# 04 - planning

Status: BUILT (session S003, 2026-09-28; v2 after the design lock)

**Purpose:** plan the next month. Choose the topics and the pieces (angles on one topic that all lead to the destination, plus standalone pieces), give each piece its job in the performance design, lay every channel's posts on a dated calendar, and write one brief per piece. The client approves the plan and calendar before writing starts.

**Use when:** a task arrives from `03 - performance` (both routes). On a month route, planning always refers to last month and plans the month after the current one.

## Stages (run in order: each stage folder's `00 - ENTRY.md` is its instruction)

| # | Stage folder | One job | Writes |
|---|---|---|---|
| 1 | `01 - month-plan/` | The month's topics and pieces, each a question with a performance job | `24-planning/01-month-plan.md` |
| 2 | `02 - calendar/` | Every post on every channel, dated, with its test variant and tagged link | `24-planning/02-calendar.md` |
| 3 | `03 - briefs/` | One self-contained brief per piece | `24-planning/briefs/<piece>.md`, `24-planning/03-brief-index.md` |
| 4 | `04 - approval/` | The plan and calendar for the client (H1); hold; apply the reply | `24-planning/04-plan-for-client.md`, `24-planning/05-approval.md` |
| 5 | `05 - gate/` | Check; carry forward; advance | the `CONTEXT.md` section, `24-planning/gate.md` |
| — | `work/` | Tasks at this node | — |

## Writes (checked by `00 - control/02 - tools/task.py check`)

| File in the task folder | Stage |
|---|---|
| `24-planning/01-month-plan.md` | 1 |
| `24-planning/02-calendar.md` | 2 |
| `24-planning/03-brief-index.md` | 3 |
| `24-planning/04-plan-for-client.md` | 4 |
| `24-planning/05-approval.md` | 4 |
| `CONTEXT.md#24-planning` | 5 |
| `24-planning/gate.md` | 5 |

## Passes to

`02 - content/05 - writing`, with an approved plan, a dated calendar and one brief per piece.

## Past material merged here

| From | Became |
|---|---|
| `99 - archive/2026-09-28-restructure/01 - writing-department/BLOG_AS_KNOWLEDGE_PRODUCTION.md` (planning ≠ creation; every piece is earned by research) | The "a piece is a question, not an outline" rule in `01 - month-plan/` |
| `99 - archive/2026-09-28-restructure/02 - content-distribution/01 - substack-hub/WORKFLOW.md` (topic clusters, cluster index, internal links, the first-piece exemption) | The topic and link rules in `01 - month-plan/` |
| `99 - archive/2026-09-28-restructure/02 - content-distribution/WORKING_RULES.md` Rule 4 (the 30-day deployment of one piece) | The per-piece deployment in `02 - calendar/` |
| `99 - archive/2026-09-28-restructure/01 - writing-department/OUTPUT_CONTRACT.md` §3 (the six decomposition seeds) | The "seeds this piece must yield" field in the brief |
| Pipeline v1 `99 - archive/2026-09-28-pipeline-v1/04 - planning/03 - gate-and-branch/` (one child task per piece) | Superseded by the design lock: one task per request; all pieces are written inside the one task |
