# 05 · Answers

**Purpose:** turn the client's reply into slot values with evidence, and settle the frame decisions left open. Then decide: ask the next round, or let the gate check the intake slots.

## Contract

- **Reads:** the reply, `from-client/11-intake-questions-round-N-reply.md` (the operator pastes it verbatim); `11-intake/01-parse.md`, `02-frame.md`, `03-routing.md`, `04-questions-round-N-for-client.md`; the previous `06-slot-board.md` from round 2 on.
- **Writes:** `11-intake/06-slot-board.md` (rewritten each round; the round is in its title). If another round is needed, it runs `04 - questions/` again, which writes `04-questions-round-N+1-for-client.md`.
- **Done when:** every question sent is marked answered or not answered; all 13 slots have a current status with evidence; either every intake slot is Known, or the next round has been sent and the task is on HOLD.

## Procedure

1. **Resume the task** if it is on HOLD: `python3 "00 - control/02 - tools/task.py" resume <task-id> --note "round N reply"`.
2. **Map the reply.** For each CQ sent in this round, find the exact words that answer it, or write "not answered". Never paraphrase into the map.
3. **Settle each UNDECIDED frame decision** from `02-frame.md`, using its deciding question:

   | The answer | Then |
   |---|---|
   | maps to one value | Write that value, citing [client: 11-intake-questions-round-N-reply CQn] |
   | is "not sure", and the decision is F1 | F1 = TO STRATEGY: strategy recommends a value, and the client approves it at `02 - content/02 - strategy/06 - approval/` |
   | is "not sure", and the decision is F2 or F4 | Ask again next round, with the options narrowed to two |
   | is missing | The decision stays UNDECIDED; its question goes into the next round |

4. **Recompute the package shape** from the lookup table in `01 - commercial/01 - intake/03 - frame/00 - ENTRY.md`.
5. **Update all 13 slots** with the status rules in `00 - control/01 - law/BRIEF_SLOTS.md`. Evidence for a Known value is a quote from the reply. An assumption the client corrected is replaced by their answer; one they didn't correct stays Assumed.
6. **Close readings.** For each reading pair from the parse, record which reading the answer confirmed.
7. **Decide the next step.**

   | Situation | Action |
   |---|---|
   | Every intake slot (SPEAKER, BRAND, OFFER in one line, GOAL, CHANNELS, LIMITS budget and timeline, EXECUTION, LANGUAGE) is Known, and F1, F2, F4 have values | Go to `06 - gate/` |
   | Any of them is still open | Run `04 - questions/` again for round N+1 (≤ 4 questions, numbering continues from the last CQ), send it, and hold |
   | The client has not replied within 7 days of sending | The operator sends one reminder; the task stays on HOLD. After 14 more days with no reply, the operator may close it: `task.py close <task-id> --reason "no reply to round N"` |

## Output template

`06-slot-board.md`:

    # Slot board — <task id> (after round N)
    ## Frame
    | Decision | Value | Evidence |
    Package shape: <cell from the lookup>
    ## Readings closed
    | Pair | Held | Evidence |
    ## Answers this round
    | CQ | The client's words | Fills |
    ## Slots
    | # | Slot | Status | Value | Evidence | Open part → route |
    ## Next
    <"intake slots all Known → gate", or "round N+1 sent: CQ5–CQ7">

## Worked example

Gemstone task, round-1 reply *(illustrative)*: "new name, not decided yet. want 10 company orders before diwali. we have instagram in english, no site. you make it, we post. budget around 40k a month, start next month."

| Decision / slot | Result |
|---|---|
| F1 | NEW, citing [client: 11-intake-questions-round-1-reply CQ1] "new name" |
| F4 | CONTENT-ONLY, citing "you make it, we post" |
| GOAL | Known: "10 company orders before diwali" |
| CHANNELS / LANGUAGE | Known: "instagram in english, no site" |
| LIMITS | Known (budget, timeline): "around 40k a month, start next month" |
| BRAND | Partly known: a new brand; the name is open → strategy proposes it, the client approves |
| Next | OFFER (one line) is still open: round 2 asks what the gifts are and whether they exist yet |

## Self-check

- [ ] Does every CQ sent have the client's exact words or "not answered"?
- [ ] Does every slot row carry the evidence its status requires?
- [ ] Was each UNDECIDED decision settled by the table above, not by judgment?
- [ ] If a next round is needed, was it sent and is the task on HOLD?

## Traps

- **Paraphrasing answers into slots.** A Known value must quote the reply.
- **"Not sure" read as consent.** It isn't an answer. Apply the table.
- **Moving on with one slot open.** "We'll find out at discovery" is a skip. Scope and pricing need every intake slot; ask again.
