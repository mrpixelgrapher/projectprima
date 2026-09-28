# 04 · Acceptance

**Purpose:** send the signed-off proposal, and record exactly what the client accepted, changed or declined.

## Contract

- **Reads:** the latest `14-proposal/02-proposal…-for-client.md`; the client's reply, `from-client/14-proposal-proposal-reply.md` (for a revision, `…-proposal-v2-reply.md`); `00 - control/01 - law/HANDOFFS.md` (H1).
- **Writes:** `14-proposal/04-acceptance.md`; one row in `01 - commercial/ledgers/proposals.md` when sent.
- **Done when:** the outcome is recorded (accepted with the add-ons chosen, changes requested, or declined), quoting the client.

## Procedure

1. **Send and hold** (H1). Append a `sent` row to `ledgers/proposals.md`. Then `task.py hold <task-id> --on "H1 client: 14-proposal/02-proposal-for-client.md"`. For a rehearsal task, don't send; hold with "(rehearsal: not sent)".
2. **When the reply lands,** resume and classify it:

   | The client's words | Outcome | Next |
   |---|---|---|
   | accept, with or without add-ons | ACCEPTED | Record the add-ons chosen; go to the gate |
   | ask for changes (price, quantity, channels) | CHANGES | Back to `01 - package/` with the change; a v2 document; sign-off again; send again |
   | decline, or no reply 14 days after a reminder | DECLINED | Record it; the gate closes the task |

3. **Record** the outcome with the client's exact words, and append the outcome row to `ledgers/proposals.md`.

## Output template

    # Acceptance — <task id>
    Proposal version: … · Sent: <date> · Reply: <date>
    Outcome: ACCEPTED / CHANGES / DECLINED
    The client's words: "…" [client: from-client/…]
    Add-ons chosen: … / none
    Includes (final): …

## Self-check

- [ ] Is the outcome quoted from the client?
- [ ] Are the add-ons chosen reflected in the final includes?

## Traps

- **Reading "sounds good" as acceptance of everything.** Confirm which add-ons, if any, before the gate.
