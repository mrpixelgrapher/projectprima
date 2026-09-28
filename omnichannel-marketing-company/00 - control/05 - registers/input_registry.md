# Input Registry — human inputs

Tier 2: append rows and update Status cells only.
Purpose: every fact or ruling that came from a person, not from research, gets an ID here. Claim files cite it as `[src: I-nnn]`. Research sources live in `02-sourcing/source_ledger.md` (`[src: L-nnn]`).
Created: 2026-09-28, session S002.

## Inputs received

| ID | Date | From | Input (summary; verbatim text in the source file) | Source file | Answers | Lands in | Status |
|---|---|---|---|---|---|---|---|
| I-001 | 2026-09-28 | operator | The friend is the author: the person whose expertise and voice every piece is produced in. Not a client | `00-control/source-intent/03 - operator-directives-2026-09-28.md` ¶2 | F-001 Q1 (role) | `01-foundation/author-voice.md` | ACCEPTED. Name, field and voice still open → F-002 Q1, Q2 |
| I-002 | 2026-09-28 | operator | Buyer type is already fixed by what's built: a founder or small-business owner making a professional decision, not a consumer. One real, named buyer is still missing and must not be invented | same, ¶3 | F-001 Q2 (type) | `01-foundation/customer.md` | ACCEPTED. The specific buyer is open → F-002 Q3 |
| I-003 | 2026-09-28 | operator | Nothing is sold before it has been made, checked and delivered once. The first unit through the line is free, and its purpose is the proof file. Only then does a paid version open, priced against what run 1 actually cost. The price is the friend's decision | same, ¶4 | F-001 Q3 (sequence) | `01-foundation/offer.md` | ACCEPTED. Price is deliberately deferred until the proof run exists |
| I-004 | 2026-09-28 | operator | Turn on the hub and exactly one spoke; run one real piece through both; open the rest only after that works. The order is set by the wiring. Handles and URLs are the friend's to supply | same, ¶5 | F-001 Q4 (order) | `02 - content-distribution/CHANNEL_ACTIVATION.md` | ACCEPTED. Handles open → F-002 Q4 |
| I-005 | 2026-09-28 | operator | No image producer exists. Mark each image-dependent platform as waiting, never fake or skip it, and build the image station's infrastructure so that a producer, when it arrives, knows what to extract and make | same, ¶6 | gap G-X04 | `04 - media-department/` | ACCEPTED |
| I-006 | 2026-09-28 | operator | The first piece in a new topic is excused from the link-back rule; later pieces follow it normally | same, ¶6 | gap G-C05 | `02 - content-distribution/01 - substack-hub/OUTPUT_CONTRACT.md`, `02 - content-distribution/01 - substack-hub/WORKFLOW.md`, `01 - writing-department/BLOG_AS_KNOWLEDGE_PRODUCTION.md` | ACCEPTED. See S002 note on piece 2 in `03 - architecture-governance/INSTRUCTION_GAP_REGISTER.md` |
| I-007 | 2026-09-28 | operator | The folder structure is one assembly line. Each folder does one job, and nothing runs in a later folder while an earlier one is empty or half-filled | same, ¶1 | — | `00-control/ASSEMBLY_LINE.md`, `00-control/tools/line_status.py` | ACCEPTED |

## Still open (asked in `00-control/carbon-input/CARBON_INPUT_FORM-002.md`)

| Needed | Why it can't be researched | Form |
|---|---|---|
| The friend's real name, field (specialty) and publishing name | Only the friend knows who they are and what they're expert in | F-002 Q1 |
| 3–5 samples of the friend's own writing | The voice stage writes toward one real person's voice, never "human in general" | F-002 Q2 |
| One real buyer: name (or anonymised label), industry, size, what they already tried | A made-up buyer would poison every file that reads `customer.md` | F-002 Q3 |
| Hub (Substack) and spoke (LinkedIn) URLs / handles | Accounts belong to the friend | F-002 Q4 |

## Deliberately deferred (not asked yet)

| Needed | Deferred until | Why |
|---|---|---|
| Price of the paid audit; retainer price and contents | `08 - proof/PR-001-proof-run.md` records the cost of run 1 | I-003: priced against what the first run actually cost |
| Which results, names and numbers may be published as proof | the proof run exists | There is nothing to grant permission for yet |

## Questions from `02-sourcing/question_bank.md`

| Question | Routed to |
|---|---|
| What proof most increases trust for the buyer? | D-001 lane L2 (research) + the proof run PR-001 (evidence) |
| Which part of the buyer path stalls first? | D-001 lane L2 |
| How should referral-led audits and owned media be sequenced? | Answered by I-003 + I-004: proof run first, then hub + one spoke |
