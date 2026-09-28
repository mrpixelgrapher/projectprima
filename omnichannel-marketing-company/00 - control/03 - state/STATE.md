# STATE — Omnichannel Marketing Company

Tier 3: rewrite freely at the end of every session. Last written: 2026-09-28, session S003 (after the design lock).
Read after `00 - ENTRY.md`. Then run `python3 "00 - control/02 - tools/task.py" status`.

## The 30-second answer

- **What this is.** Three departments that take a vague client request to paid, monthly, organic omnichannel content: `01 - commercial/` (intake, scope, pricing, proposal, billing, month review), `02 - content/` (discovery, strategy, performance, planning, writing, packaging, publishing, delivery), `03 - video-factory/` (script, shots, stills, motion, edit plan). A task moves one node at a time along a route (`00 - control/01 - law/ROUTES.md`: engagement, month, and direct for runs without commercials); each client has a permanent folder in `clients/`. The design is the operator's, locked in `00 - control/04 - source-intent/06 - operator-directives-2026-09-28-design-lock.md`.
- **Where it stands.** **Skeleton built and verified.** Every department, node and stage has its instruction; `task.py` moves tasks along every route; each route was run end to end on a scratch copy through the real node ENTRYs. No task has been run for a client yet.
- **Company phase.** **2, CAPABILITY OS BUILDING** (`00 - control/03 - state/PHASE_DERIVATION.md`): built, not yet exercised. The first real delivered task moves it.
- **What runs next.** The rehearsal of both sample requests on the direct route (no commercials, I-013), then the depth package it informs (below). Nothing is blocked on the operator.

## What is built (S003)

| Part | State | Where |
|---|---|---|
| Law | Built: task contract, routes, hand-offs (client, operator, ARENA, image factory, motion), 13 brief slots, instruction standard, the two doctrines | `00 - control/01 - law/` |
| Tools | Built and fixture-tested: `task.py` (new, status, check, advance, advance --to, hold, resume, close); `check_links.py` (strict); `derive_phase.py` (remapped) | `00 - control/02 - tools/` |
| Commercial | Built: 7 nodes, 28 stages, ledgers, effort table, billing profile (empty) | `01 - commercial/` |
| Content | Built: 8 nodes, 47 stages, 14 sub-stages (writing: 10 stages, 3 research sub-stages, 11 channel folders) | `02 - content/` |
| Video factory | Built: 5 nodes, 13 stages | `03 - video-factory/` |
| Client folder | Template built | `clients/00 - template/` |
| Past material | Archived whole, with a map of where each part went | `99 - archive/00 - ENTRY.md` |

## Blocked on the operator

Nothing. The operator ruled that the commercial side is not a block and is not needed for this run (I-013). The billing profile, rates and payment are needed only when a real client runs on the engagement or month route; the direct route skips them.

## Standing interpretations (the operator may correct any time; none blocks work)

| What | Where |
|---|---|
| The image factory's root was given as `.CE\…`, read as `D:\ROOT\CE\…` | `00 - control/01 - law/HANDOFFS.md` (H4) |
| On the engagement and month routes, content work starts after the advance invoice is paid (D-31) | `01 - commercial/06 - billing-advance/02 - payment/` |
| The cadence and effort tables are starting estimates, corrected by delivery lessons (D-32) | `01 - commercial/02 - scope/` |

## Next action

1. **Rehearsal (running).** Both sample requests are open as rehearsal tasks on the **direct** route, and hold at intake for the client's round-1 answers (`python3 "00 - control/02 - tools/task.py" status`):
   - `T-20260928-gemstones-corporate-gifts`: questions in `01 - commercial/01 - intake/work/T-20260928-gemstones-corporate-gifts/11-intake/04-questions-round-1-for-client.md`
   - `T-20260928-performance-marketer-xyz`: questions in `01 - commercial/01 - intake/work/T-20260928-performance-marketer-xyz/11-intake/04-questions-round-1-for-client.md`

   To carry a rehearsal on, anyone can answer as the client: paste the answers into the task's `from-client/11-intake-questions-round-1-reply.md`, then `task.py resume`, and intake stage 5 continues.
2. **The depth package,** informed by what the rehearsal shows:
   1. **Channel crafts in depth,** one reference per channel folder in `02 - content/05 - writing/06 - channels/`: what performs on that platform, formats, a hook library, examples, the full self-check.
   2. **Creator sampling and top-post breakdowns:** how to judge each of the six dimensions (hook, structure, angle, funnel mechanics, cadence, visual), step by step (`02 - content/01 - discovery/03 - creators/`, `02 - content/05 - writing/01 - research/`).
   3. **Neuromarketing and virality references** for `02 - content/03 - performance/`: each principle with examples per channel and its honesty line.
   4. **Research method:** how to write an ARENA request that makes a complicated topic simple, and how to read a dossier into a boundary map.
   5. **Video craft:** shot grammar, Nano Banana scene prompting, cinematic motion prompting, stop-motion (`03 - video-factory/`).
3. **Later, when a real client is priced:** a worked proposal and invoice template (`01 - commercial/`).

## Named gaps (the phase ladder's NOT BUILT minimums)

Authority claims, public-proof rules, rollback rules (pausing or reducing an engagement), drift checks, a readiness dashboard. None is needed before the first client; each is named in `PHASE_DERIVATION.md`.

## Verify this file

    python3 "00 - control/02 - tools/check_links.py"    # PASS
    python3 "00 - control/02 - tools/derive_phase.py"   # phase 2; exit 0
    python3 "00 - control/02 - tools/task.py" status    # two rehearsal tasks, HOLD at intake
