# 03 · Gate

**Purpose:** confirm the month is scheduled as approved, and advance to delivery.

## Contract

- **Reads:** `27-publishing/*.md`.
- **Writes:** the `## 27-publishing` section of `CONTEXT.md`; `27-publishing/gate.md`.
- **Done when:** the task has advanced.

## Procedure

1. **Checks:** PB1 every post in the schedule is on the run sheet (else stage 1); PB2 every row is scheduled or live, or "could not" with a next step the operator confirmed (else stage 2).
2. **Carry forward** (at most 3 bullets): N posts scheduled, M live so far; any could-not and its next step.
3. **Write `gate.md`** (five-line format), then `task.py advance <task-id>`.

## Self-check

- [ ] Is every post accounted for?

## Traps

- **Advancing with unscheduled posts unexplained.**
