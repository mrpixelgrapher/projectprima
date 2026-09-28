# 02 · Gate

**Purpose:** confirm every video can be assembled from its edit plan, and send the task back to the content line for packaging.

## Contract

- **Reads:** `35-edit-plan/*.md`.
- **Writes:** the `## 35-edit-plan` section of `CONTEXT.md`; `35-edit-plan/gate.md`.
- **Done when:** the task has advanced to `02 - content/06 - packaging`.

## Procedure

1. **Checks:** EP1 every video has an edit plan covering every second (else 01 - edit-plan); EP2 VO, text, captions and end card are timed; exports are set (else 01 - edit-plan).
2. **Carry forward** (at most 3 bullets): videos ready to assemble; who records the voice-over; export targets.
3. **Write `gate.md`** (five-line format), then `task.py advance <task-id>`.

## Self-check

- [ ] Could an editor assemble each video without asking a question?

## Traps

- **An edit plan that relies on a clip that was never accepted.**
