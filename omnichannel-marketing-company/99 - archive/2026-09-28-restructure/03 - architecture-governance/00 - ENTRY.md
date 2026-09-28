# ENTRY - Company Architecture Governance

## Parent

Parent: `.\..\00 - ENTRY.md`

This folder holds audits and repairs for Company instruction flow. It is not a company execution cognitive sequence.

## Ancestry

- Parent: `.\..\00 - ENTRY.md`
- Root map: `.\..\..\..\..\02 - WORKSPACE_META\06 - human-readable\CANONICAL_PATHS.md`

## Read Order

1. `..\00 - ENTRY.md`
2. This `ENTRY.md`
3. The named governance report only

## Current Reports

- `function-design-flow-analysis.md` - first-principles entry simulation, discrepancy map, sub-agent contract, raw idea lifecycle, and repair log.

## Promotion Pipeline — Arena to Company

When Arena completes a run with `verdict: pass` and a `promotion_contract` with `engine: "company_promotion"`, the output is eligible for promotion to Company. The promotion path is wired in `finalize_arena_run.py`.

### Artifact Format (What Makes Output Promotable)

A promotable Arena output must satisfy these verifiable assertions:

1. **Validation passed** — `finalize_arena_run.py`'s validation returned `verdict: "pass"` for the applicable mode (prompt_bank_synthesis, textual_frontdoor, or generic).
2. **Run reached terminal state** — state is `converged`, not `needs_correction` or `frozen`.
3. **Content is non-empty** — `output_nonempty` is true, output contains markdown section headings.
4. **No raw source leakage** — `<arena_context_packet`, `<source_excerpt`, and `<Artifact` tags are absent from output (per the Untrusted Output Contract).
5. **Goal alignment** — output addresses the declared research question from the run's REQUEST.json, not an adjacent topic.

Criteria 4 and 5 follow the Arena Untrusted Output Contract at `.\..\..\..\01 - arena\05 - governance\00_UNTRUSTED_OUTPUT_CONTRACT.md`. The evaluation gate is the boundary between Untrusted and Trusted output per Phase 3's definition.

### Promotion Destination

Promoted artifacts land in `06 - promoted-artifacts/` under the Company workspace root. The subfolder is named after the target company (if specified via `promotion_contract.company_name` or `promotion_contract.stage`) or `general/` if no company was targeted. Each promotion creates:

- `PROMOTION-{run_id}.md` — the promotion receipt (metadata, verdict, failures, source path)
- `{artifact_stem}-{run_id}.md` — a durable copy of the promoted output artifact

### Promotion Receipt Format

The receipt records: what was promoted (run_id), when, what the evaluation result was, where the original output lives, and what company it targets. See `06 - promoted-artifacts/` for live receipts and `.\..\..\..\..\02 - WORKSPACE_META\03 - folder-governance\03 - intake-drops\queue\_template-promotion.md` for the template.

### Promotion Gate

If the output fails any of the five criteria above, promotion is blocked. The run's status remains `needs_correction` with a recorded failure reason. The agent must address the failures before re-queuing. No automatic retry — the evaluation gate requires explicit agent action to resolve.

## Write Law

- Write governance reports here.
- Do not move live company artifacts from this folder.
- Do not read generated runs, raw idea payloads, or sibling company content unless a report explicitly names them as required evidence.
- Fix entry, agent, routing, path-token, and packet-header files in place when they cause repeat ambiguity or token-expensive rediscovery.

## Current Reports — Additions (appended 2026-09-25, session S001)

- `INSTRUCTION_GAP_REGISTER.md` — every gap found in the company's instruction files after the relocation: contradictions, broken links, unpropagated doctrine and missing machinery. Each gap has evidence, a class and a next step.
- `EXTERNAL_DEPENDENCY_REGISTER.md` — every CE-workspace system these files reference, with the local substitute to use in this repo. `.\..\00-control\tools\check_links.py` reads it.

## Local Wiring (appended 2026-09-25, session S001)

- This folder now sits inside `omnichannel-marketing-company/`. Parent `.\..\00 - ENTRY.md` is the company ENTRY. Company state: `.\..\00-control\STATE.md`.
- Claims in this folder about CE systems describe the original CE workspace: DEPARTMENT_ROUTER.py ("gap CLOSED"), KSE Gate 8, WORK_AXIOM_BANK, and the Arena promotion pipeline above. None of them runs in this repo. See register rows X-02, X-03, X-05 and X-06.
- Department statuses in `DEPARTMENT_REGISTRY.md` are CE-workspace claims. In this repo, what the company can sell is decided by the capability ledger, which is created in build Phase C (gap G-C09).
