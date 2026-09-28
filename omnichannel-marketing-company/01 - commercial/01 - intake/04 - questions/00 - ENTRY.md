# 04 · Questions

**Purpose:** send every open item to the one place that can close it: the client, research (ARENA, at discovery), or a stated assumption. Then write this round's client file, send it through the operator, and hold the task until the client answers.

## Contract

- **Reads:** `11-intake/01-parse.md`, `11-intake/02-frame.md` (and, from round 2 on, `11-intake/06-slot-board.md`); `00 - control/01 - law/BRIEF_SLOTS.md`; `00 - control/01 - law/HANDOFFS.md` (H1).
- **Writes:** `11-intake/03-routing.md`, `11-intake/04-questions-round-N-for-client.md` (N = the round), `11-intake/05-research-questions.md`.
- **Done when:** every open item has exactly one route; the client file can be sent without edits; every research question can be run by someone who never saw the request; the task is on HOLD for the reply.

## Procedure

1. **List the open items.** One row per:
   - Unknown slot, and the open part of each Partly-known slot.
   - UNDECIDED frame decision.
   - Deciding question from the parse that the frame didn't already absorb.

   If two items would be answered by the same question, merge them into one row.

2. **Route each item.**

   | Route | Rule | Becomes |
   |---|---|---|
   | CLIENT | About the client's own business, intentions, numbers, assets or decisions | CQn |
   | RESEARCH | About the outside world: buyers in general, market, competitors, norms, rules, platforms | RQn |
   | ASSUME | Only if a wrong assumption is cheap **and** reversible **and** shown to the client | ASn |

   A slot can split. BUYER: "which companies do you want" is CLIENT; "how such companies buy gifts" is RESEARCH.

3. **Rank the CLIENT items.**
   - P1: decides F1, F2 or F4.
   - P2: fills a slot first needed at intake (scope and pricing can't work without it): SPEAKER, BRAND, OFFER in one line, GOAL, CHANNELS, LIMITS (budget, timeline), EXECUTION, LANGUAGE.
   - P3: its answer changes which research to run.
   - P4: needed by a later node. These are **not asked here**: the node that needs them asks, so the client only ever answers what is needed now.

   A round is the top 4 of P1–P3. The rest wait for the next round, which `05 - answers/` sends after this one comes back. Rounds continue until every P1 and P2 item is answered.

4. **Write the client file,** `11-intake/04-questions-round-N-for-client.md` (template below). If there are no CLIENT items in P1–P3, write the file with the restated request, the assumptions, and "No questions: we have what we need to prepare your proposal"; it is still sent, and step 6 still holds (the client may correct an assumption).
   - Open by restating the request in the client's words.
   - Every question has: **why we ask**, in their terms; **options**, if the answer is a choice (always include "not sure"), or an **example answer**, if it is a fact; and **needed by**.
   - Recommend an option only when it is a real choice and you can state the reason in one line. Never recommend an answer to a factual question.
   - Use the client's own vocabulary. Explain any term they didn't use, unless their stated profession uses it every day (a performance marketer and "cost per lead").
   - End with the ASSUME items, under "What we'll assume unless you tell us otherwise".
   - If F3 marks "performance marketing" central, say in one line that the work is organic content engineered to convert, not paid ads, so the client isn't surprised at the proposal.

5. **Write the research file.** These questions are not run here: `02 - content/01 - discovery/01 - requests/` sends them to ARENA.
   - Every RQ states: what to capture; the source categories to try; the node that needs it; and a condition ("unconditional", or "after CQn": include it in the ARENA request only once that answer has arrived).
   - A research question may point at an area to check. It may not state the answer.
6. **Send and hold** (`00 - control/01 - law/HANDOFFS.md` H1). The operator sends the client file unchanged; the reply comes back as `from-client/11-intake-questions-round-N-reply.md`. Run:

       python3 "00 - control/02 - tools/task.py" hold <task-id> --on "H1 client: 11-intake/04-questions-round-N-for-client.md"

   For a `rehearsal` task, write the file but don't send it: hold with `--on "H1 client (rehearsal: not sent): …"`.

## Output templates

`03-routing.md`:

    # Routing — <task id>
    | Item | Route | Becomes | Priority | Round | Needed by |
    ## Next rounds (client questions held back)
    | CQ | Question | Needed by |

`04-questions-round-N-for-client.md`:

    # Questions for you — round N
    You asked us to: "<the literal ask, in their words>". If we've misread that, tell us first.
    ## CQ1. <question>
    Why we ask: …
    Options: … / … / not sure        (or: Example answer: …)
    Needed by: <node>
    …
    ## What we'll assume unless you tell us otherwise
    - AS1: …

`05-research-questions.md`:

    # Research questions — <task id>
    ## RQ1. <question>
    Capture: … · Sources: … · Needed by: <node> · Condition: …

## Worked example

Gemstone request, round 1 (P1 → P3):

| CQ | Question | Priority | Why it's in round 1 |
|---|---|---|---|
| CQ1 | Will the corporate gifts be sold under your current business name, or a new name? | P1 | Decides F1 |
| CQ2 | What do you want this to achieve in the first 3 months, and how will you know it worked? (Example answer: "10 company orders before Diwali") | P2 | GOAL: scope sizes the work to it |
| CQ3 | Which accounts, site or newsletter do you run today, and in which language do you post? (Example answer: "Instagram in English and Hindi, a website, no newsletter") | P2 | CHANNELS and LANGUAGE |
| CQ4 | Do you want us to post for you, or to hand you everything ready to post? And what monthly budget and start date do you have in mind? | P1 + P2 | Decides F4; LIMITS for pricing |

Round 2 *(after the reply)*: which companies they want to sell to (P3: it sets the ARENA research), unless round 1's answers already named them.

RQ1: *How do companies in the target segment choose and buy corporate gifts: who decides, which occasions, lead times, budget per gift?* Condition: after the buyer question is answered. Needed by: 02 - content/01 - discovery.

AS1: *We make the content; you or your team publish it and handle orders.*

## Self-check

- [ ] Does every open item from the parse and frame appear in routing, exactly once?
- [ ] Does this round have at most 4 questions, chosen by priority, with no P4 item?
- [ ] Is the task on HOLD, naming the client file?
- [ ] Does the client file open with the restated request and close with the assumptions?
- [ ] Does each question have why, options or an example, and needed-by?
- [ ] Does every RQ have capture, sources, needed-by and a condition, with no answer written into it?

## Traps

- **Asking the client what research can find** ("What do companies spend on gifts?"). That is RQ, not CQ.
- **A leading question** that assumes one reading ("What will the new brand be called?" before CQ1 is answered).
- **Homework.** More than 4 questions, or questions that need marketing know-how to answer.
- **A hidden assumption.** Proceeding on a guess that isn't listed as an AS item.
