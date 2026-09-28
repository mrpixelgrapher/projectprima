# 03 · Gate and branch

**Purpose:** confirm the plan and briefs are complete, then split the task: one child per piece starts at research, and the parent parks at packaging to wait for them.

## Contract

- **Reads:** `04-planning/01-content-plan.md`, `02-brief-index.md`, `briefs/*.md`.
- **Writes:** the `## 04 - planning` section of `CONTEXT.md`; `04-planning/gate.md`. Then the operator creates the child tasks and moves the parent.
- **Done when:** the children exist in `05 - research/work/`, and the parent is in `09 - packaging/work/` with status WAITING-CHILDREN.

## Procedure

1. **Run the checks in order.** Stop at the first failure.

   | # | Check | On failure |
   |---|---|---|
   | N1 | The piece count follows the package table; every piece is one question for one buyer at one stage | stage 1 |
   | N2 | Internal links follow the first-piece rule; start weeks are staggered by ≥ 1 week | stage 1 |
   | N3 | Every plan row has a brief, and every brief has every template section filled | stage 2 |
   | N4 | Each brief copies the buyer profile, pillar and voiceprint verbatim | stage 2 |

2. **Write the carry-forward** (at most 10 bullets, each with its source):

       ## 04 - planning
       - Pieces: N in cluster "<name>": <slug> (cornerstone), <slug>, … [04-planning/01-content-plan.md]
       - Channels for every piece: … [03-strategy/03-channel-plan.md]
       - Order: <slug> wk1 · <slug> wk2 · … [04-planning/01-content-plan.md]
       - Children: T-…<slug>, … start at 05 - research [04-planning/02-brief-index.md]

3. **Write `gate.md`** (the five-line format in `00 - control/01 - law/TASK_CONTRACT.md` §2), with `VERDICT: PASS` and `Waiting on: —`.
4. **Branch and park,** listing the slugs in plan order:

       python3 "00 - control/02 - tools/task.py" branch <task-id> --start "05 - research" --join "09 - packaging" --children <slug-1> <slug-2> …

5. **Check** with `python3 "00 - control/02 - tools/task.py" status`: the children are at 05, and the parent is at 09 (WAITING-CHILDREN).

## Self-check

- [ ] Does every child have its brief as `00-brief.md`?
- [ ] Is the parent parked at 09 and nowhere else?

## Traps

- **Advancing the parent to 05.** Use `branch --join`, not `advance`. The parent does no piece work.
- **Branching before the briefs are final.** Children copy the brief at birth; later edits don't reach them.
