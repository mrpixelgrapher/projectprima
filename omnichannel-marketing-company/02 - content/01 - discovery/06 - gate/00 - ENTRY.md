# 06 · Gate

**Purpose:** decide whether the brief is fit for strategy. If it is, carry its essentials forward, publish the client's brief, creator library and voice to their folder, and advance.

## Contract

- **Reads:** every file in `21-discovery/` and `from-client/`.
- **Writes:** the `## 21-discovery` section of `CONTEXT.md`; `21-discovery/gate.md`; `clients/<client>/brief.md`, `creators.md`, `voice.md`.
- **Done when:** `gate.md` says `VERDICT: PASS`, the three client files are published, and the task has advanced.

## Procedure

1. **Run the checks in order.** Stop at the first failure and go back to the stage named.

   | # | Check | On failure |
   |---|---|---|
   | D1 | Every request in `01-requests.md` has returned, and every client question is mapped | 01 - requests (hold again if a return is missing) |
   | D2 | SPEAKER, BRAND, OFFER, BUYER, GOAL, CHANNELS, LIMITS, EXECUTION, LANGUAGE and VOICE are Known (or Assumed and shown to the client) | 01 - requests (next client round) |
   | D3 | Every RQ has a finding or a route; every ledger row has seven fields; every contradiction is listed | 02 - findings |
   | D4 | Every channel in the engagement has creators and six pattern cards, each pattern on 2+ posts from 2+ creators | 03 - creators |
   | D5 | The voiceprint has six evidenced dimensions, its basis and its confidence | 04 - voice |
   | D6 | Every line of the brief is cited; its open items hold nothing needed at intake or discovery | 05 - brief |

2. **Write the carry-forward** (at most 10 bullets, each with its source):

       ## 21-discovery
       - Buyer A: <one line>; decides: …; buys: … [21-discovery/07-client-brief.md]
       - Offer: <one line> [client]
       - Proof in hand: … · asserted only: … [21-discovery/07-client-brief.md]
       - Market: main alternatives …; openings: … [src: L-…]
       - Creator patterns that matter most: <channel: pattern>, … [21-discovery/05-creator-library.md]
       - Limits: budget …, timeline …, rules … [21-discovery/07-client-brief.md]
       - Voice: basis …, the tell … [21-discovery/06-voiceprint.md]
       - Open for later nodes: … [21-discovery/07-client-brief.md]

3. **Publish to the client folder** (move any existing file to `clients/<client>/versions/<file>-<YYYY-MM-DD>.md` first): `07-client-brief.md` → `brief.md`; `05-creator-library.md` → `creators.md`; `06-voiceprint.md` → `voice.md`.
4. **Write `gate.md`** (the five-line format in `00 - control/01 - law/TASK_CONTRACT.md` §2), then run `python3 "00 - control/02 - tools/task.py" advance <task-id>`.

## Self-check

- [ ] Were the checks run in order?
- [ ] Is the carry-forward ≤ 10 bullets, each with a source?
- [ ] Do the three client files match the task files they were copied from?

## Traps

- **Passing with a hollow buyer.** D2 fails if BUYER is still "companies".
- **Publishing before passing.** The client folder only ever holds files a gate passed.
