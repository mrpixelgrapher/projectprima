# 01 · Answers

**Purpose:** turn the client's reply into slot values with evidence, and settle the frame decisions intake left open. The research stage needs to know which conditions are now met; the brief needs every slot's current status.

## Contract

- **Reads:** the client's reply, as received; `01-intake/01-parse.md`, `02-frame.md`, `03-routing.md`, `04-client-questions.md`.
- **Writes:** `client/answers-round-N.md` (N = the round); `02-discovery/01-slot-board.md`. If round 2 is needed: `02-discovery/01-round-2-questions.md`.
- **Done when:** every question sent is marked answered or not answered; all 12 slots have a current status with evidence; F1, F2 and F4 each have a value, or a round-2 question.

## Procedure

1. **Log the reply verbatim** in `client/answers-round-N.md`: when and how it arrived, the full text in a `text` block, then a map from each CQ to the exact words that answer it, or "not answered".
2. **Settle each UNDECIDED frame decision** from `01-intake/02-frame.md`, using its deciding question.

   | The answer | Then |
   |---|---|
   | maps to one value | Write that value, citing [client: answers-round-N CQn] |
   | is "not sure", and the decision is F1 | F1 = TO STRATEGY: strategy will recommend a value, and the client approves it at `03 - strategy/05 - approval/` |
   | is "not sure", and the decision is F2 or F4 | Ask again in round 2, with the options narrowed to two |
   | is missing | The decision stays UNDECIDED; its question goes into round 2 |

3. **Recompute the package** from the lookup table in `01 - intake/03 - frame/00 - ENTRY.md`.
4. **Update all 12 slots.** Apply the status rules in `00 - control/01 - law/BRIEF_SLOTS.md`. Evidence is a quote from the reply, cited as [client: answers-round-N CQn]. An AS assumption the client corrected is replaced by their answer; one they didn't correct stays Assumed.
5. **Close readings.** For each reading pair from the parse, record which reading the answer confirmed.
6. **Decide on round 2.**

   | Situation | Action |
   |---|---|
   | Any CLIENT item needed by 02 is still open, **or** F2 or F4 is still UNDECIDED | Write `01-round-2-questions.md`, using the rules and template of `01 - intake/04 - questions/00 - ENTRY.md`: at most 4 questions, numbering continues from the last CQ, P1–P4 ranking. The gate will HOLD |
   | Only items needed later are open | Carry them to the round-2 list in the brief; no send now |

## Output template

`01-slot-board.md`:

    # Slot board — <task id> (after round N)
    ## Frame
    | Decision | Value | Evidence |
    Package: <cell from the lookup>
    ## Readings closed
    | Pair | Held | Evidence |
    ## Slots
    | # | Slot | Status | Value | Evidence | Open part → route |
    ## Round 2
    <"not needed", or "sent: CQ5–CQ7 in 01-round-2-questions.md">

## Worked example

Gemstone task. The client's reply *(illustrative)*: "new name, not decided yet. IT and consulting firms in our city, 50–300 people, for festival and client gifts. We have 3 desk-piece designs with gemstones, not final. Around 3,000–15,000 per gift, 20–200 pieces an order."

| Decision / slot | Result |
|---|---|
| F1 | NEW, citing [client: answers-round-1 CQ1] "new name" |
| Package | Name + positioning, then the launch set |
| BRAND | Partly known: a new brand. Open: the name → strategy proposes, the client approves |
| BUYER | Partly known: "IT and consulting firms in our city, 50–300 people". Open: who inside the firm decides → RQ1 |
| OFFER | Partly known: "3 desk-piece designs with gemstones, not final". Open: the final range → CQ5 in round 2 (needed by 02) |

## Self-check

- [ ] Is the reply logged verbatim, with every CQ mapped?
- [ ] Does every slot row carry the evidence its status requires?
- [ ] Was each UNDECIDED decision settled by the table above, not by judgment?
- [ ] If round 2 is needed, does it follow the intake question rules (≤ 4, why, options or example, needed-by)?

## Traps

- **Paraphrasing answers into slots.** A Known value must quote the client's reply.
- **"Not sure" read as consent.** It isn't an answer. Apply the table.
- **Round 2 as homework.** Asking the client what research can find ("what do firms usually spend?"). That is an RQ.
