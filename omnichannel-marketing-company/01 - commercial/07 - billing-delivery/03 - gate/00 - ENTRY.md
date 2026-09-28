# 03 · Gate

**Purpose:** finish the task.

## Contract

- **Reads:** `17-billing-delivery/*.md`.
- **Writes:** the `## 17-billing-delivery` section of `CONTEXT.md`; `17-billing-delivery/gate.md`.
- **Done when:** the task is in `clients/<client>/done/` with status DONE.

## Procedure

1. **Checks:** BD1 the invoice bills only what shipped, re-adds and is logged (else stage 1); BD2 the history row exists, and next month's task exists or the reason is stated (else stage 2).
2. **Carry forward** (at most 3 bullets): invoice number and total; next month's task, or none.
3. **Write `gate.md`** (five-line format), then `task.py advance <task-id>`. The route is complete, so the tool files the task in `clients/<client>/done/`.

## Self-check

- [ ] Is the task filed as DONE?

## Traps

- **Leaving the month open.** A retainer with no next task stops without anyone deciding it should.
