# 01 · Handover

**Purpose:** deliver the month's package with a short note that tells the client where to start, and log their acknowledgement.

## Contract

- **Reads:** `26-packaging/03-package.md`; `27-publishing/02-publish-log.md` (if publishing is included); `TASK.md` (kind); `00 - control/01 - law/HANDOFFS.md` (H1).
- **Writes:** `28-delivery/01-delivery-note-for-client.md`.
- **Done when:** the note is sent (or marked "not sent: rehearsal"), and the client's receipt is in `from-client/28-delivery-delivery-note-reply.md`, or 5 days have passed since sending.

## Procedure

1. **Write the note,** at most 150 words, in the client's language: one line of what's inside; "Start with the package page"; what's waiting (client-supplied items); if we publish, "every post is scheduled; live links follow"; what to send back and when (retainer: the numbers on day 20).
2. **Send (H1)** the note with the `26-packaging/` folder (the package page, the kit, the schedule). A rehearsal is written but not sent.
3. **Hold** for the receipt: `task.py hold <task-id> --on "H1 client: 28-delivery/01-delivery-note-for-client.md (receipt)"`. Resume when the reply lands, or after 5 days with a note "no receipt by <date>".

## Output template

    # Delivery note — <client label> · <month>
    Sent: <date, via> | not sent: rehearsal
    <≤ 150 words>

## Self-check

- [ ] Does the note point to the package page first?

## Traps

- **Sending the whole task folder.** The client gets `26-packaging/`, not our research workings, unless they ask.
