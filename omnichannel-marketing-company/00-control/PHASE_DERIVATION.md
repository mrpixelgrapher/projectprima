# Phase Derivation

Tier 3 report: regenerate freely. Derived: 2026-09-25, session S001.
Operator: `python3 00-control/tools/derive_phase.py`. If this file and the script disagree, the script wins and this file is stale.

## Verdict

| | Phase | Label | Source |
|---|---|---|---|
| Claimed (before S001) | 3 | FORGE IN PROGRESS | `manifest.json` as uploaded (kept under `phase_previous_claim`) |
| **Derived** | **1** | **FOUNDATION ACTIVE** | `derive_phase.py`, table below |

**Downgraded by 2 phases.** Under the anti-inflation law (handoff §3.1), a claimed phase is invalid while any lower phase's minimum is missing. `manifest.json` now carries phase 1. The script writes it (`--write-manifest`), so don't hand-edit the phase fields.

"FORGE IN PROGRESS" is not a label on the Phase Map. It named a CE build cell, not a readiness level.

## Why 1: the judgment the script cannot make

- **Not phase 0.** Phase 0's trigger is "cannot state its service thesis and buyer path from files". `00-control/status.md` does state them, at thesis level: offer, buyer path, leverage actor, proof structure. The company is past phase 0.
- **Phase 1's trigger matches.** "Core business logic exists but capability / acquisition / delivery / research structures are not represented by governed artifacts." The departments hold real, governed methodology, but none of it has been run for this company. Nothing on disk turns it into capability cards, a pipeline, an intake or a delivery record (verified: 0 `research-*` folders, 0 `drafts/` folders, 0 `PUBLISH_KIT/` folders, 0 ledgers).
- **Phase 1 cannot exit.** 7 of its 8 minimums fail: the three foundation files carry no evidence-tagged claims, and the research plan, input registry, source ledger and any dossier are all missing. The one that passes is the carbon input form, `00-control/carbon-input/CARBON_INPUT_FORM-001.md`, staged this session.
- **Why the old claim of 3 was invalid.** Every phase-2 minimum is missing (capability cards, promotion gates, validation-run template, capability ledger), and so is every phase-3 minimum (pipeline ledger, sequence rules, proof system, authority claims, public-proof rules, compiler contract).

## Per-phase exit minimums (script output, 2026-09-25)

| Phase | Exit minimum | Result | Missing |
|---|---|---|---|
| 0 UNINITIALIZED | company manifest | PASS |  |
| 0 UNINITIALIZED | service thesis | PASS |  |
| 0 UNINITIALIZED | buyer map | PASS |  |
| 0 UNINITIALIZED | initial system rules | PASS |  |
| 1 FOUNDATION ACTIVE | foundation: customer, evidence-tagged | FAIL | `01-foundation/customer.md` has no `## Claims` section |
| 1 FOUNDATION ACTIVE | foundation: problem, evidence-tagged | FAIL | `01-foundation/problem.md` has no `## Claims` section |
| 1 FOUNDATION ACTIVE | foundation: value proposition, evidence-tagged | FAIL | `01-foundation/value-proposition.md` has no `## Claims` section |
| 1 FOUNDATION ACTIVE | source packet: research plan | FAIL | missing `02-sourcing/research_plan.md` |
| 1 FOUNDATION ACTIVE | source packet: input registry | FAIL | missing `02-sourcing/input_registry.md` |
| 1 FOUNDATION ACTIVE | source packet: source ledger (>= 1 row) | FAIL | missing `02-sourcing/source_ledger.md` |
| 1 FOUNDATION ACTIVE | source packet: >= 1 research dossier | FAIL | missing `02-sourcing/01 - dossiers` |
| 1 FOUNDATION ACTIVE | source packet: >= 1 carbon input form | PASS |  |
| 2 CAPABILITY OS BUILDING | capability cards | FAIL | missing `06 - capability/cards` |
| 2 CAPABILITY OS BUILDING | promotion gates | FAIL | missing `06 - capability/promotion-gates.md` |
| 2 CAPABILITY OS BUILDING | validation-run template | FAIL | missing `06 - capability/validation-run-template.md` |
| 2 CAPABILITY OS BUILDING | capability ledger (>= 1 row) | FAIL | missing `06 - capability/capability-ledger.md` |
| 3 ACQUISITION AND PROOF BUILDING | pipeline ledger | FAIL | missing `07 - acquisition/pipeline-ledger.md` |
| 3 ACQUISITION AND PROOF BUILDING | cognitive sequence rules | FAIL | missing `07 - acquisition/sequence-rules.md` |
| 3 ACQUISITION AND PROOF BUILDING | proof system index | FAIL | missing `08 - proof/00 - INDEX.md` |
| 3 ACQUISITION AND PROOF BUILDING | authority claims | FAIL | missing `08 - proof/authority-claims.md` |
| 3 ACQUISITION AND PROOF BUILDING | public-proof rules | FAIL | missing `08 - proof/public-proof-rules.md` |
| 3 ACQUISITION AND PROOF BUILDING | compiler contract | FAIL | missing `00-control/contracts/COMPILER_CONTRACT.md` |
| 4 DELIVERY AND QUALITY BUILDING | intake form · work packet · delivery packet · service ledger · quality thresholds · QA checklist · review report | FAIL (all 7) | `09 - delivery/` and `10 - quality/` do not exist |
| 5 CLIENT AND UPGRADE BUILDING | client ledger · client template · upgrade rules with thresholds · rollback rules · upgrade brief template | FAIL (all 5) | `11 - client-state/` and `12 - upgrade/` do not exist |
| 6 GOVERNANCE INSTALLED | lessons · patterns-to-promote · drift checks · readiness dashboard | FAIL (4) | `13 - memory/` and `14 - governance/` do not exist |
| 6 GOVERNANCE INSTALLED | phase map | FAIL at first run, PASS once this file exists | `00-control/PHASE_DERIVATION.md` (this file) |
| 6 GOVERNANCE INSTALLED | exercised matter · exercised quality/proof disposition | FAIL | not machine-checked until a ledger schema exists; nothing has been exercised |
| 7 GOVERNED LOOP EXERCISED | loop · transition · governance refresh | FAIL (all 3) | nothing has been exercised |
| 8 LIVE GOVERNED OPERATION | repeated proof · every sequence exercised · no overclaim | FAIL (all 3) | nothing has been exercised |

Phases 4–8 are condensed here; run the script for the row-by-row output. Where the handoff named no folder, the paths come from the gate table in the script (decision D-04, `meta_workspace.md`).

## Knowledge-work override: NOT SATISFIED

This company runs on external research and prompt-derived compilation, so the override applies (handoff §3). None of its three contracts exist: research-dossier, compiler, handoff (`00-control/contracts/`). Consequence: **`03-setup/01 - outputs/` P1–P4 (positioning, pitch stack, website surface, channel copy) are invalid as current-state positioning**, and so is any market-facing claim. They are stubs to be recompiled from dossiers, not drafts to be polished.

## Other claims audited this session

| Claim | Where | Verdict | Evidence |
|---|---|---|---|
| "Generated attempt, not a live company" | `00 - ENTRY.md` | **Confirmed.** Stays true until derived phase 8 | this file |
| Active folder `forge-folder` / `active_cell: forge-cell` | `00 - ENTRY.md`, `manifest.json` | **Unresolved.** No such folder exists (`find -iname '*forge*'` → 0) | gap G-C15 |
| Media Department COMPLETE | `03 - architecture-governance/DEPARTMENT_REGISTRY.md` | **Unverifiable here.** Not in this repo | register X-04 |
| Writing Department ACTIVE | registry; `01 - writing-department/00 - ENTRY.md` | **Built, not exercised.** 0 research folders; no voiceprint | gap G-C09 |
| Content Distribution ACTIVE | registry; `02 - content-distribution/00 - ENTRY.md` | **Built, not exercised.** 0 drafts, 0 publish kits | gap G-C09 |
| Law OPERATIONAL | registry | **Unverifiable here** | register X-12 |
| Department-router gap "CLOSED" | `03 - architecture-governance/DEPARTMENT_FIRST_BUSINESS_MODEL.md` | **Not true in this repo.** The script is external | gap G-X06 |
| `execute.md` gate | `00-control/execute.md` | **Was not a gate** (no operator, handoff §2.7). Operator added in S001: result BLOCKED | gap G-M07 |
| Departments are linked | the three department folders | **Verified.** `check_links.py`: 0 broken, 0 unregistered | `00-control/tools/check_links.py` |

## Regeneration

1. `python3 00-control/tools/derive_phase.py`. If the derived phase changed, add `--write-manifest`.
2. Replace the Verdict and per-phase table with the new output, and update "Why" if the triggers changed.
3. Log the change in `meta_workspace.md` §3.
