# 05 · Gate

**Purpose:** confirm the record is complete and the lessons are written, carry the month forward, and pass the task to the delivery invoice.

## Contract

- **Reads:** everything in `28-delivery/`; the ledgers.
- **Writes:** the `## 28-delivery` section of `CONTEXT.md`; `28-delivery/gate.md`.
- **Done when:** the task has advanced to `01 - commercial/07 - billing-delivery`.

## Procedure

1. **Run the checks in order.**

   | # | Check | On failure |
   |---|---|---|
   | E1 | The delivery note was sent (or marked rehearsal), and the receipt is logged or 5 days have passed | 01 - handover |
   | E2 | The record has what shipped, the time per node from History, and the client's response; the ledger row is appended | 02 - record |
   | E3 | A retainer has its results plan; a one-off says so | 03 - results-plan |
   | E4 | Every event has a lesson with a file; twice-seen fixes are applied | 04 - lessons |

2. **Write the carry-forward:**

       ## 28-delivery
       - Delivered: <date> · shipped: … [28-delivery/02-record.md]
       - Response: … [28-delivery/02-record.md]
       - Results: asked on <date> / not tracked (one-off) [28-delivery/03-results-plan.md]
       - Lessons: N, applied: … [28-delivery/04-lessons.md]

3. **Write `gate.md`** (the five-line format in `00 - control/01 - law/TASK_CONTRACT.md` §2), then run `python3 "00 - control/02 - tools/task.py" advance <task-id>`.

## Self-check

- [ ] Is every ledger row traceable to this task's files?

## Traps

- **Closing without lessons.** The next month inherits the same gaps.
