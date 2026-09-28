# 02 · Kit

**Purpose:** assemble a PUBLISH_KIT that the client can publish without adapting anything: every piece, every channel in the plan, final text, in publishing order, with each link placement and image stated.

## Contract

- **Reads:** `09-packaging/pieces/*/08-shaping/` (the hub, the variants, the visual index); the parent's `03-strategy/03-channel-plan.md`; `09-packaging/01-join-report.md`.
- **Writes:** `09-packaging/PUBLISH_KIT/<NN-piece-slug>/<NN-channel>.md`, one `partial_publication.yaml` per piece where needed, and `09-packaging/02-kit-index.md`.
- **Done when:** every piece has one file per channel in the plan, and every piece's completeness is stated.

## Procedure

1. **Folder per piece:** `PUBLISH_KIT/01-<cornerstone-slug>/`, `02-<slug>/` …, in plan order.
2. **File per channel, in publishing order:** `01-hub.md` first, then the spokes in the order the schedule uses them (`02-linkedin.md`, …).
3. **Copy the final text** from the piece's `08-shaping/` file, word for word. Put a **publish block** above it:

       Publish on: <channel> · When: <schedule reference>
       Link: <where the hub link goes: body / first comment / final post / bio / canonical>
       Image: <file in images/, or "WAITING — brief VB-…">
       Alt text: …
       Client to supply before posting: <items, or none>

4. **Images:** list rendered files under `PUBLISH_KIT/<piece>/images/`. Slots that are waiting stay listed with their brief ID.
5. **Completeness per piece:**
   - **COMPLETE:** every channel in the plan is final, and every image is ATTACHED.
   - **PARTIAL:** anything is waiting (images, or client-supplied facts).
6. **`partial_publication.yaml`.** Write one in the piece's folder when it is PARTIAL, or when the plan skipped any of the doctrine's channels (website, hub, Medium, Twitter/X, LinkedIn):

       partial_publication:
         artifact: <piece slug>
         channels_shipped: [...]
         channels_skipped: [...]
         reason: "<the channel plan's 'left out' reasons>"
         waiting_images: [<brief IDs>]
         client_to_supply: [...]

7. **Kit index:** one row per piece, giving its folder, its channels, and COMPLETE or PARTIAL (and why).

## Output template

    # Kit index — <parent id>
    | Piece | Folder | Channels | Completeness | Why partial |

## Self-check

- [ ] Does every piece have a file for every channel in the plan, with the hub first?
- [ ] Is the text identical to the shaped variant?
- [ ] Does every file have a publish block?
- [ ] Does every PARTIAL piece have its yaml?

## Traps

- **Adapting at packaging.** If the client would have to rewrite something, the kit has failed.
- **Calling a kit complete with images waiting.**
