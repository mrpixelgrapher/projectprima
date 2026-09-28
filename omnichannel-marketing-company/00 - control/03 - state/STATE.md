# STATE — Omnichannel Marketing Company

Tier 3: rewrite freely at the end of every session. Last written: 2026-09-28, session S003 (after the design lock).
Read after `00 - ENTRY.md`. Then run `python3 "00 - control/02 - tools/task.py" status`.

## The 30-second answer

- **What this is.** Three departments that take a vague client request to paid, monthly, organic omnichannel content: `01 - commercial/` (intake, scope, pricing, proposal, billing, month review), `02 - content/` (discovery, strategy, performance, planning, writing, packaging, publishing, delivery), `03 - video-factory/` (script, shots, stills, motion, edit plan). A task moves one node at a time along a route (`00 - control/01 - law/ROUTES.md`); each client has a permanent folder in `clients/`. The design is the operator's, locked in `00 - control/04 - source-intent/06 - operator-directives-2026-09-28-design-lock.md`.
- **Where it stands.** **Skeleton built and verified.** Every department, node and stage has its instruction; `task.py` moves tasks along both routes; both routes were run end to end on a scratch copy through the real node ENTRYs. No task has been run for a client yet.
- **Company phase.** **2, CAPABILITY OS BUILDING** (`00 - control/03 - state/PHASE_DERIVATION.md`): built, not yet exercised. The first real delivered task moves it.
- **What runs next.** The operator reviews the skeleton; then the depth package (below).

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

| # | What | Why it matters | Where |
|---|---|---|---|
| 1 | Review the skeleton | The operator ordered "skeleton, then depth" | this session's report |
| 2 | Fill the billing profile (legal name, trading name, address, tax registration, payment details) | Every invoice prints it; billing holds until it is filled | `01 - commercial/billing-profile.md` |
| 3 | Confirm the image factory's root: the path was given as `.CE\…`, read as `D:\ROOT\CE\…` | Stills are delivered there | `00 - control/01 - law/HANDOFFS.md` (H4) |
| 4 | Confirm that content work starts only after the advance invoice is paid (decision D-31, read from "setup upfront. 50% monthly advance") | It decides when discovery starts | `01 - commercial/06 - billing-advance/02 - payment/` |
| 5 | Rates per kind of work, per client | Asked at each client's pricing, not now | `01 - commercial/03 - pricing/01 - rates/` |

## Next action: the depth package (after the review)

The skeleton's stage instructions are complete, but several stages point to knowledge that deserves its own reference files. In order:

1. **Channel crafts in depth,** one reference per channel folder in `02 - content/05 - writing/06 - channels/`: what performs on that platform, formats, a hook library, examples, the full self-check.
2. **Creator sampling and top-post breakdowns:** how to judge each of the six dimensions (hook, structure, angle, funnel mechanics, cadence, visual), step by step (`02 - content/01 - discovery/03 - creators/`, `02 - content/05 - writing/01 - research/`).
3. **Neuromarketing and virality references** for `02 - content/03 - performance/`: each principle with examples per channel and its honesty line.
4. **Research method:** how to write an ARENA request that makes a complicated topic simple, and how to read a dossier into a boundary map.
5. **Video craft:** shot grammar, Nano Banana scene prompting, cinematic motion prompting, stop-motion (`03 - video-factory/`).
6. **Commercial templates:** a worked proposal and invoice.
7. **Rehearsal:** run both sample requests (`gemstones-corporate-gifts`, `performance-marketer-xyz`) through intake as `--kind rehearsal`, and fix what the run shows.

## Named gaps (the phase ladder's NOT BUILT minimums)

Authority claims, public-proof rules, rollback rules (pausing or reducing an engagement), drift checks, a readiness dashboard. None is needed before the first client; each is named in `PHASE_DERIVATION.md`.

## Verify this file

    python3 "00 - control/02 - tools/check_links.py"    # PASS
    python3 "00 - control/02 - tools/derive_phase.py"   # phase 2; exit 0
    python3 "00 - control/02 - tools/task.py" status    # no tasks
