# Assembly Line

Tier 2 (append rows and sections; the station table is read by `00-control/tools/line_status.py`). Created: 2026-09-28, session S002, from input I-007.

## The law

The whole folder structure is one assembly line on disk. A vague request drops in at the first station. Each station does **one job** and passes what it made to the next. Every station reads from the stations before it, so:

1. **Nothing runs at a later station while an earlier station is EMPTY or PARTIAL.**
   - Inside a unit of work, any output at a later station while an earlier one is not FILLED is a skip-ahead violation (e.g. a draft before the spine, a kit before the gate).
   - Company stations (S0–S2) hold the operator's rulings plus named gaps, so a PARTIAL company station is honest, not a skip. It is a violation only if a company station is FILLED while an earlier one is not.
2. **No unit of work (article or client deliverable) may start until every company station (S0–S2) is FILLED.**
3. **Waiting is written down, never implied.** A station that can't finish carries a `[CARBON-BLOCKED: …]`, `[WAITING: …]` or `[dossier: …, PENDING]` marker naming exactly what it waits on. Silence is never read as completion.
4. **A deliberate deferral is not waiting.** Some items are scheduled by an explicit rule to happen after a later event. The price, for example, is set only after the proof run (I-003). These carry `[DEFERRED: until <event>, per I-nnn]`. They are listed by the operator but do not hold the station back; otherwise the price would block S2 and S2 would block the very proof run that sets the price. A DEFERRED marker that cites no `I-nnn` or `L-nnn` rule counts as waiting.
5. **A station's own research is part of its job.** Research that a station reads (e.g. D-001 lane L1 for S1b) runs as part of that station, not after it.

Operator: `python3 00-control/tools/line_status.py`. It prints every station's status and where the line stands. It exits 1 on any skip-ahead violation.

## Stations

The operator reads this table. `[root]` is the unit's own folder; `[slug]` is the unit's name.

| ID | Station | One job | Unit | Writes (checked by the operator) | Reads from |
|---|---|---|---|---|---|
| S0 | Intake | Capture the request verbatim | company | `00-control/source-intent/` | — |
| S1a | Who: voice | Say whose voice this is: real name, field, way of talking | company | `01-foundation/author-voice.md` | S0 |
| S1b | Who: buyer | Say who it is for: the buyer type, plus one real buyer | company | `01-foundation/customer.md` | S0 |
| S2 | Need | Say what the buyer needs, the mechanism of relief, and what is offered in what order | company | `01-foundation/problem.md`, `01-foundation/value-proposition.md`, `01-foundation/offer.md` | S1a, S1b, `02-sourcing/` |
| S3 | Plan | Research the topic's full boundary, then build the spine (stages 01–02) | piece | `[root]/sources/`, `[root]/observations/`, `[root]/synthesis/SPINE.md` | S1a (field), S2 |
| S4 | Write | Draft from the spine, then voice it toward the author (stages 03–04) | piece | `[root]/outputs/DRAFT.md`, `[root]/outputs/ARTICLE.md` | S3; S1a voiceprint |
| S5 | Check | Gate the piece: PASS, or FAIL back to a named station (stage 05) | piece | `[root]/outputs/GATE.md` | S4 |
| S6 | Shape | Produce the hub version, one variant per active spoke, and one visual brief per image slot | piece | `02 - content-distribution/01 - substack-hub/drafts/[slug]/decomposition-seeds.md`, `02 - content-distribution/02 - linkedin-layer/drafts/[slug]/post.md`, `04 - media-department/01 - requests/[slug]/` | S5; `02 - content-distribution/CHANNEL_ACTIVATION.md` |
| S7 | Post | Assemble a paste-ready kit; the author posts it; the URLs are recorded | piece | `02 - content-distribution/06 - publish-kits/[slug]/PUBLISH_KIT/` | S6; side station M |
| S8 | Record | Write down what happened | piece | `[root]/RECORD.md` | S7 |
| M | Media (side station) | Turn visual briefs into verified images | side | `04 - media-department/PRODUCER.md` | S6 briefs |

S6 lists the pilot pair only: the hub, plus LinkedIn (`02 - content-distribution/CHANNEL_ACTIVATION.md`). When another spoke opens, append its variant path to the S6 cell. That is a path addition, not a rewrite.

## How the operator judges a station

| Written path | FILLED when | PARTIAL when | EMPTY when |
|---|---|---|---|
| a file in `01-foundation/` | it has `## Claims`, and no bullet carries a waiting marker (cited `[DEFERRED: …]` markers are allowed) | some bullets carry `[CARBON-BLOCKED`, `[WAITING`, `PENDING]` or an uncited `[DEFERRED` | missing, or no `## Claims` bullets |
| a folder (ends in `/`) | it holds at least one file | — | missing or empty |
| `GATE.md` | it contains `VERDICT: PASS` | it exists without a PASS | missing |
| any other file | it exists | — | missing |

A station's status is the worst status among its paths. S7 is capped at PARTIAL while side station M has no producer: every active channel's contract makes the image mandatory (`02-sourcing/source_ledger.md` L-006), so no kit can be complete without one.

## Units of work

| Unit kind | Folder (`[root]`) | Stations it passes through | Notes |
|---|---|---|---|
| Content piece | `01 - writing-department/03 - research/research-[slug]/` | S3 → S8 | Decided S002 (gap G-C07). The folder is permanent (writing Rule 2) |
| Client unit (e.g. an audit) | `09 - delivery/[unit-id]/` | the same jobs: S6 shapes for the client, S7 delivers, S8 writes the proof file `08 - proof/[unit-id]-proof-run.md` for a proof run | Station file names are fixed at the first instance, PR-001 (Build Order Law) |

The same stations serve both kinds, and each unit carries the handoff's work contract (§4): S0 is INTAKE; S1–S2 plus the unit's research are ORIENTATION; S3–S6 are WORKING; S7 is OUTPUT; S8 is STATE.

## The two first runs

| Run | Unit | What it proves | Opens |
|---|---|---|---|
| Pilot piece | the first content piece, through the hub and exactly one spoke (LinkedIn) | the content line works end to end on one pair | the next spoke (`02 - content-distribution/CHANNEL_ACTIVATION.md`) |
| PR-001 proof run | the first audit, free, for the one real buyer | the service line works: made, checked, delivered once | the paid audit (`01-foundation/offer.md`) |

Neither run can start until S0–S2 are FILLED.

## Where the line stands

Run the operator. The status at the time of writing is recorded in `00-control/STATE.md`.
