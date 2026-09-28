# 02 · Gate

**Purpose:** act on the review verdict. A PASS floats the piece to shaping; a FAIL sends it back to the named node with the reason recorded.

## Contract

- **Reads:** `07-review/01-review-report.md`; History in `TASK.md`.
- **Writes:** the `## 07 - review` section of `CONTEXT.md`; `07-review/gate.md`.
- **Done when:** the task has moved forward (PASS) or backward (FAIL).

## Procedure

1. **Loop limit.** If History shows this task has been returned for the **same check** 3 times, don't return it again. Set `VERDICT: HOLD`, `waiting on: operator (repeated FAIL on <check>)`, and stop. A defect that keeps coming back usually sits upstream, in the brief or the strategy.
2. **On a PASS:**
   - Append to CONTEXT.md:

         ## 07 - review
         - Verdict: PASS (round N) [07-review/01-review-report.md]
         - SURPLUS: … [07-review/01-review-report.md]

   - Write `gate.md` (the five-line format in `00 - control/01 - law/TASK_CONTRACT.md` §2) with `VERDICT: PASS`, then run `python3 "00 - control/02 - tools/task.py" advance <task-id>`.
3. **On a FAIL:**
   - Write `gate.md` with `VERDICT: HOLD`, the failed check, and the stage to return to.
   - Run `python3 "00 - control/02 - tools/task.py" advance <task-id> --to "<node from the report>" --reason "<check>: <defect>; rerun stage <stage>"`.
   - The receiving node reruns from the named stage, and its later stages overwrite their files.

## Self-check

- [ ] On a FAIL, does the reason name both the check and the stage to rerun?

## Traps

- **Fixing it here.** Review never repairs. Only the returning node does.
