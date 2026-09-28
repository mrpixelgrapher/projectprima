# Channel Activation — which platforms are on, and in what order

Tier 2 (append; update the Activation, Image and Account cells as they change).
Created: 2026-09-28, session S002, from input I-004.
Read by: station S6 (Shape) and S7 (Post) in `00-control/ASSEMBLY_LINE.md`, and by the "Publishes as" binding in `01-foundation/author-voice.md`.

## Rule

Turn on the hub and exactly one spoke. Run one real piece through both. Open the rest only after the pilot exit below holds. [I-004]

## Why the hub is Substack and the first spoke is LinkedIn

This was decided by the existing wiring, not by preference (I-004).

- **Hub = Substack.** Every layer pulls from Substack and never the reverse (`02 - content-distribution/WORKING_RULES.md` Rule 2; source ledger L-005).
- **First spoke = LinkedIn**, for four reasons read off the files:
  1. The 30-day plan pairs LinkedIn with Substack in week 1 (L-005).
  2. The core-insight seed, the first seed any piece yields, maps primarily to LinkedIn (L-005).
  3. LinkedIn is built for the professional decision-maker that the machinery fixed as the buyer (L-002, I-002).
  4. Of the five channels the doctrine requires in every kit, only Substack, LinkedIn and Twitter/X have layer machinery. Website and Medium have none (gap G-M04), and Twitter/X sits in week 2 of the plan.
- **Next spoke after the pilot, by the same wiring:** Twitter/X (week 2, in the doctrine set, layer exists). Then Threads (shares its layer) and Facebook (weeks 2–3). Website and Medium open only once their layer contracts exist (G-M04).

## Channels

| Channel | Role | Layer folder | Activation | Image slots (see `04 - media-department/VISUAL_BRIEF_CONTRACT.md`) | Account / URL | Publishes as |
|---|---|---|---|---|---|---|
| Substack | hub | `02 - content-distribution/01 - substack-hub/` | **ON (pilot)** | featured + inline-N: WAITING-ON-PRODUCER | [CARBON-BLOCKED: F-002 Q4] | the author, per `01-foundation/author-voice.md` |
| LinkedIn | spoke 1 | `02 - content-distribution/02 - linkedin-layer/` | **ON (pilot)** | asset-1: WAITING-ON-PRODUCER | [CARBON-BLOCKED: F-002 Q4] | the author |
| Twitter/X | spoke 2 (next) | `02 - content-distribution/03 - twitter-threads-layer/` | OFF: opens after the pilot exit | twitter-hero: WAITING-ON-PRODUCER once on | — | — |
| Threads | spoke | `02 - content-distribution/03 - twitter-threads-layer/` | OFF | threads-implication: WAITING-ON-PRODUCER once on | — | — |
| Facebook | spoke | `02 - content-distribution/04 - facebook-layer/` | OFF | asset-1: WAITING-ON-PRODUCER once on | — | — |
| Website | conversion layer | none (G-M04) | OFF: no layer contract | — | — | — |
| Medium | spoke | none (G-M04) | OFF: no layer contract | — | — | — |
| Instagram | spoke | none | OFF: no machinery | — | — | — |

**Both pilot channels require an image before their output counts as complete** (L-006). While there is no producer, the pilot can reach *text-complete*, but not *complete*.

## Pilot exit: when the pilot "works" and the next spoke may open

All six conditions must hold, and each is checked on disk:

1. One real piece went through S3 → S8 with no skip-ahead. `python3 00-control/tools/line_status.py` exits 0 and shows the piece at S8 FILLED.
2. The hub article passed writing gates 1–7, and the LinkedIn variant passed the per-variant gate (`02 - content-distribution/05 - templates/decomposition-checklist.md`).
3. Every image slot of the pair is ATTACHED. **Or** the operator has decided in writing to post with a slot still waiting, and that decision is logged in `02-sourcing/input_registry.md` and in the kit's `partial_publication.yaml`. Both contracts make the image mandatory, so relaxing that is the operator's call, not the line's.
4. Both live URLs are recorded in the drafts' `metadata.json`.
5. The piece's `RECORD.md` says what happened: what shipped, when, and what response came back.
6. The operator decides to open the next spoke. That is a human decision, logged in `02-sourcing/input_registry.md`.

Engagement thresholds are deliberately not set here. The measurable objective belongs to `05-convergence/` (gap G-M09).

## Partial publication

The doctrine (`03 - architecture-governance/02 - doctrine-enforcement/OMNICHANNEL_ENFORCEMENT.md` Rule 4) requires a stated reason whenever a piece ships to fewer channels than the full set. The pilot ships to two of the doctrine's five channels by design, so every pilot kit carries `PUBLISH_KIT/partial_publication.yaml` (gap G-D06, decided S002):

    partial_publication:
      artifact: [slug]
      channels_shipped: [substack, linkedin]
      channels_skipped: [website, medium, twitter-x]
      reason: "hub + one-spoke pilot per operator directive I-004 (2026-09-28); website and medium have no layer contract (G-M04)"
      waiting_images: [every brief ID still WAITING-ON-PRODUCER, or none]

## Where things live

- Working area, one folder per layer: `drafts/[slug]/` (each layer's `OUTPUT_CONTRACT.md`).
- Paste-ready output, one folder per piece: `02 - content-distribution/06 - publish-kits/[slug]/PUBLISH_KIT/` (gap G-C08, decided S002). The author posts from here.
