# D-001 — Buyer and problem

Status: **STAGED** — the queries are written and have not run. Staged 2026-09-28, session S002.
Brief and lane map: `02-sourcing/research_plan.md`.
Runs lane by lane, as part of the station that reads each lane (`02-sourcing/research_plan.md`): L1 and L4 may run now; L2 and L3 wait until station S1 is FILLED (`python3 00-control/tools/line_status.py`).

## How to run

Each query is self-contained: an agent with web access, or a person with a search engine, can run it without reading anything else.

For every source found, append a row to `02-sourcing/source_ledger.md` (kind `web`: url, date read, claim, confidence, implication). Then record the query's result below as the ledger IDs it produced.

Rules (the boundary discipline from `01 - writing-department/01 - prompt-library/01 - PROMPT_boundary_research.md`):
- Name the category of every source (survey, practitioner write-up, platform documentation, pricing page, case study). Never write "studies show".
- If you can't find something, write `[VERIFY]`. Never fill the gap with a plausible number.
- When two sources disagree, log both rows and add a line under "Contradictions". Do not pick one silently.
- Aim for at least 3 independent source categories per lane.

When done: set Status to RUN. In `01-foundation/*.md`, replace every `[dossier: D-001 Qn, PENDING]` tag with the `[src: L-nnn]` rows found, or with an honest "not supported" if nothing was found.

## Queries

**Lane L1: buyer situation**
- **Q1.** For founder-led or small businesses (roughly 5–50 staff) selling to other businesses: how many marketing channels do they typically run at once, and who runs them (founder, junior hire, freelancers, agency)? Capture any survey figures with their sample and year.
- **Q2.** What do founders of such businesses describe as the cost of fragmented marketing: inconsistent message, no attribution, time spent, wasted spend? Capture first-person accounts and survey data separately.
- **Q3.** How do small-business owners measure whether marketing "works"? Which reports do they actually read or ignore?
- **Q4.** What share of such businesses have a documented marketing strategy or plan? Capture the source and year.

**Lane L2: buying behaviour**
- **Q5.** How do small B2B businesses hire marketing help (agency, freelancer, fractional CMO, in-house), and what are the reported reasons each engagement ended?
- **Q6.** What proof do founders say most increases their trust in a marketing provider (case studies, referrals, a free audit, a trial, guarantees)?
- **Q7.** How do agencies and consultants structure audit-first offers (free vs paid audit, audit credited toward a retainer)? What conversion from audit to retainer is reported, and by whom?
- **Q8.** Price *norms* only, as context: typical price ranges for a marketing audit and for monthly retainers aimed at small businesses, with source and region. This input never sets the price (I-003).

**Lane L3: alternatives**
- **Q9.** How do agencies, fractional CMOs and "omnichannel marketing" providers describe their offer to small businesses? Collect 5+ positioning statements verbatim, with URLs.
- **Q10.** Which parts of "omnichannel" do small businesses find credible, and which do they read as jargon? Look for reviews, forum threads and practitioner commentary.

**Lane L4: channel facts** (may run any time)
- **Q11.** The current maximum length of a Threads post, from platform documentation (resolves gap G-C03).
- **Q12.** Does LinkedIn reduce the reach of posts with external links in the body? Log each claim with its evidence type (platform statement, controlled test, anecdote). Surface contradictions.
- **Q13.** Current recommended image dimensions and aspect ratios for: a Substack post header, a LinkedIn feed image, an X/Twitter in-feed image, a Threads image, a Facebook feed image. Use platform documentation first. Fills the dimension field in `04 - media-department/VISUAL_BRIEF_CONTRACT.md`.
- **Q14.** Does Medium support canonical links to an original on another domain, and how are they set?

## Results

| Query | Ledger rows | Notes |
|---|---|---|
| Q1–Q14 | — | not run |

## Contradictions

None logged yet.
