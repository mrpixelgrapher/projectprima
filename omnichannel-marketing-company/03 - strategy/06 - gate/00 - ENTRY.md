# 06 · Gate

**Purpose:** confirm the strategy is complete, approved and consistent. Then carry it forward and float the task to planning.

## Contract

- **Reads:** every file in `03-strategy/`; `client/approval-strategy.md`.
- **Writes:** the `## 03 - strategy` section of `CONTEXT.md`; `03-strategy/gate.md`; the `waiting on` field in `TASK.md`.
- **Done when:** `gate.md` says `VERDICT: PASS` and the task has advanced, **or** `VERDICT: HOLD` with `waiting on` set.

## Procedure

1. **Run the checks in order.** Stop at the first failure.

   | # | Check | On failure |
   |---|---|---|
   | T1 | The position statement follows the template, and every difference has proof in hand | stage 1 |
   | T2 | 3–5 pillars, each with cited proof, an objection and a buyer stage; aware, considering and deciding all covered | stage 2 |
   | T3 | One hub; every spoke passes both tests; within the cap; every other channel listed with a reason | stage 3 |
   | T4 | Every objective has a metric, baseline, target (client-given or approved) and review date | stage 4 |
   | T5 | `client/approval-strategy.md` records APPROVED, or APPROVED WITH CHANGES with the changes applied | no reply → **HOLD**; otherwise stage 5 |

2. **On a PASS, write the carry-forward** (at most 10 bullets, each with its source):

       ## 03 - strategy
       - Position: "<statement>" [03-strategy/01-positioning.md]
       - Promise: "<line>" [03-strategy/02-messages.md]
       - Pillars: P1 … · P2 … · P3 … [03-strategy/02-messages.md]
       - Brand name / voice decisions: … [client] [client/approval-strategy.md]
       - Hub: …; spokes: …; families: … [03-strategy/03-channel-plan.md]
       - Objectives: O1 …, review … [03-strategy/04-objectives.md]
       - Approved on <date> with changes: … [client/approval-strategy.md]

3. **Write `gate.md`** (the five-line format in `00 - control/01 - law/TASK_CONTRACT.md` §2), set `waiting on`, and on a PASS run `python3 "00 - control/02 - tools/task.py" advance <task-id>`.

## Self-check

- [ ] Is there a client approval on file, verbatim?
- [ ] Does the carry-forward name every channel in the plan?

## Traps

- **Advancing on an implied yes.** T5 needs the reply logged.
- **A carry-forward without the pillars.** Planning builds its pieces from the pillars.
