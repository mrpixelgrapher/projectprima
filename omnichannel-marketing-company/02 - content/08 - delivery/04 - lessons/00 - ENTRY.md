# 04 · Lessons

**Purpose:** turn what went wrong or right in this task into specific fixes to the instructions, so the next task runs better. A lesson with no file to change is only a note.

## Contract

- **Reads:** `TASK.md` (History: returns, holds); every `gate.md`, `gate-superseded-*.md` and review in the task (including `25-writing/*/07-review.md`); `from-operator/25-writing-human-check.md`; `28-delivery/02-record.md`; `02 - content/08 - delivery/ledgers/lessons-log.md`.
- **Writes:** `28-delivery/04-lessons.md`; one row in `02 - content/08 - delivery/ledgers/lessons-log.md`.
- **Done when:** every HOLD that waited longer than planned, every return, every human-check FIX, every client correction and every effort difference over 25% has a lesson, and every lesson names a file and the change to make.

## Procedure

1. **Collect the events:** every `returned` row in History; every HOLD that lasted longer than a week; every human-check FIX; every client correction (at strategy, plan approval, or in replies); every effort difference over 25% in the record.
2. **One lesson per event.** Give: what happened; its cause (which instruction was unclear, missing or wrong); the fix (the exact file, e.g. `02 - content/02 - strategy/04 - channels/00 - ENTRY.md`, and the change to make). An effort difference fixes a row of `01 - commercial/02 - scope/02 - breakdown/effort-table.md`.
3. **Promotion rule.** Search `lessons-log.md` for the same cause.
   - If it appears in **2 or more tasks**, apply the fix now. Append a dated "Lesson from T-…" line or rule to that stage ENTRY (Tier 2: append, never rewrite), or a superseding dated row to the effort table, and log it in `00 - control/03 - state/meta_workspace.md` §3.
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
- **Blaming ARENA or the image factory.** A thin dossier or a wrong still usually traces to our request; fix the request instruction.
