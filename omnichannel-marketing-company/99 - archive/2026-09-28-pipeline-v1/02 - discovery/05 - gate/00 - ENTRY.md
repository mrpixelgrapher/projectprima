# 05 · Gate

**Purpose:** decide whether the brief is fit for strategy. If it is, carry its essentials forward and float the task. If client answers are missing, hold, and say exactly what is being waited for.

## Contract

- **Reads:** every file in `02-discovery/` and `client/`.
- **Writes:** the `## 02 - discovery` section of `CONTEXT.md`; `02-discovery/gate.md`; the `waiting on` field in `TASK.md`.
- **Done when:** `gate.md` says `VERDICT: PASS` and `task.py advance` has moved the task, **or** it says `VERDICT: HOLD` and `waiting on` names the outstanding items.

## Procedure

1. **Run the checks in order.** Stop at the first failure.

   | # | Check | On failure |
   |---|---|---|
   | D1 | Every CQ sent is logged in `client/answers-round-N.md`, as answered or not answered | stage 1 |
   | D2 | SPEAKER, BRAND, OFFER, BUYER, VOICE (the samples), LIMITS and EXECUTION are Known, or Assumed and shown to the client | round 2 out → **HOLD**; otherwise stage 1 |
   | D3 | F1, F2 and F4 have values (F1 may be TO STRATEGY only after a "not sure" answer) | stage 1 |
   | D4 | Every runnable RQ has a finding, or "not found" with where you searched | stage 2 |
   | D5 | Every ledger row has all six fields; every contradiction is listed | stage 2 |
   | D6 | The voiceprint has six evidenced dimensions, its source and its confidence | stage 3 |
   | D7 | Every line of the brief is cited; its open items hold nothing needed at 02 | stage 4 |

2. **On a PASS, write the carry-forward:** at most 10 bullets, each with its source.

       ## 02 - discovery
       - Frame: F1 …, F2 …, F4 …; package: … [02-discovery/01-slot-board.md]
       - Buyer A: <one line>; decides: …; buys: … [02-discovery/05-client-brief.md]
       - Offer: <one line> [client]
       - Proof in hand: … · asserted only: … [02-discovery/05-client-brief.md]
       - Market: main alternatives … [src: L-…]
       - Limits: budget …, timeline …, rules … [02-discovery/05-client-brief.md]
       - Voice: source …, the tell … [02-discovery/04-voiceprint.md]
       - Open for later nodes: … [02-discovery/05-client-brief.md]

3. **Write `gate.md`** (the five-line format in `00 - control/01 - law/TASK_CONTRACT.md` §2): the verdict, the first failed check, the stage to return to, `Waiting on:`, and notes for 03 - strategy.
4. **Set `waiting on` in `TASK.md`.** On a PASS, run `python3 "00 - control/02 - tools/task.py" advance <task-id>`. On a HOLD caused by round 2, send `01-round-2-questions.md` (unless the task is a rehearsal). When the answers arrive, rerun from stage 1 with N+1.

## Self-check

- [ ] Were the checks run in order?
- [ ] Is the carry-forward ≤ 10 bullets, each with a source?
- [ ] On a HOLD, does `waiting on` name exact CQ numbers?

## Traps

- **Passing with a hollow buyer.** D2 fails if BUYER is still "companies".
- **Holding on items later nodes need.** Only items needed at 02 justify a HOLD.
