# 03 · Gate

**Purpose:** release the task to the content department.

## Contract

- **Reads:** `16-billing-advance/*.md`; `from-operator/16-billing-advance-payment.md`.
- **Writes:** the `## 16-billing-advance` section of `CONTEXT.md`; `16-billing-advance/gate.md`.
- **Done when:** the task has advanced.

## Procedure

1. **Checks:** BA1 the invoice is complete, itemised and logged as issued (else stage 1); BA2 the payment is confirmed and logged as paid, or the operator's written decision to start is in `from-operator/` (else stage 2).
2. **Carry forward** (at most 3 bullets): invoice number and total; paid on <date>; anything owed.
3. **Write `gate.md`** (five-line format), then `task.py advance <task-id>`.

## Self-check

- [ ] Is the payment (or the operator's decision) in `from-operator/`?

## Traps

- **Advancing on HOLD.** The tool refuses; resume only when the payment has landed.
