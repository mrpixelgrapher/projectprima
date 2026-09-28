# 03 · Lessons

**Purpose:** turn what went wrong or right in this task into specific fixes to the instructions, so the next task runs better. A lesson with no file to change is only a note.

## Contract

- **Reads:** `TASK.md` (History: returns, holds); every `gate.md` and review report in the task (including `09-packaging/pieces/*`); `10-delivery/02-record.md`; `10 - delivery/ledgers/lessons-log.md`.
- **Writes:** `10-delivery/03-lessons.md`; one row in `10 - delivery/ledgers/lessons-log.md`.
- **Done when:** every HOLD, return and client correction has a lesson, and every lesson names a file and the change to make.

## Procedure

1. **Collect the events:** every HOLD, every `returned` row in History, every client correction (in approval or round-2 answers), and every item that waited longer than a week.
2. **One lesson per event.** Give: what happened; its cause (which instruction was unclear, missing or wrong); the fix (the exact file, e.g. `03 - strategy/03 - channels/00 - ENTRY.md`, and the change to make).
3. **Promotion rule.** Search `lessons-log.md` for the same cause.
   - If it appears in **2 or more tasks**, apply the fix now. Append a dated "Lesson from T-…" line or rule to that stage ENTRY (Tier 2: append, never rewrite), and log it in `00 - control/03 - state/meta_workspace.md` §3.
   - At its first appearance, log it only.
4. **What worked:** 1–3 lines on what to keep doing.
5. **Append the log row.**

## Output template

    # Lessons — <task id>
    | Event | Cause (instruction) | Fix (file · change) | Seen before? | Applied? |
    ## Keep doing

## Self-check

- [ ] Does every event from History have a lesson?
- [ ] Does every lesson name a file?
- [ ] Were the fixes that appeared twice applied and logged?

## Traps

- **Blaming the client.** "The client was slow" is not a lesson. "Round-1 questions needed options, not open text" is.
