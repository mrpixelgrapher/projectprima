# 03 · Gate

**Purpose:** confirm every transition is accepted, and advance to the edit plan.

## Contract

- **Reads:** `34-motion/00-motion-index.md`.
- **Writes:** the `## 34-motion` section of `CONTEXT.md`; `34-motion/gate.md`.
- **Done when:** the task has advanced.

## Procedure

1. **Checks:** MO1 every moving shot and non-cut transition has a prompt (else 01 - prompts); MO2 every clip is ACCEPTED (else 02 - check).
2. **Carry forward** (at most 3 bullets): clips accepted; revision rounds; shots the operator simplified.
3. **Write `gate.md`** (five-line format), then `task.py advance <task-id>`.

## Self-check

- [ ] Is every clip accepted?

## Traps

- **Leaving a gap for the editor to "fix".** The edit plan assumes every clip exists.
