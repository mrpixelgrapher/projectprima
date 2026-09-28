# 04 - planning

Status: BUILT (session S003, 2026-09-28)

**Purpose:** turn the approved strategy into a list of pieces, write one self-contained brief per piece, and branch. Each piece becomes a child task that travels `05 → 08` on its own, while the parent waits at `09 - packaging`.

**Use when:** a task arrives from `03 - strategy`. **Branch node:** this is where one task becomes many.

## Stages (run in order: each stage folder's `00 - ENTRY.md` is its instruction)

| # | Stage folder | One job | Writes |
|---|---|---|---|
| 1 | `01 - content-plan/` | Decide the pieces: how many, which pillar, which buyer and stage, which question each one answers, the order | `04-planning/01-content-plan.md` |
| 2 | `02 - briefs/` | Write one brief per piece that a child task can work from cold | `04-planning/briefs/<piece-slug>.md`, `04-planning/02-brief-index.md` |
| 3 | `03 - gate-and-branch/` | Check the work, write the carry-forward, branch the children, park the parent | the `CONTEXT.md` section, `04-planning/gate.md` |
| — | `work/` | Tasks at this node | — |

## Writes (checked by `00 - control/02 - tools/task.py check`)

| File in the task folder | Stage |
|---|---|
| `04-planning/01-content-plan.md` | 1 |
| `04-planning/02-brief-index.md` | 2 |
| `CONTEXT.md#04 - planning` | 3 |
| `04-planning/gate.md` | 3 |

The operator's `branch` command checks separately that a brief exists for every child.

## Passes to

The children go to `05 - research`; the parent goes to `09 - packaging` (status WAITING-CHILDREN). One command does both: see stage 3.

## Past material merged here

| From (now in `99 - archive/2026-09-28-restructure/`) | Became |
|---|---|
| `01 - writing-department/BLOG_AS_KNOWLEDGE_PRODUCTION.md` (planning ≠ creation; every piece is earned by research; the archive compounds) | The "a piece is a question, not an outline" rule in `01 - content-plan/` |
| `02 - content-distribution/01 - substack-hub/WORKFLOW.md` (topic clusters, cluster index, internal links, the first-piece exemption) | The cluster and link rules in `01 - content-plan/` and in the brief |
| `02 - content-distribution/WORKING_RULES.md` Rule 4 (the 30-day deployment of one piece) | The start-week and stagger rules in `01 - content-plan/` |
| `01 - writing-department/OUTPUT_CONTRACT.md` §3 (the six decomposition seeds) | The "seeds this piece must yield" field in the brief |
| `03 - architecture-governance/01 - content-infrastructure/15 - department-first-business-model.md` (self-contained playbooks; request outputs by name) | The self-contained brief |
