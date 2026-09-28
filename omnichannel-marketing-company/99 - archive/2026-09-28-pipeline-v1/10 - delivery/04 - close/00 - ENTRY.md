# 04 · Close

**Purpose:** confirm the record is complete, carry the last section forward, and file the task in `done/` as the permanent record of the job.

## Contract

- **Reads:** everything in `10-delivery/`; the ledgers.
- **Writes:** the `## 10 - delivery` section of `CONTEXT.md`; `10-delivery/gate.md`.
- **Done when:** the task is in `10 - delivery/done/` with status DONE.

## Procedure

1. **Run the checks in order.**

   | # | Check | On failure |
   |---|---|---|
   | E1 | The delivery note exists; it was sent, or marked rehearsal | stage 1 |
   | E2 | The record has shipped, cost, response and (for a proof run) disposition; the ledger rows are appended | stage 2 |
   | E3 | Every event has a lesson with a file; twice-seen fixes are applied | stage 3 |
   | E4 | A client response is logged, or 14 days have passed since sending (or it's a rehearsal) | **HOLD** (waiting on the client receipt) |

2. **Write the carry-forward:**

       ## 10 - delivery
       - Delivered: <date> · shipped: … [10-delivery/02-record.md]
       - Response: … · disposition: … [10-delivery/02-record.md]
       - Lessons: N, applied: … [10-delivery/03-lessons.md]

3. **Write `gate.md`** (the five-line format in `00 - control/01 - law/TASK_CONTRACT.md` §2), then run `python3 "00 - control/02 - tools/task.py" advance <task-id>`. The task moves to `done/`.

## Self-check

- [ ] Is every ledger row traceable to this task's files?

## Traps

- **Closing without lessons.** The next task inherits the same gaps.
