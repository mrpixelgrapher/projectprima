# Execute

Read `00-control/asset-intake.md` before any buyer-facing work.
Do not proceed if any required slot is unresolved.

## Operator (appended 2026-09-25, session S001)

The two lines above describe a gate with no operator, and by handoff §2.7 that is not a gate. This section adds the operator and the verification path. The rule itself is unchanged.

- Operator: `python3 00-control/tools/derive_phase.py`, section "Buyer-facing gate".
- A slot counts as resolved only when it traces to evidence. Having text in it is not enough:
  1. the foundation claims carry evidence tags (`01-foundation/*.md`, section `## Claims`);
  2. the knowledge-work override contracts exist, so positioning is compiled, not drafted (`00-control/contracts/`);
  3. the capability ledger has at least one `live_capability` row, so nothing unproven is marketed (handoff §2.5).
- Result on 2026-09-25: **BLOCKED**, all three fail. `asset-intake.md` has text in every slot, but it is the same thesis text repeated for three surfaces, not intake evidence.
