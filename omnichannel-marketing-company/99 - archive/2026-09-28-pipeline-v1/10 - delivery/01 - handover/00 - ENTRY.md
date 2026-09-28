# 01 · Handover

**Purpose:** deliver the package with a short note that tells the client where to start, and log their acknowledgement.

## Contract

- **Reads:** `09-packaging/00-package.md`; `TASK.md` (kind).
- **Writes:** `10-delivery/01-delivery-note.md`; `client/receipt.md` when the client replies.
- **Done when:** the note is written and sent (or marked "not sent: rehearsal"), and `waiting on` names the receipt.

## Procedure

1. **Write the note.** At most 150 words:
   - one line of what's inside;
   - "Start with `09-packaging/00-package.md`";
   - what's waiting;
   - what to send back;
   - when you'll check results together (the objectives' review date).
2. **Send** the note plus the task's `09-packaging/` folder (the package page, the PUBLISH_KIT, the schedule) through the client's channel. For a `rehearsal` task, write "not sent: rehearsal" at the top of the note, and don't send.
3. **Set `waiting on`** to `client receipt`.
4. **When the client replies,** log the reply verbatim in `client/receipt.md`.

## Output template

    # Delivery note — <client label>
    Sent: <date, via> | not sent: rehearsal
    <≤ 150 words>

## Self-check

- [ ] Does the note point to the package page first?
- [ ] Is the review date stated?

## Traps

- **Sending the whole task folder.** The client gets `09-packaging/`, not our research workings, unless they ask.
