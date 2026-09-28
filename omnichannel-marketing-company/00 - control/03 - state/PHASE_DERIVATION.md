# Phase Derivation

Tier 3 report: regenerate freely. Last derived: 2026-09-28, session S002.
Operator: `python3 00-control/tools/derive_phase.py`. If this file and the script disagree, the script wins and this file is stale.

## Verdict

| When | Claimed | Derived | Note |
|---|---|---|---|
| Before S001 | 3, FORGE IN PROGRESS | — | an inherited label (kept in `manifest.json` under `phase_previous_claim`) |
| S001, 2026-09-25 | — | 1, FOUNDATION ACTIVE | 7 of 8 phase-1 minimums missing |
| **S002, 2026-09-28** | — | **2, CAPABILITY OS BUILDING** | all 10 phase-1 minimums PASS; the first phase-2 minimum fails |

`manifest.json` carries phase 2. It was written by the script (`--write-manifest`); don't hand-edit it.

## Phase 2 does not mean the line is moving

Two operators measure two different things, and both are true today:

| Operator | Question | Answer on 2026-09-28 |
|---|---|---|
| `derive_phase.py` | Has the company **named** everything it is missing, and staged a packet for each gap? (Phase 1's exit: "foundation artifacts + named source packets for missing proof and inputs") | **Yes.** Every foundation claim carries evidence or a named waiting marker. Research dossier D-001 is staged and forms F-001 and F-002 exist, so phase 1 exits |
| `line_status.py` | Has each early station actually been **filled**? | **No.** The line is stuck at S1 (who: voice, and who: buyer), waiting on the friend (F-002) and on research lane L1 (`00-control/ASSEMBLY_LINE.md`) |

Naming a gap is what phase 1 requires; filling it is what the line requires. Phase 2's work (capability cards, promotion gates, capability ledger) describes what the line can and cannot do yet. It produces no content, so it can proceed without skipping ahead on the line.

## Why 2: the judgment the script cannot make

- **Phase 1 exits honestly.** Every tag was checked by hand as well as by script:
  - `[src: …]` tags point at real rows in `02-sourcing/source_ledger.md` (L-001 to L-010, on-disk evidence only) or `02-sourcing/input_registry.md` (I-001 to I-007, the operator's rulings).
  - `[CARBON-BLOCKED: F-002 Qn]` tags point at questions staged in `00-control/carbon-input/CARBON_INPUT_FORM-002.md`.
  - `[dossier: D-001 Qn, PENDING]` tags point at queries written in `02-sourcing/01 - dossiers/D-001-buyer-and-problem/DOSSIER.md`.
  - `[DEFERRED: …, per I-003]` tags point at the operator's ordering rule.
  - No claim is asserted without one of these.
- **Phase 2 fails at its first minimum.** No capability cards, no promotion gates, no validation-run template, no capability ledger.
- **The source ledger contains no market evidence yet.** All ten rows are `disk` sources: evidence of what the line is *built* to do, not of what buyers need. That is why S2 (need) stays PARTIAL on the line.

## Per-phase exit minimums (script output, 2026-09-28)

| Phase | Exit minimum | Result | Missing |
|---|---|---|---|
| 0 UNINITIALIZED | manifest · service thesis · buyer map · initial system rules | PASS (all 4) | |
| 1 FOUNDATION ACTIVE | foundation: customer, problem, value proposition, author voice, offer (evidence-tagged) | PASS (all 5) | |
| 1 FOUNDATION ACTIVE | source packets: research plan · input registry · source ledger (≥ 1 row) · ≥ 1 dossier · ≥ 1 carbon input form | PASS (all 5) | |
| 2 CAPABILITY OS BUILDING | capability cards | FAIL | `06 - capability/cards` |
| 2 CAPABILITY OS BUILDING | promotion gates | FAIL | `06 - capability/promotion-gates.md` |
| 2 CAPABILITY OS BUILDING | validation-run template | FAIL | `06 - capability/validation-run-template.md` |
| 2 CAPABILITY OS BUILDING | capability ledger (≥ 1 row) | FAIL | `06 - capability/capability-ledger.md` |
| 3 ACQUISITION AND PROOF BUILDING | pipeline ledger · sequence rules · proof index · authority claims · public-proof rules · compiler contract | FAIL (all 6) | `07 - acquisition/`, `08 - proof/`, `00-control/contracts/COMPILER_CONTRACT.md` |
| 4–5 | delivery, quality, client and upgrade artifacts | FAIL | `09 - delivery/` to `12 - upgrade/` |
| 6 | lessons · patterns · drift checks · dashboard | FAIL | `13 - memory/`, `14 - governance/` |
| 6 | phase map | PASS | this file |
| 6–8 | every exercised-loop requirement | FAIL | nothing has been exercised |

Run the script for the row-by-row output.

## Gates

| Gate | Operator section | Result | Why |
|---|---|---|---|
| Knowledge-work override | "Knowledge-work override" | NOT SATISFIED | None of the three contracts exist (`00-control/contracts/`). `03-setup/01 - outputs/` P1–P4 stay invalid |
| Buyer-facing assets (`00-control/execute.md`) | "Buyer-facing gate" | BLOCKED | Foundation now PASS; override contracts and any `live_capability` row are missing |
| Paid offer (`01-foundation/offer.md`) | "Paid-offer gate" | CLOSED | `08 - proof/PR-001-proof-run.md` does not exist. The first unit is the free proof run |

## Other claims audited (carried from S001; any change noted)

| Claim | Verdict |
|---|---|
| "Generated attempt, not a live company" (`00 - ENTRY.md`) | Confirmed. It stays true until derived phase 8 |
| `forge-folder` / `forge-cell` labels | Unresolved (gap G-C15) |
| Writing and Content Distribution "ACTIVE" | Built, not exercised: 0 pieces, 0 drafts, 0 kits |
| Media "COMPLETE" | Refers to the CE workspace. **Here:** `04 - media-department/` exists as intake only and is NOT OPERATIONAL (S002) |
| Departments linked | Verified: `check_links.py` reports 0 broken and 0 unregistered |

## Regeneration

1. Run `python3 00-control/tools/derive_phase.py`. If the phase changed, add `--write-manifest`.
2. Run `python3 00-control/tools/line_status.py` and keep the phase-vs-line table above current.
3. Log the change in `meta_workspace.md` §3.
