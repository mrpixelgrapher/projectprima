# 04 · Questions

**Purpose:** send every open item to the one place that can close it: the client, research, or a stated assumption. Then write the round-1 client file, which is the node's send unit.

## Contract

- **Reads:** `01-intake/01-parse.md`, `01-intake/02-frame.md`, `00 - control/01 - law/BRIEF_SLOTS.md`.
- **Writes:** `01-intake/03-routing.md`, `01-intake/04-client-questions.md`, `01-intake/05-research-questions.md`.
- **Done when:** every open item has exactly one route; the client file can be sent without edits; every research question can be run by someone who never saw the request.

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
   - P2: its answer changes which research to run.
   - P3: needed by `02 - discovery`.
   - P4: needed later.

   Round 1 is the top 4. Everything else is round 2.

4. **Write the client file** (template below).
   - Open by restating the request in the client's words.
   - Every question has: **why we ask**, in their terms; **options**, if the answer is a choice (always include "not sure"), or an **example answer**, if it is a fact; and **needed by**.
   - Recommend an option only when it is a real choice and you can state the reason in one line. Never recommend an answer to a factual question.
   - Use the client's own vocabulary. Explain any term they didn't use, unless their stated profession uses it every day (a performance marketer and "cost per lead").
   - End with the ASSUME items, under "What we'll assume unless you tell us otherwise".

5. **Write the research file.**
   - Every RQ states: what to capture; the source categories to try; the node that needs it; and a condition ("unconditional", or "after CQn": run only once that answer arrives).
   - A research question may point at an area to check. It may not state the answer.

## Output templates

`03-routing.md`:

    # Routing — <task id>
    | Item | Route | Becomes | Priority | Round | Needed by |
    ## Round 2 (client questions held back)
    | CQ | Question | Needed by |

`04-client-questions.md`:

    # Questions for you — round 1
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
| CQ2 | Which companies do you want to sell gifts to? (Example answer: "mid-sized law firms in our city, for year-end client gifts") | P2 | Sets the buyer segment and the geography for research |
| CQ3 | What would the gifts be, and do they exist yet? (ready to sell / designs, not final / still an idea / not sure) | P3 | OFFER, needed by discovery |
| CQ4 | What price per gift, and roughly how many gifts per company order? | P3 | Who approves a purchase depends on its size |

RQ1: *How do companies in the target segment choose and buy corporate gifts: who decides, which occasions, lead times, budget per gift?* Condition: after CQ2. Needed by: 02 - discovery.

AS1: *We make the content; you or your team publish it and handle orders.*

## Self-check

- [ ] Does every open item from the parse and frame appear in routing, exactly once?
- [ ] Does round 1 have at most 4 questions, chosen by priority?
- [ ] Does the client file open with the restated request and close with the assumptions?
- [ ] Does each question have why, options or an example, and needed-by?
- [ ] Does every RQ have capture, sources, needed-by and a condition, with no answer written into it?

## Traps

- **Asking the client what research can find** ("What do companies spend on gifts?"). That is RQ, not CQ.
- **A leading question** that assumes one reading ("What will the new brand be called?" before CQ1 is answered).
- **Homework.** More than 4 questions, or questions that need marketing know-how to answer.
- **A hidden assumption.** Proceeding on a guess that isn't listed as an AS item.
