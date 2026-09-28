# 01 · Kit

**Purpose:** a kit the client (or our publishing node) can post from without adapting anything: one folder per channel, every post in date order, final text, its image, and exactly where its link goes.

## Contract

- **Reads:** `25-writing/<P>/channels/*.md`; `25-writing/stills/` (accepted stills); `35-edit-plan/` (videos, when included); `24-planning/02-calendar.md`; `22-strategy/04-channel-plan.md` (month task: `clients/<client>/strategy.md`).
- **Writes:** `26-packaging/kit/<NN-channel>/<date>-<P>-<slug>.md` (one per post), `26-packaging/kit/<NN-channel>/images/`, `26-packaging/kit/video/` (when included), `partial_publication.yaml` in any channel folder that needs it, and `26-packaging/01-kit-index.md`.
- **Done when:** every post in the calendar has its kit file with a publish block, and every channel folder's completeness is stated.

## Procedure

1. **One folder per channel** in the plan: `kit/01-<channel>/`, `02-<channel>/` …, in the order of the channel plan (the long-form home first).
2. **One file per post,** named `<YYYY-MM-DD>-<P>-<slug>.md`, so the folder reads in posting order.
3. **Copy the final text** from the variant, word for word, without its metadata block and audit trail. Put a **publish block** above it:

       Post on: <channel> · Date and time: <from the calendar>
       Link: <tagged link> · Where: <body / first comment / final post / bio / canonical>
       Image: images/<still-id>.<ext> (alt text: …) | Video: ../video/<V-id>/
       Test variant: <T… A/B | none>
       Client to supply before posting: <items, or none>

4. **Images:** copy each accepted still into the channel's `images/`, named by its still id. **Video:** copy each video's edit plan and clips into `kit/video/<V-id>/`.
5. **Completeness per channel folder:**
   - **COMPLETE:** every post is final, and every image and video is in the kit.
   - **PARTIAL:** anything is waiting (a `CLIENT TO SUPPLY` item). Write `partial_publication.yaml` in that folder:

         partial_publication:
           channel: <channel>
           posts_ready: [...]
           posts_waiting: [...]
           client_to_supply: [...]
           reason: "<what is missing and who supplies it>"

6. **Kit index:** one row per channel: folder, posts, completeness (and why partial).

## Output template

    # Kit index — <task id> · <month>
    | Channel | Folder | Posts | Images | Completeness | Why partial |

## Worked example

*(illustrative)* `kit/03-instagram/2026-11-10-P2-real-or-fake.md` · Link: bio link `…&utm_content=P2-a` · Image: `images/S-P2-instagram-carousel-1.png` … `-7.png` · Test variant: T1-A.

## Self-check

- [ ] Does every calendar post have a kit file with a publish block?
- [ ] Is the text identical to the passed variant?
- [ ] Does every PARTIAL folder have its yaml?

## Traps

- **Adapting at packaging.** If the client would have to rewrite something, the kit has failed.
- **Calling a folder complete with something waiting.**
