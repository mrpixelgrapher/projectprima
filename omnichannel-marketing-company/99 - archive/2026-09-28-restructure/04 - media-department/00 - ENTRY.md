# Media Department — image station

Type: function folder. This is side station **M** in `00-control/ASSEMBLY_LINE.md`: it feeds S6 (Shape) and S7 (Post).
Status: **NOT OPERATIONAL. The intake is built; there is no producer.** It was created on 2026-09-28 (session S002) from input I-005.

## Why this folder exists

Every channel contract makes a custom image mandatory, the hub included (`02-sourcing/source_ledger.md` L-006). Nothing in this repo can make one. The CE workspace's Media department (`03 - architecture-governance/DEPARTMENT_REGISTRY.md` row 1) is not here (`03 - architecture-governance/EXTERNAL_DEPENDENCY_REGISTER.md` X-04).

So this station is built intake-first. The line does all the thinking about images now: which image, for which channel, showing what, with which words. That thinking is written down as briefs. When a producer arrives, it reads the briefs and renders. Nothing has to be re-thought, and no image is faked in the meantime.

## What exists and what doesn't

| Part | State |
|---|---|
| `VISUAL_BRIEF_CONTRACT.md` | Built. Defines the slots per channel, what gets extracted, the brief format, the status lifecycle, verification, and what a channel may claim while waiting |
| `01 - requests/[slug]/` (one brief per image slot) | Declared. S6 creates it when the first piece is shaped |
| `PRODUCER.md` | **Absent.** This absence is what `00-control/tools/line_status.py` reads as NOT OPERATIONAL |
| Rendered images | None |

## The flow

    S5 PASS: the article (research-[slug]/outputs/ARTICLE.md)
       │  extract: the article's graphic slots, the spine's one thing,
       │           decomposition seeds 4 (framework) and 6 (visual concept)
       ▼
    S6 Shape: for each channel that is ON (02 - content-distribution/CHANNEL_ACTIVATION.md)
       │  make: one brief per required image slot, at 01 - requests/[slug]/
       │        status WAITING-ON-PRODUCER
       ▼
    M  Producer (absent): reads the waiting briefs, renders, records provenance
       │  make: the image file at the layer's visual-assets path; status RENDERED
       ▼
    Verify: the render-dependent unit law (handoff §2.7); status VERIFIED or REJECTED
       ▼
    Attach: the variant references the file, and the layer's image check can pass; status ATTACHED
       ▼
    S7 Post: a kit is COMPLETE only when every slot of every ON channel is ATTACHED

## While no producer exists

- S6 still writes every brief, so the image thinking happens while the piece is fresh.
- Each layer's image check reports **WAITING-ON-PRODUCER**. It never passes, and it is never skipped.
- A variant can be *text-complete* but never *complete*. Kits stay PARTIAL, with the reason logged in `partial_publication.yaml`.
- No stock image, no placeholder image, and no "image to follow" posted as finished.
- Whether to post the pilot with an image slot still waiting is the operator's decision, not the line's (`02 - content-distribution/CHANNEL_ACTIVATION.md`, pilot exit, condition 3).

## Switching the station on

1. Write `PRODUCER.md`: who or what produces (a person, a tool, a pipeline); which classes it can make (diagram, data-viz, illustration, photo); and how it records provenance. From then on `line_status.py` reports M as OPERATIONAL.
2. The producer works through WAITING briefs oldest first. Briefs whose class it can't make stay WAITING (§7 of the contract).
3. After the first VERIFIED render, update: register row X-04 (Substitute and Status); gap G-X04; the image column of `02 - content-distribution/CHANNEL_ACTIVATION.md`; and a note in `03 - architecture-governance/DEPARTMENT_REGISTRY.md`. Log the change in `meta_workspace.md` §3.
4. Change this file's Status line only after that first VERIFIED render.

## Reads and writes

- Reads: `research-[slug]/synthesis/SPINE.md`, `research-[slug]/outputs/ARTICLE.md`, the Substack hub's `decomposition-seeds.md`, each ON channel's variant and `OUTPUT_CONTRACT.md`, and `02 - content-distribution/CHANNEL_ACTIVATION.md`.
- Writes: briefs in `01 - requests/[slug]/`. The producer writes images into the layers' `drafts/[slug]/visual-assets/` folders.
