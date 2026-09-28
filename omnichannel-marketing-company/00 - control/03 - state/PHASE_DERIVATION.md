# Phase Derivation

Tier 3 report: regenerate freely. Last derived: 2026-09-28, session S003, after the design lock.
Operator: `python3 "00 - control/02 - tools/derive_phase.py"`. If this file and the script disagree, the script wins and this file is stale.

## Verdict

| When | Claimed | Derived | Note |
|---|---|---|---|
| Before S001 | 3, FORGE IN PROGRESS | — | an inherited label (kept in `manifest.json` under `phase_previous_claim`) |
| S001, 2026-09-25 | — | 1, FOUNDATION ACTIVE | 7 of 8 phase-1 minimums missing |
| S002, 2026-09-28 | — | 2, CAPABILITY OS BUILDING | all phase-1 minimums passed on the S002 structure |
| **S003, 2026-09-28** | — | **2, CAPABILITY OS BUILDING** | the gate table remapped onto the v2 structure; the first failing minimum is a delivery-ledger row |

`manifest.json` carries phase 2, written by the script (`--write-manifest`).

## How the phase map was remapped (S003, decision D-30)

The handoff's phase map (§3, Tier 1) names minimums for a company shaped around capability cards, an acquisition system and upgrade rules. At the design lock the operator said that ladder "was for the pricing and offer, upselling thing" and chose to map it onto the pricing department. So:

- **Foundation (phase 1)** is the law every task obeys and the nodes that name every missing input: the task contract, routes, brief slots, hand-offs, every node built, intake's client questions, discovery's ARENA request.
- **Capability, pipeline, client and upgrade minimums (phases 2, 3, 5)** are read from the ledgers: `02 - content/08 - delivery/ledgers/delivery-ledger.md` (the capability ledger), `01 - commercial/ledgers/proposals.md` (the pipeline), `clients.md` (the client ledger), and the upsell stage (upgrade rules).
- **Exercised minimums (phases 6–8)** are now checked by the script against real finished tasks in `clients/*/done/`: a real DONE task, one with a review PASS, one on each route. Rehearsal tasks never count.
- **Minimums with no artifact** are reported as NOT BUILT, by name: authority claims, public-proof rules, rollback rules, drift checks, a readiness dashboard.

## Why 2, and what moves it

Phase 1 exits: the whole line exists and names what it needs. Phase 2 fails at one minimum: **no real task has been delivered**, so the delivery ledger has no real row. That is the honest state: the company is built, not yet exercised. The first real client task that reaches `02 - content/08 - delivery/02 - record/` writes that row.

## Script output (2026-09-28)

## Exit minimum per phase (first FAIL = derived phase)

| Phase | Exit minimum | Result | Missing |
|---|---|---|---|
| 0 UNINITIALIZED | company manifest | PASS |  |
| 0 UNINITIALIZED | service thesis | PASS |  |
| 0 UNINITIALIZED | buyer map | PASS |  |
| 0 UNINITIALIZED | initial system rules | PASS |  |
| 1 FOUNDATION ACTIVE | foundation: task contract | PASS |  |
| 1 FOUNDATION ACTIVE | foundation: routes | PASS |  |
| 1 FOUNDATION ACTIVE | foundation: brief slots | PASS |  |
| 1 FOUNDATION ACTIVE | foundation: every node on every route BUILT | PASS |  |
| 1 FOUNDATION ACTIVE | source packets: intake names every missing input (client questions) | PASS |  |
| 1 FOUNDATION ACTIVE | source packets: research is staged as an ARENA request | PASS |  |
| 1 FOUNDATION ACTIVE | source packets: hand-off law (client, operator, ARENA, image factory, motion) | PASS |  |
| 1 FOUNDATION ACTIVE | source packets: input registry (>= 1 row) | PASS |  |
| 2 CAPABILITY OS BUILDING | capability cards: every node declares its outputs and its gate | PASS |  |
| 2 CAPABILITY OS BUILDING | promotion gates: proposal sign-off and acceptance | PASS |  |
| 2 CAPABILITY OS BUILDING | validation-run template: the delivery record | PASS |  |
| 2 CAPABILITY OS BUILDING | capability ledger: delivery ledger (>= 1 real row) | FAIL | `02 - content/08 - delivery/ledgers/delivery-ledger.md` has 0 of >= 1 real row(s) |
| 3 ACQUISITION AND PROOF BUILDING | pipeline ledger: proposals (>= 1 real row) | FAIL | `01 - commercial/ledgers/proposals.md` has 0 of >= 1 real row(s) |
| 3 ACQUISITION AND PROOF BUILDING | cognitive sequence rules: routes | PASS |  |
| 3 ACQUISITION AND PROOF BUILDING | proof system: client results (>= 1 real month) | FAIL | 0 of >= 1 real DONE task(s) holding `15-month-review/02-review.md` |
| 3 ACQUISITION AND PROOF BUILDING | authority claims | FAIL | NOT BUILT: no file states the company's own public claims and their evidence |
| 3 ACQUISITION AND PROOF BUILDING | public-proof rules | FAIL | NOT BUILT: no rule for when a client result may be shown publicly |
| 3 ACQUISITION AND PROOF BUILDING | compiler contract: research compiled into a spine | PASS |  |
| 4 DELIVERY AND QUALITY BUILDING | intake form | PASS |  |
| 4 DELIVERY AND QUALITY BUILDING | work packet: the piece brief | PASS |  |
| 4 DELIVERY AND QUALITY BUILDING | delivery packet: the client package | PASS |  |
| 4 DELIVERY AND QUALITY BUILDING | service ledger: delivery ledger | PASS |  |
| 4 DELIVERY AND QUALITY BUILDING | quality thresholds: the review gate prompt | PASS |  |
| 4 DELIVERY AND QUALITY BUILDING | QA checklist: the human check | PASS |  |
| 4 DELIVERY AND QUALITY BUILDING | review report (>= 1 completed, in a real task) | FAIL | 0 of >= 1 real DONE task(s) holding `25-writing/*/07-review.md` |
| 5 CLIENT AND UPGRADE BUILDING | client ledger (>= 1 real row) | FAIL | `01 - commercial/ledgers/clients.md` has 0 of >= 1 real row(s) |
| 5 CLIENT AND UPGRADE BUILDING | client template | PASS |  |
| 5 CLIENT AND UPGRADE BUILDING | upgrade rules with thresholds: upsell triggers | PASS |  |
| 5 CLIENT AND UPGRADE BUILDING | rollback rules | FAIL | NOT BUILT: no rule for pausing or reducing an engagement |
| 5 CLIENT AND UPGRADE BUILDING | upgrade brief template: the upsell offer | PASS |  |
| 6 GOVERNANCE INSTALLED | lessons | PASS |  |
| 6 GOVERNANCE INSTALLED | patterns-to-promote: the promotion rule | PASS |  |
| 6 GOVERNANCE INSTALLED | drift checks | FAIL | NOT BUILT: no check compares what the company says, sells and has delivered |
| 6 GOVERNANCE INSTALLED | readiness dashboard | FAIL | NOT BUILT: `task.py status` shows tasks, not readiness |
| 6 GOVERNANCE INSTALLED | phase map | PASS |  |
| 6 GOVERNANCE INSTALLED | exercised matter: a real task DONE | FAIL | 0 of >= 1 real DONE task(s) in `clients/*/done/` |
| 6 GOVERNANCE INSTALLED | exercised quality/proof disposition: a real task DONE with a review PASS | FAIL | 0 of >= 1 real DONE task(s) holding `25-writing/*/07-review.md` |
| 7 GOVERNED LOOP EXERCISED | matter moved through delivery and quality disposition | FAIL | 0 of >= 1 real DONE task(s) holding `28-delivery/02-record.md` |
| 7 GOVERNED LOOP EXERCISED | client transition backed by a named artifact: client ledger | FAIL | `01 - commercial/ledgers/clients.md` has 0 of >= 1 real row(s) |
| 7 GOVERNED LOOP EXERCISED | governance refresh after the loop | FAIL | NOT-MACHINE-CHECKED: needs a judgment across an exercised loop |
| 8 LIVE GOVERNED OPERATION | repeated proof: >= 2 real tasks DONE | FAIL | 0 of >= 2 real DONE task(s) in `clients/*/done/` |
| 8 LIVE GOVERNED OPERATION | an exercised loop for every route: engagement | FAIL | 0 of >= 1 real DONE task(s) on route engagement in `clients/*/done/` |
| 8 LIVE GOVERNED OPERATION | an exercised loop for every route: month | FAIL | 0 of >= 1 real DONE task(s) on route month in `clients/*/done/` |
| 8 LIVE GOVERNED OPERATION | readiness dashboard with no open overclaim | FAIL | NOT-MACHINE-CHECKED: needs a judgment across an exercised loop |

## Knowledge-work override

- research-dossier contract (the ARENA request and dossier): PASS
- compiler contract (the spine): PASS
- handoff contract (task contract and hand-offs): PASS

Override: SATISFIED

## Commercial readiness

- billing profile filled: FAIL - `01 - commercial/billing-profile.md` empty: Legal name, Trading name (as shown to clients), Address, Tax registration (e.g. GSTIN), if any, Payment details (bank / UPI / payment link)

Invoices: HOLD at billing until the operator fills `01 - commercial/billing-profile.md`
