# STATE — Omnichannel Marketing Company

Tier 3: rewrite freely at the end of every session. Last written: 2026-09-25, session S001.
Read after `manifest.json` and `00-control/status.md` (company `00 - ENTRY.md` → Company Map → Cold-boot order).

## The 30-second answer

- **What exists.** A business thesis (`00-control/status.md`), a placeholder foundation (`01-foundation/`), and stub outputs (`03-setup/01 - outputs/`). Alongside them sit three substantive but unexercised methodology folders: `01 - writing-department/`, `02 - content-distribution/`, `03 - architecture-governance/`. Since S001 these are all wired together inside this folder, with two operators in `00-control/tools/`.
- **What state it is in.** Derived phase **1, FOUNDATION ACTIVE** (`00-control/PHASE_DERIVATION.md`; the manifest previously claimed 3). Nothing has been exercised end to end. Buyer-facing work is **BLOCKED** (`00-control/execute.md` operator). Four human answers are pending in `00-control/carbon-input/CARBON_INPUT_FORM-001.md`.
- **What runs next.** Build Phase B as one package: run research dossier D-001 and make the foundation evidence-backed. The exact steps are below.

## Next action (one package: build Phase B, "foundation that is not placeholder")

Class: **agent-executable** (web research) + **CE-actionable** (writing and tagging). It does not wait on F-001; claims that depend on its answers are tagged `[CARBON-BLOCKED: F-001 Qn]`.

Scope (P15): files to write — `02-sourcing/research_plan.md`, `02-sourcing/input_registry.md`, `02-sourcing/source_ledger.md`, `02-sourcing/01 - dossiers/D-001-buyer-and-problem/DOSSIER.md`, the three `01-foundation/*.md`, `05-convergence/{objective_function,evaluation_log,convergence_status}.md`, `00-control/contracts/RESEARCH_DOSSIER_CONTRACT.md`. Verify with `derive_phase.py`.

1. Archive the current placeholder text of `01-foundation/customer.md`, `problem.md` and `value-proposition.md` to `01-foundation/META/archive/2026-09-25-placeholder/`, recording date, reason and source path (handoff P17).
2. Write `02-sourcing/research_plan.md`: the research brief plus a **lane map**, because parallel research is legal only after one exists (handoff §2.4). Proposed lanes: L1 the buyer segment and its pains with fragmented channels; L2 how that buyer purchases marketing (audits, retainers, what they tried); L3 competing offers (agencies, fractional CMOs, omnichannel retainers); L4 channel facts the instructions depend on (e.g. the Threads length limit, gap G-C03).
3. Write `02-sourcing/01 - dossiers/D-001-buyer-and-problem/DOSSIER.md`: numbered, self-contained, runnable queries per lane. Use the boundary discipline of `01 - writing-department/01 - prompt-library/01 - PROMPT_boundary_research.md`: named source categories, `[VERIFY]` instead of invention, and contradictions surfaced.
4. Run the queries. Log every source in `02-sourcing/source_ledger.md` as a table row: `ID · url/path · date · claim · confidence · implication`.
5. Write `02-sourcing/input_registry.md`: every human input (F-001 Q1–Q4 and their status) and the three open questions in `02-sourcing/question_bank.md`.
6. Rewrite the three foundation files. Each gets a `## Claims` section in which **every bullet** carries `[src: L-nnn]`, `[dossier: D-001 Qn]` or `[CARBON-BLOCKED: F-001 Qn]`. The operator enforces this.
7. Make `05-convergence/objective_function.md` measurable (target metric, current value, convergence threshold, evaluation method), and create `evaluation_log.md` and `convergence_status.md`.
8. Only after D-001 has run, derive `00-control/contracts/RESEARCH_DOSSIER_CONTRACT.md` from the dossier's actual shape (Build Order Law: instance first).
9. Verify: `python3 00-control/tools/derive_phase.py`. Expected result is phase 2 (CAPABILITY OS BUILDING), with all phase-1 minimums PASS. Then `--write-manifest`, update `PHASE_DERIVATION.md`, update this file, and log in `meta_workspace.md` §3.

After Phase B: build Phase C (capability cards and ledger in `06 - capability/`). Then the first real article, which is where gaps G-C05, G-C07, G-M02 and G-X04 get decided.

## Blocked on human

| Form | Questions | Status | Unblocks |
|---|---|---|---|
| `00-control/carbon-input/CARBON_INPUT_FORM-001.md` | Q1 friend's role · Q2 first real buyer · Q3 offer and price · Q4 live channels and publishing name | OPEN | foundation claims tagged CARBON-BLOCKED; the author voice; the channel matrix; the client ledger |
| CARBON_INPUT_FORM-002 (queued, not staged) | author voiceprint samples · public proof permissions | QUEUED until F-001 is answered | writing Stage 04; proof assets |

## What is real and what is placeholder

| Path | Verdict |
|---|---|
| `00-control/status.md` | Real, at thesis level (one line per field) |
| `00-control/asset-intake.md`, `00-control/work-choices.md` | Redundant restatements of `status.md`. Kept, not relied on (gap G-M08) |
| `00-control/execute.md` | Gate with an operator since S001. Result: BLOCKED |
| `01-foundation/*.md`, `01-foundation/META/slot-map.md` | Placeholder. No evidence, no `## Claims` |
| `02-sourcing/question_bank.md` | 3 real questions. No plan, registry, ledger or dossier |
| `03-setup/01 - outputs/P1…P4` | Stubs, **invalid** under the knowledge-work override (`00-control/PHASE_DERIVATION.md`) |
| `04-interface/execution-sequence.md` | A plan, not exercised |
| `05-convergence/objective_function.md` | Placeholder, not measurable |
| `01 - writing-department/` | Substantive, not exercised: 0 research folders, no voiceprint |
| `02 - content-distribution/` | Substantive, not exercised: 0 drafts, 0 publish kits. No website or Medium layer |
| `03 - architecture-governance/` | Substantive. Now also holds the two registers written in S001 |

## Handoff §7.3 gap list, checked against disk

| # | Handoff gap | Verdict on 2026-09-25 |
|---|---|---|
| 1 | No capability ledger or cards | VERIFIED open. Build Phase C |
| 2 | No dossiers or source ledger | VERIFIED open. Next action above |
| 3 | No intake form, work packet, delivery packet or service ledger | VERIFIED open. Build Phase E |
| 4 | No quality thresholds, QA checklist or review report | VERIFIED open for business deliverables. Articles have gates 1–7 in `01 - writing-department/OUTPUT_CONTRACT.md` (gate 7 added in S001). Build Phase E |
| 5 | No client ledger or upgrade rules | VERIFIED open. Build Phase F |
| 6 | No readiness dashboard, drift checks, lessons or pattern register | VERIFIED open. `meta_workspace.md` §5 holds pattern candidates until `13 - memory/` exists |
| 7 | Convergence objective not measurable | VERIFIED open. Next action, step 7 |
| 8 | Foundation files are placeholders | VERIFIED open. 1 of 8 phase-1 minimums now passes (F-001) |
| 9 | `execute.md` has no operator | **CLOSED in S001.** Operator appended |
| 10 | No single index across scaffold and departments | **CLOSED in S001.** Company Map in `00 - ENTRY.md`; departments moved inside and linked |

Instruction-level gaps (55 in total) are tracked in `03 - architecture-governance/INSTRUCTION_GAP_REGISTER.md`: 18 fixed, 13 registered or resolved, 17 open, 7 waiting on a human.

## Verify this file (the regeneration instructions)

    python3 00-control/tools/derive_phase.py   # must print derived phase 1; exit 0 (manifest agrees)
    python3 00-control/tools/check_links.py    # must print RESULT: PASS (0 broken, 0 unregistered)

If either disagrees with this file, the operator wins. Rewrite this file from its output and log the drift in `meta_workspace.md` §3.
