# 05 · Gate

**Purpose:** confirm the month is planned, approved and complete, carry it forward, and send the task to writing.

## Contract

- **Reads:** `24-planning/*.md`, `24-planning/briefs/*.md`.
- **Writes:** the `## 24-planning` section of `CONTEXT.md`; `24-planning/gate.md`.
- **Done when:** the task has advanced to writing.

## Procedure

1. **Run the checks in order.** Stop at the first failure.

   | # | Check | On failure |
   |---|---|---|
   | N1 | The piece count equals the engagement's; ≥ half are funnel angles; the four path stages are covered; every piece is one question with a CTA to the destination | 01 - month-plan |
   | N2 | Every channel's post count equals its engagement quantity; every post is dated, timed and tagged; test variants are balanced | 02 - calendar |
   | N3 | Every piece has a brief with every section filled; buyer, pillar, voice and performance rules are copied verbatim | 03 - briefs |
   | N4 | `05-approval.md` records the client's approval, with changes applied | 04 - approval |

2. **Write the carry-forward** (at most 10 bullets, each with its source):

       ## 24-planning
       - Month: … · topics: … [24-planning/01-month-plan.md]
       - Pieces: P1 <slug> (funnel, aware) · P2 … · … [24-planning/01-month-plan.md]
       - Channels × posts: … [24-planning/02-calendar.md]
       - Tests: T1 on P1, P3 … [24-planning/01-month-plan.md]
       - Videos: … / none [24-planning/01-month-plan.md]
       - Approved on <date>; changes: … [client] [24-planning/05-approval.md]

3. **Write `gate.md`** (the five-line format in `00 - control/01 - law/TASK_CONTRACT.md` §2), then run `python3 "00 - control/02 - tools/task.py" advance <task-id>`.

## Self-check

- [ ] Were the checks run in order?

## Traps

- **Passing on a partial calendar.** A channel short of its quantity is a promise the client paid for and won't get.
