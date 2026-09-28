# Visual Brief Contract

Tier 2. Created: 2026-09-28, session S002 (input I-005).
This contract defines how an article turns into image requests, and how a render counts as done. It is the full intake side of the image station, written so that a producer arriving later needs nothing else.

## 1. Image slots per channel

The slots come from the layer contracts, not from taste. Only channels that are ON in `02 - content-distribution/CHANNEL_ACTIVATION.md` get briefs. During the pilot that means the Substack hub and LinkedIn.

| Channel | Slot | The producer writes | Required by | Seed it draws on | What the image must do |
|---|---|---|---|---|---|
| Substack (hub) | `featured` | `02 - content-distribution/01 - substack-hub/drafts/[slug]/visual-assets/featured.png` | hub contract §1 and check 5 | 6, visual concept | Make the article's one thing visible at a glance |
| Substack (hub) | `inline-N`, one per graphic slot in the article | `…/visual-assets/inline-N.png` | writing contract: minimum 2 custom graphics per article; gate G4 checks the graphic slots | 4, framework, or the slot's own claim | Compress the concept at that point in the argument |
| LinkedIn | `asset-1` | `02 - content-distribution/02 - linkedin-layer/drafts/[slug]/visual-assets/asset-1.png` | LinkedIn contract §3 and check 5 | 4, framework | Framework diagram, before/after, or data visualisation (LinkedIn template). Professional-credibility register; no meme style |
| Twitter/X | `twitter-hero` | `02 - content-distribution/03 - twitter-threads-layer/drafts/[slug]/visual-assets/twitter-hero.png` | Twitter/Threads contract §3 | 2, process | Show the process the thread walks through |
| Threads | `threads-implication` | `…/visual-assets/threads-implication.png` | Twitter/Threads contract §3 (mandatory) | 5, implication | Illustrate the implication, not the process |
| Facebook | `asset-1` | `02 - content-distribution/04 - facebook-layer/drafts/[slug]/visual-assets/asset-1.png` | Facebook contract §3 and check 6 | 6 visual concept, or 5 implication | Storytelling, high production value, for the business-owner persona |

The file extension follows the brief's format field. PNG is shown for readability only.

## 2. What gets extracted for each slot

| Extract from | What | Into brief field |
|---|---|---|
| `01 - writing-department/03 - research/research-[slug]/synthesis/SPINE.md` | THE ONE THING, and the spine claim this image supports | `idea` |
| `…/research-[slug]/outputs/ARTICLE.md` | The graphic-slot marker and the claim around it; the exact terms the article uses | `idea`, `text_on_image` |
| The hub's `decomposition-seeds.md` | Seed 4 (the named framework and its parts) and seed 6 (the diagrammable description) | `elements` |
| The channel's own variant (post, thread, …) | The angle this channel takes on the seed | `angle` |
| The layer's `OUTPUT_CONTRACT.md` and `WORKFLOW.md` | The channel's visual expectations | `channel_constraints` |
| `02-sourcing/01 - dossiers/D-001-buyer-and-problem/DOSSIER.md` Q13 (once run) | Dimensions and aspect ratio | `format` |
| `02-sourcing/source_ledger.md` or the piece's `sources/` | Where any number shown comes from | `data_sources` |

**Seed-split rule.** When two channels draw on the same seed, their briefs take different visual angles. No brief reuses another brief's elements. This mirrors the distribution seed-split discipline.

## 3. Brief format

One file per slot, at `04 - media-department/01 - requests/[slug]/[channel]-[slot].md`:

    # Brief [slug] · [channel] · [slot]
    id: VB-[slug]-[channel]-[slot]
    status: WAITING-ON-PRODUCER
    piece: research-[slug]
    seed: 4 framework | 6 visual concept | 2 process | 5 implication
    idea: one sentence the image must make obvious
    angle: what this channel's take adds, in one line
    class: diagram | data-viz | illustration | photo
    elements: every box, arrow or figure, in reading order
    text_on_image: the exact words, and nothing else
    data_sources: the ledger or source IDs behind every number shown ("none" if there are no numbers)
    format: [VERIFY: D-001 Q13] until the dossier runs
    channel_constraints: copied from the layer contract
    alt_text: one sentence, what a screen reader should say
    brand: none defined; no Design department exists yet (do not invent a palette)
    destination: the exact path from §1
    provenance: filled by the producer (who or what made it, date, tool, input files)
    history: one line per status change (date, new status, by whom, reason)

## 4. Status lifecycle

| Status | Set by | Meaning |
|---|---|---|
| DRAFTED | S6 | Brief written, not yet checked against §2 |
| WAITING-ON-PRODUCER | S6 | Brief complete; no render yet. **Every brief is here while `04 - media-department/PRODUCER.md` is absent** |
| RENDERED | producer | The file exists at its destination and provenance is filled |
| VERIFIED | verifier (not the producer) | Passed every check in §5 |
| REJECTED | verifier | Failed a check in §5; the failed check is named in `history`. The brief goes back to WAITING |
| ATTACHED | S6 / S7 | The variant references the file and the layer's image check passes |

## 5. Verification

A render counts as done only when it exists and verifies (handoff §2.7: render-dependent unit law). All seven checks must pass:

1. The file exists at `destination`.
2. Every item in `elements` is present, and the image carries exactly the `text_on_image` words and no others.
3. Every number shown traces to `data_sources`.
4. The size and aspect match `format`.
5. The `provenance` field is filled.
6. It is not stock imagery without provenance (every layer contract forbids it).
7. The variant that uses the image carries the `alt_text`.

## 6. What a channel may claim while an image waits

| Brief status | The channel may say | It may not say |
|---|---|---|
| WAITING-ON-PRODUCER | The variant is text-complete (every check except the image passes). The kit is PARTIAL, and `partial_publication.yaml` names the waiting brief ID and gap G-X04 | That it is complete; that the image check passed; that the image is "coming soon" in a posted piece |
| ATTACHED | The layer's image check passes | — |

It is never acceptable to use a stock image, use a placeholder, or silently skip a channel because its image is missing.

## 7. Class routing, for when a producer arrives

| Class | Can be made by | Note |
|---|---|---|
| diagram, data-viz | any producer, including an in-repo SVG producer if the operator approves one | These cover most pilot slots (framework and visual-concept seeds) |
| illustration, photo | a human designer or an image tool | Cannot be substituted with a diagram. The brief stays WAITING until a producer of this class exists |
