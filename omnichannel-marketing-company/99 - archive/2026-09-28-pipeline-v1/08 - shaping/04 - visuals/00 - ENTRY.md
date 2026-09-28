# 04 · Visuals

**Purpose:** write one brief per image slot, so that a producer can render every image without re-thinking the piece. If there is no producer, the briefs wait. Images are never faked, and channels are never silently skipped.

## Contract

- **Reads:** the channel variants in `08-shaping/03-channels/`; `08-shaping/02-hub-article.md` (featured and inline slots); `08-shaping/01-seeds.md`; `05-research/04-spine.md`; `05-research/01-sources.md` (for any number shown); `00-brief.md` (limits).
- **Writes:** `08-shaping/04-visuals/<channel>-<slot>.md` (one per slot) and `08-shaping/04-visual-index.md`.
- **Done when:** every slot named in the hub and the variants has a brief, and the index shows each one's status.

## Files in this folder

| File | Role |
|---|---|
| `PRODUCER.md` | **Absent today.** When a producer exists (a person, tool or pipeline), this file says who or what it is, which classes it can make (diagram, data-viz, illustration, photo), and how it records provenance. While it is absent, every brief is WAITING-ON-PRODUCER |

## Procedure

1. **Collect every slot** from the hub (`featured`, `inline-N`) and each variant's metadata. Common slots: LinkedIn `asset-1`, Twitter/X `twitter-hero`, Threads `threads-implication`, Facebook `asset-1`, Instagram `carousel-N`, website `website-hero`, email `email-header`, ads `ad-<platform>-<angle>`, collateral `collateral-cover`. Medium reuses the hub's `featured`.
2. **Extract for each slot:**

   | From | Extract | Brief field |
   |---|---|---|
   | The spine and the slot's surrounding text | The one idea this image must make obvious | idea |
   | The seed assigned to the channel | The elements (boxes, steps, figures) | elements |
   | The variant's text | The channel's angle; the exact words to show | angle, text_on_image |
   | `05-research/01-sources.md` | The source behind every number shown | data_sources |
   | The channel's ENTRY | Its visual expectations (e.g. no meme style on LinkedIn; storytelling on Facebook) | channel_constraints |

   **Seed-split:** two channels drawing on the same seed get different visual angles.
3. **Set the class:** diagram, data-viz, illustration or photo.
4. **Set the status.** If `PRODUCER.md` exists and lists this class: `WAITING` (queued). Otherwise: `WAITING-ON-PRODUCER`.
5. **Write the index.**

## Output templates

    # Brief <slug> · <channel> · <slot>
    id: VB-<slug>-<channel>-<slot> · status: WAITING-ON-PRODUCER · class: …
    idea: … · angle: …
    elements: …
    text_on_image: "<exact words, nothing else>"
    data_sources: <L-IDs, or none>
    format: [VERIFY: the platform's current image size, query-bank Q12]
    channel_constraints: …
    alt_text: <one sentence>
    brand: <brand colours/fonts if the client supplied them in ASSETS, else "none supplied, don't invent">
    destination: 09-packaging/PUBLISH_KIT/<piece>/images/<channel>-<slot>.<ext>
    provenance: <filled by the producer>
    history: <date, status, by, reason>

    # Visual index — <task id>
    | Brief | Channel | Slot | Class | Status |

## What happens after a brief

| Status | Set by | Meaning |
|---|---|---|
| WAITING-ON-PRODUCER | this stage | There is no producer for this class. The variant is text-complete; the kit will be PARTIAL |
| WAITING | this stage | A producer exists; the brief is queued |
| RENDERED | the producer | The file is at its destination, with provenance filled |
| VERIFIED | a verifier (not the producer) | It passes all 7 checks below |
| ATTACHED | packaging | The kit references the file; the variant can be complete |

**Verification (all 7):** the file exists at its destination · the elements and the exact words are present, with no others · every number traces to data_sources · the format matches · provenance is filled · it is not stock imagery · the alt text is in the variant.

## Worked example

*(illustrative)* `VB-real-or-fake-linkedin-asset-1` · class: diagram · idea: "anyone can verify a gemstone gift in 60 seconds" · elements: three numbered steps (lab name → report number on the lab's site → carat weight) · text_on_image: "The 60-second check" / "1 Lab name" / "2 Report number" / "3 Carat weight".

## Self-check

- [ ] Does every slot in the hub and the variants have a brief?
- [ ] Does every number shown have a data source?
- [ ] Is the status WAITING-ON-PRODUCER wherever `PRODUCER.md` is absent?

## Traps

- **A placeholder or stock image "for now".** The rules forbid it, and it would ship by accident.
- **Vague briefs.** "A nice image about trust" can't be rendered or verified.
