# Source Ledger

Tier 2: append rows only; never edit a logged claim. If a source is later contradicted, add a new row and name the contradiction.
Log format (handoff §2.4): url/path · date · claim · confidence · implication.
Created: 2026-09-28, session S002. Claim files cite rows as `[src: L-nnn]`.

**Kinds of source**
- `disk`: a file in this repo, read in full on the date given. It is evidence of what the line **is built to do**, never evidence about the market.
- `web`: an external source, logged when dossier D-001 runs. There are none yet.

## Ledger

| ID | Kind | url / path | Date read | Claim (what the source says) | Confidence | Implication |
|---|---|---|---|---|---|---|
| L-001 | disk | `00-control/status.md` | 2026-09-25 | The company's recorded thesis: the leverage actor is a "founder or revenue lead buying retained growth execution"; the buyer path is friend referral → audit → strategy call → retained execution; the offer is an omnichannel marketing system | high that this is what the file records; **none** as market evidence | A thesis to test, not a finding |
| L-002 | disk | `02 - content-distribution/02 - linkedin-layer/WORKFLOW.md` | 2026-09-28 | LinkedIn is built as "B2B thought-leadership" for "executives / clients / recruiters / decision-makers"; posts must be referenceable in "client acquisition … business development" | high | The line's professional channel assumes a business decision-maker as reader |
| L-003 | disk | `02 - content-distribution/04 - facebook-layer/OUTPUT_CONTRACT.md` | 2026-09-28 | The `persona` enum is mature-reader, approaching-retirement-professional, business-owner, investor, high-income-segment. There is no consumer or entertainment persona | high | Even the broad-reach channel was poured for business readers; `business-owner` is available as-is |
| L-004 | disk | `03 - architecture-governance/02 - doctrine-enforcement/OMNICHANNEL_ENFORCEMENT.md` | 2026-09-28 | Website = "where retainers get signed"; LinkedIn = "where legal/B2B buyers actually look"; Substack = owned email list | high | The website and email channels are built to convert professional buyers |
| L-005 | disk | `02 - content-distribution/MULTI_PLATFORM_ARCHITECTURE.md` | 2026-09-28 | Hub-and-spoke, one-way flow from Substack. 30-day plan: week 1 = "LinkedIn (main derivative) + Substack (canonical)". Core-insight seed → LinkedIn primary | high | The wiring puts LinkedIn first among the spokes |
| L-006 | disk | `02 - content-distribution/01 - substack-hub/OUTPUT_CONTRACT.md` check 5; `02 - content-distribution/02 - linkedin-layer/OUTPUT_CONTRACT.md` check 5; `02 - content-distribution/03 - twitter-threads-layer/OUTPUT_CONTRACT.md` check 10; `02 - content-distribution/04 - facebook-layer/OUTPUT_CONTRACT.md` check 6; `02 - content-distribution/WORKING_RULES.md` Rule 6 | 2026-09-28 | Every channel, including the hub, requires a custom Media-produced image before its output counts as complete | high | With no producer, no channel can reach "complete". The hub + LinkedIn pilot is image-blocked too |
| L-007 | disk | `00-control/source-intent/01 - CLOUD_AI_HANDOFF.md` §2.5 | 2026-09-28 | Capability promotion: validated = ran once end to end on real input; live = run at least twice and reconciled; only `live_capability` may be marketed, "unless explicitly framed as staged" | high | A paid run 2 after one proof run must be sold framed as validated (proven once), not as an established service |
| L-008 | disk | `00-control/PHASE_DERIVATION.md` | 2026-09-28 | Zero units have been exercised: 0 research folders, 0 drafts, 0 publish kits, 0 ledgers | high | Nothing on this line is proven yet, so nothing can be sold yet |
| L-009 | disk | `01 - writing-department/01 - prompt-library/00 - WIRING_MANIFEST.md`; `01 - writing-department/01 - prompt-library/04 - PROMPT_voice_humanization.md` | 2026-09-28 | The writing chain's input is "topic + author name (+ 3-5 writing samples for voiceprint)". Stage 04 requires `voiceprints/[author].md`; "no piece humanizes toward 'human in general'" | high | The author's identity and samples are hard inputs. No file ever held them |
| L-010 | disk | `02 - content-distribution/02 - linkedin-layer/OUTPUT_CONTRACT.md`; `03 - architecture-governance/MULTI_VERTICAL_CONTENT_OS.md` | 2026-09-28 | The vertical lists default to the earlier project (law, arbitration, litigation, consulting). LinkedIn allows `general` for posts outside those verticals | high | The platform folders can take this company's identity without being rebuilt |
