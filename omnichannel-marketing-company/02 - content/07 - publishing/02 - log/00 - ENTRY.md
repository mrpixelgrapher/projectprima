# 02 · Log

**Purpose:** a record of every post: scheduled, live, or could not, with its link. Delivery and the month review rely on it.

## Contract

- **Reads:** `from-operator/27-publishing-run-sheet.md`; the run sheet.
- **Writes:** `27-publishing/02-publish-log.md`.
- **Done when:** every run-sheet row has a status from the operator's reply, and every "could not" has a next step.

## Procedure

1. **Resume** the task when the operator's reply lands.
2. **One row per post:** status (scheduled / live / could not), the scheduler's confirmation or the live URL, the date.
3. **"Could not":** name why and the next step (the operator fixes access; the post moves to a new date, which the client is told about in the delivery note).

## Output template

    # Publish log — <client> · <month>
    | # | Date | Channel | Kit file | Status | Confirmation / URL | Next step |

## Self-check

- [ ] Is every row's status from the operator, not assumed?

## Traps

- **Marking scheduled as live.** Live means a URL.
