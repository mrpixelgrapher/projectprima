# Offer — what is sold, and in what order

Station **S2 (need)** in `00-control/ASSEMBLY_LINE.md`.
Created: 2026-09-28, session S002, from input I-003.
Gate operator: `python3 00-control/tools/derive_phase.py`, section "Paid-offer gate".

## Claims

- The rule: nothing is sold until it has been made once, checked once and delivered once, all the way through the line. [src: I-003]
- No unit has been through the line yet, so today nothing is sellable. [src: L-008]
- Unit 1 is the free proof run **PR-001**: the first audit, done for one real buyer at no charge. Its only purpose is the proof file `08 - proof/PR-001-proof-run.md`. [src: I-003] Recipient: the buyer named in `01-foundation/customer.md`. [CARBON-BLOCKED: F-002 Q3]
- The proof file must record six things: the request; what was made; the check result (review report); confirmation of delivery; what the run cost, in time and effort per station; and the buyer's response. It ends with `Disposition: PROVEN`, `PARTIAL` or `NOT PROVEN`. [src: I-003, L-007]
- The paid audit opens only when PR-001 says `Disposition: PROVEN`. [src: I-003] Its price is set by the friend against the cost recorded in PR-001. [DEFERRED: price, until PR-001 is PROVEN, per I-003]
- The first paid audit is sold as validated: delivered once, proof available on request. It is not sold as an established service. It becomes `live_capability`, and can be marketed openly, only after a second delivery has been reconciled. [src: L-007] This reconciles "paid after one proven run" (I-003) with the capability promotion law.
- The retainer ("retained execution") comes after the audit is live. [src: I-003, L-001] Its contents and price: [DEFERRED: retainer, until the paid audit is live, per I-003]
