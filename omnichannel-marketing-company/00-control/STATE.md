# STATE — Omnichannel Marketing Company

Tier 3: rewrite freely at the end of every session. Last written: 2026-09-28, session S002.
Read after `manifest.json` and `00-control/status.md` (company `00 - ENTRY.md` → Company Map → Cold-boot order).

## The 30-second answer

- **What this is.** One assembly line on disk (`00-control/ASSEMBLY_LINE.md`). A request enters at S0; stations S1 (who) and S2 (need) set up the company; each piece or client job then runs S3 plan → S4 write → S5 check → S6 shape → S7 post → S8 record. The three methodology departments plus a new image station (`04 - media-department/`) do the unit-level work.
- **Where the line stands.** **Stuck at S1.** The voice file (`01-foundation/author-voice.md`) has the role decided (the friend is the author) but no name, field or writing samples. The buyer file (`01-foundation/customer.md`) has the type fixed (founder or small-business owner) but no real buyer. Nothing downstream may start (`python3 00-control/tools/line_status.py`).
- **Company phase.** **2, CAPABILITY OS BUILDING** (`00-control/PHASE_DERIVATION.md`). Every gap is now named and staged, which is phase 1's exit. It is not the same as the line moving: see the table in that file.
- **What runs next.** The friend fills F-002 (the send unit below). In parallel, an agent runs research lanes L1 and L4, then Phase C (capability cards).

## The send unit (one sitting, for the friend)

`00-control/carbon-input/CARBON_INPUT_FORM-002.md`, about 20–30 minutes:
- Q1: name, field, what your expertise rests on.
- Q2: 3–5 samples of your own writing.
- Q3: one real buyer, and whether they've agreed to a free audit.
- Q4: Substack and LinkedIn accounts.

Answering Q1–Q3 is what un-sticks the line.

## Next actions, in line order

| # | Class | Action | Allowed now? | Done when |
|---|---|---|---|---|
| 1 | human | The friend completes `00-control/carbon-input/CARBON_INPUT_FORM-002.md` | yes | answers logged as I-nnn in `02-sourcing/input_registry.md` |
| 2 | agent-executable | Run D-001 **lane L1** (Q1–Q4, buyer situation: station S1b's own research) and **lane L4** (Q11–Q14, channel facts). Log every source in `02-sourcing/source_ledger.md`; replace the `[dossier: D-001 Q1–Q4, PENDING]` tag in `01-foundation/customer.md`; fill the `format` guidance in `04 - media-department/VISUAL_BRIEF_CONTRACT.md` from Q13; resolve gap G-C03 from Q11 | yes (research plan: L1 belongs to S1b, L4 feeds instructions only) | D-001 L1 and L4 rows logged; `line_status.py` no longer lists D-001 Q1–Q4 under S1b |
| 3 | CE-actionable | Build Phase C: one capability card per capability (research, long-form writing, platform decomposition, visual production, distribution, reporting, audit delivery), each honestly at `raw_fragment` (nothing has run), plus promotion gates, a validation-run template and `06 - capability/capability-ledger.md` | yes: it describes the line and produces no content | `derive_phase.py` shows the phase-2 minimums PASS |
| 4 | agent + human | Once F-002 is answered: move the answers into `## Claims` (`[src: I-nnn]`); run Stage 04 Part A on the samples → `01 - writing-department/voiceprints/[author-slug].md` | after #1 | `line_status.py`: S1a and S1b FILLED |
| 5 | agent-executable | Run D-001 **lanes L2–L3** (Q5–Q10) → fill `01-foundation/problem.md` and `value-proposition.md` | after S1 is FILLED | S2 FILLED |
| 6 | both | The two first runs: **PR-001** (the free audit for the named buyer → `08 - proof/PR-001-proof-run.md`) and the **pilot piece** (hub + LinkedIn; exit rules in `02 - content-distribution/CHANNEL_ACTIVATION.md`) | after S2 is FILLED | PR-001 disposition recorded; the pilot passes its exit |

## Decisions ahead (not blocking yet; needed before the pilot reaches S7)

Every channel, both pilot channels included, requires an image, and there is no producer (`04 - media-department/00 - ENTRY.md`). Before the pilot posts, the operator chooses one of three options:
- **(a) Approve an in-repo SVG producer** for diagram-class images: frameworks and flows, which cover most pilot slots. Writing `04 - media-department/PRODUCER.md` switches the station on for that class.
- **(b) Bring a human designer or an image tool**, for any class.
- **(c) Post the pilot with image slots still waiting**, logged as a partial publication. The contracts make the image mandatory, so this relaxation is the operator's call only.

## Station status (`line_status.py`, 2026-09-28)

| Station | Status | Waiting on |
|---|---|---|
| S0 Intake | FILLED | — |
| S1a Who: voice | PARTIAL | F-002 Q1 (name, field), F-002 Q2 (samples) |
| S1b Who: buyer | PARTIAL | F-002 Q3 (real buyer), D-001 Q1–Q4 (lane L1) |
| S2 Need | PARTIAL | D-001 Q2, Q3, Q5, Q6, Q9–Q10; F-002 Q3 |
| S3–S8 | EMPTY | no unit may start until S0–S2 are FILLED |
| M Media (side) | NOT OPERATIONAL | no `04 - media-department/PRODUCER.md` |
| Deferred by rule (not blocking) | — | price and retainer until PR-001 / live audit (I-003); relief evidence until PR-001 |

## Blocked on human

| Form | Status | What's open |
|---|---|---|
| `00-control/carbon-input/CARBON_INPUT_FORM-001.md` | PARTIALLY ANSWERED (S002) | nothing new: its open facts moved to F-002 |
| `00-control/carbon-input/CARBON_INPUT_FORM-002.md` | OPEN | Q1 name and field · Q2 writing samples · Q3 one real buyer · Q4 accounts |
| deferred by rule | — | prices (after PR-001), proof permissions (after PR-001) |

## What is real and what is placeholder

| Path | Verdict |
|---|---|
| `00-control/status.md`, `00-control/source-intent/` | real |
| `00-control/asset-intake.md`, `work-choices.md`, `01-foundation/META/slot-map.md` | redundant restatements; no station reads them (gap G-M08) |
| `01-foundation/author-voice.md`, `customer.md`, `problem.md`, `value-proposition.md`, `offer.md` | real claim files; PARTIAL, and every gap is tagged |
| `02-sourcing/` | real: input registry (I-001–I-007), source ledger (L-001–L-010, disk evidence only), research plan, D-001 staged |
| `03-setup/01 - outputs/P1…P4` | stubs, **invalid** until the knowledge-work override is satisfied |
| `04-interface/execution-sequence.md` | superseded for ordering (S002) |
| `05-convergence/objective_function.md` | placeholder, not measurable (gap G-M09) |
| `01 - writing-department/`, `02 - content-distribution/` | substantive, not exercised; now bound to `author-voice.md` and `CHANNEL_ACTIVATION.md` |
| `04 - media-department/` | intake built; NOT OPERATIONAL |

Instruction-level gaps: `03 - architecture-governance/INSTRUCTION_GAP_REGISTER.md` has 64 in total (28 fixed, 16 registered or resolved, 14 open, 6 human).

## Verify this file

    python3 00-control/tools/line_status.py    # stuck at S1a/S1b; exit 0 (no skip-ahead)
    python3 00-control/tools/derive_phase.py   # phase 2; exit 0 (manifest agrees)
    python3 00-control/tools/check_links.py    # RESULT: PASS

If any of them disagrees with this file, the operator wins. Rewrite this file from its output and log the drift in `meta_workspace.md` §3.
