# 06 · Approval

**Purpose:** get the client's yes on one page before anything is designed or written. Unclear scope blocks the task; it is never a footnote.

## Contract

- **Reads:** `22-strategy/01-positioning.md` to `05-objectives.md`; `11-intake/00-request.md`; `clients/<client>/engagement.md`; `CONTEXT.md`; `00 - control/01 - law/HANDOFFS.md` (H1).
- **Writes:** `22-strategy/06-strategy-for-client.md` (the send unit); after the reply, `22-strategy/07-approval.md`.
- **Done when:** the reply is in `from-client/22-strategy-strategy-reply.md`, and `07-approval.md` records APPROVED, or APPROVED WITH CHANGES with the changes applied to the stage files and to `06-strategy-for-client.md`.

## Procedure

1. **Write the summary.** One page, in the client's language and vocabulary, with no internal IDs. These sections, in this order:
   - what you asked for (their words);
   - who we'll write for;
   - what we'll say (the promise and the pillars);
   - where everyone ends up (the destination and its one action);
   - where we'll publish (each channel, one line of role);
   - what success means (the objectives and when we'll read them);
   - **decisions we need from you** (at most 4: the name, the destination, targets, voice, claims to prove);
   - what we assume.
2. **Send and hold** (H1): `task.py hold <task-id> --on "H1 client: 22-strategy/06-strategy-for-client.md"`. A rehearsal is not sent.
3. **When the reply lands,** resume the task and apply it:

   | Reply | Action |
   |---|---|
   | APPROVED | Record the decisions in `07-approval.md`; go to `07 - gate/` |
   | APPROVED WITH CHANGES | Apply each change to the stage file it affects, and update `06-strategy-for-client.md` so it states the approved strategy; log each change with the client's quote. A change to the position statement reruns stages 2–5 |
   | REJECTED, or a new direction | Return to the stage the reply points at, log the reason, and send a new summary |
   | No reply after 7 days | The operator sends one reminder; the task stays on HOLD |

## Output template

`06-strategy-for-client.md`:

    # Strategy — for <client label>
    ## What you asked for
    ## Who we'll write for
    ## What we'll say
    ## Where everyone ends up
    ## Where we'll publish
    ## What success means
    ## Decisions we need from you
    1. … (options / our recommendation and why)
    ## What we'll assume unless you tell us otherwise

`07-approval.md`:

    # Approval — <task id>
    Reply: <date> · Outcome: APPROVED / APPROVED WITH CHANGES
    | Decision | The client's words | Applied to |

## Worked example

Gemstone task *(illustrative)*: decision 1: "The name for the gift line: Kora Gifts (our recommendation: short, reads as a gift, and keeps your name) / Stoneline Corporate / your own idea". Decision 2: "Where everyone ends up: a page where HR teams request your festival catalogue. Yes / we'd rather take orders on WhatsApp".

## Self-check

- [ ] Is the summary one page, without jargon or internal IDs?
- [ ] Are there at most 4 decisions, each with options and a stated reason for any recommendation?
- [ ] Is every change the client asked for applied, with their quote?

## Traps

- **Burying the decisions.** If the name choice sits in paragraph four, it won't be answered.
- **Silence read as approval.** No reply means HOLD.
