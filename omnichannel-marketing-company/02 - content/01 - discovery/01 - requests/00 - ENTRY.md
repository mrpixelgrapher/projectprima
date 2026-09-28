# 01 · Requests

**Purpose:** send out, in one go, everything discovery needs from outside: the research and the top-creator sampling to ARENA, and any questions only the client can answer. Then wait for both. The rest of the node works only from what comes back.

## Contract

- **Reads:** `CONTEXT.md`; `11-intake/05-research-questions.md` (RQs queued at intake); `11-intake/06-slot-board.md`; `clients/<client>/profile.md`; `clients/<client>/engagement.md` (the channels bought); for a returning client, `clients/<client>/brief.md`, `creators.md`, `voice.md`; `query-bank.md` in this folder; `00 - control/01 - law/HANDOFFS.md` (H1, H3).
- **Writes:** `21-discovery/arena-request-1.md`; `21-discovery/01-questions-round-N-for-client.md` when the client must answer something; `21-discovery/01-requests.md` (what went out, and what is awaited).
- **Done when:** the ARENA request and any client questions are written and handed to the operator, and the task is on HOLD naming both.

## Procedure

1. **Returning client?** If `clients/<client>/brief.md` and `creators.md` are filled and less than 6 months old, research only what is new (a new offer, buyer or channel); say so at the top of the request. Otherwise, research everything below.
2. **Research questions.** Take every RQ from intake whose condition is met, and add the query-bank questions this client needs (`query-bank.md`: buyer, buying behaviour, alternatives, rules, channel facts for every channel in the engagement). Replace the placeholders with the client's values. Group them into lanes: buyer, market, rules, channels.
3. **Creator sampling spec,** one block per channel in the engagement:
   - Niche: the client's category and buyer, in 1 line (from the profile).
   - Creators: the top 5 in the niche on that channel, by engagement on recent posts; for each, 5 recent posts that performed best.
   - Extract for each post: the hook (first line or frame), the structure and format, the angle (and whether the angle looks saturated), the funnel mechanics (the call to action, lead magnet, link placement, cross-posting), posting cadence and time, and the visual style.
   - Rule: patterns and links only; no creator's text is to be reused as ours.
4. **Client questions** (only what discovery needs and only the client knows): the buyer, named (who they sell to, if intake didn't settle it); 3–5 samples of their own writing, or, if they have none, 1–2 creators whose way of talking they want to sound like; documents behind any proof they claim (certificates, results). Use the rules and template of `01 - commercial/01 - intake/04 - questions/00 - ENTRY.md` (≤ 4 questions; why, options or an example, needed-by).
5. **Write** `arena-request-1.md` in the ARENA format (`HANDOFFS.md`), with "Return to: `<task>/21-discovery/arena-dossier-1/`". Write the client file if there are questions.
6. **Write `01-requests.md`:** each request, its file, its hand-off, what it must return, and where the return lands.
7. **Hold on both:**

       python3 "00 - control/02 - tools/task.py" hold <task-id> --on "H3 ARENA: 21-discovery/arena-request-1.md; H1 client: 21-discovery/01-questions-round-1-for-client.md"

   For a rehearsal task, write both but send neither; hold with "(rehearsal: not sent)".

## Output template

`01-requests.md`:

    # Requests — <task id>
    | Request | File | Hand-off | Must return | Lands at | Status |
    | ARENA research + creator sampling | arena-request-1.md | H3 | a dossier: one section per RQ, one per channel sampled | 21-discovery/arena-dossier-1/ | sent <date> |
    | Client round 1 | 01-questions-round-1-for-client.md | H1 | answers to CQn–CQm | from-client/21-discovery-questions-round-1-reply.md | sent <date> |

## Worked example

Gemstone task, excerpt of `arena-request-1.md` *(illustrative)*:

    ## What we must learn
    RQ1. How do IT and consulting firms of 50–300 people in <city> choose and buy corporate gifts:
         who decides, which occasions, lead times, budget per gift? — Why: buyer profile, timing of the plan
    ## Top-creator sampling
    Niche: corporate gifting and fine gemstones, for HR and admin buyers in India · Channels: Instagram, LinkedIn
    Creators per channel: 5 · Posts per creator: 5 (best-performing, last 90 days)

## Self-check

- [ ] Does every RQ whose condition is met appear in the ARENA request, with the decision it feeds?
- [ ] Does the sampling spec cover every channel in the engagement?
- [ ] Does every client question pass the intake question rules?
- [ ] Is the task on HOLD, naming every request?

## Traps

- **Researching ourselves.** The node has no browser. Research goes to ARENA; nothing is "looked up" here.
- **A request only this task understands.** ARENA sees only the request file. It must name the client, buyer, place and every question in full.
- **Asking the client what ARENA can find.** "What do firms spend on gifts?" is an RQ.
