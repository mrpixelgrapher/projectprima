# 01 · Edit plan

**Purpose:** one edit decision list per video that an editor follows line by line.

## Contract

- **Reads:** `31-script/<V-id>-shooting-script.md`; `32-shots/<V-id>-shot-list.md`; `34-motion/motion/` (accepted clips); `33-stills/stills/` (stills held on screen); the piece brief (platform, CTA, language).
- **Writes:** `35-edit-plan/<V-id>-edit-plan.md`; `35-edit-plan/00-edit-index.md`.
- **Done when:** every second of every video is covered by a clip or a held still, and every voice-over line, text, sound and caption has a time.

## Procedure

1. **Timeline:** in order, each item's source (clip `T-…`, or still `K-…` held for n s), in and out times, and the cut or transition into the next.
2. **Voice-over:** each line with its start time (from the shooting script); who records it (the client, or a voice the client approves).
3. **On-screen text:** each with its start, end, position and style (from the look in continuity).
4. **Music and sound:** mood and tempo, where it rises or drops, sound effects on key moments; licensed or royalty-free only (name the source when chosen).
5. **Captions:** a full caption file in the video's language, timed to the voice-over.
6. **End card:** the CTA and the destination, for the last 3–5 s.
7. **Export:** per platform: aspect, resolution, length limit, file type [VERIFY: the platform's current specs].

## Output template

    # Edit plan <V-id> — <platform>, <length>
    ## Timeline
    | # | Start | End | Source | Transition in |
    ## Voice-over
    | Start | Line | Recorded by |
    ## On-screen text
    | Start | End | Text | Position · style |
    ## Music and sound
    ## Captions (<language>)
    ## End card
    ## Export

## Worked example

*(illustrative)* `| 1 | 0.0 | 2.2 | T-V2a-1 | — |` · VO `0.2 "Your festival gift might be fake."` · text `0.3–2.0 "Real or fake?" centre, white serif`.

## Self-check

- [ ] Is every second covered, and does the total equal the length?
- [ ] Does every VO line, text and caption have a time?

## Traps

- **"Add music."** Name the mood, tempo and the moments it changes.
