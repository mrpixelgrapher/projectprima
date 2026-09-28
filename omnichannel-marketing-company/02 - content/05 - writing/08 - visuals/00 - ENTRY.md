# 08 · Visuals

**Purpose:** write one scene prompt per still (post images, carousel slides, covers, landing and blog images) for the image generation factory, send them in one hand-off, wait, and check every still that comes back. Images are never faked, stocked or skipped.

## Contract

- **Reads:** every variant's metadata block (image slots) in `25-writing/*/channels/`; the articles' `featured` and `inline-N` slots; `08-seeds.md` and `04-spine.md` per piece; `01-sources.md` (for any number shown); the piece briefs (limits, language); `clients/<client>/profile.md` and ASSETS (brand colours, fonts, product photos); `00 - control/01 - law/HANDOFFS.md` (H4).
- **Writes:** `25-writing/stills/<still-id>.prompt.md` (one per still); `25-writing/stills/00-still-index.md`; after the return, the check in the index.
- **Done when:** every image slot has a still that passed the checks, next to its prompt, and the index shows every still ACCEPTED.

## Procedure

1. **Collect every slot** from the variants and articles. Still id: `S-<P>-<channel>-<slot>`, e.g. `S-P2-instagram-carousel-3`. (Video frames are prompted by the video factory, not here.)
2. **Write the scene prompt** for each still (template below). What to decide for each field:

   | Field | Rule |
   |---|---|
   | idea | The one thing the image must make obvious, from the spine or the slot's text |
   | scene | Subject, setting, composition, lighting, lens and camera angle, style, colour palette: concrete enough that two renders would look alike |
   | text | The exact words to show, or "none". Say whether the factory renders them or the layout adds them |
   | consistency | Other stills that must match (the same product, character or style across carousel slides): name them |
   | format | Aspect ratio and size for the channel [VERIFY: the platform's current size, query-bank Q12] |
   | brand | Colours, fonts, product references from the client's ASSETS; "none supplied: don't invent a brand" otherwise |
   | never | What must not appear: competitors' marks, invented logos, false claims, stock-photo look |
   | data | The L-ID behind any number shown |

3. **Seed split:** two channels drawing on the same seed get different visual angles.
4. **Hand off (H4):** the operator copies the prompt files to the image factory's queue (path in `HANDOFFS.md`). Hold: `task.py hold <task-id> --on "H4 image factory: 25-writing/stills/ (<n> prompts)"`. A rehearsal is not sent.
5. **When the stills return** (each next to its prompt, same id), resume and check each one:

   | # | Check |
   |---|---|
   | 1 | The file is next to its prompt, named by its still id |
   | 2 | It shows the idea and the scene's subject, and nothing the "never" list forbids |
   | 3 | The text is exact (or absent if the layout adds it) |
   | 4 | Every number traces to its L-ID |
   | 5 | The format matches the channel |
   | 6 | It matches the stills named under consistency |
   | 7 | It doesn't look like stock imagery |

   A still that fails gets a revised prompt, `<still-id>.prompt-2.md`, naming the failed check; resend (H4) and hold again. After 3 failed rounds on one still, ask the operator (H2).
6. **Index:** each still with its status: PROMPTED → RETURNED → ACCEPTED (or REVISED n).

## Output template

`<still-id>.prompt.md`:

    # <still-id> · <channel> · <slot>
    idea: …
    scene: subject … · setting … · composition … · lighting … · lens/angle … · style … · palette …
    text: "<exact words>" (render: factory / layout) | none
    consistency: <still ids> | none
    format: <ratio, size>
    brand: …
    never: …
    data: <L-IDs> | none
    alt text: <one sentence>

`00-still-index.md`:

    # Still index — <task id>
    | Still | Piece | Channel | Slot | Status | Check notes |

## Worked example

*(illustrative)* `S-P2-instagram-carousel-1` · idea: "two gifts that look identical; only one is real" · scene: two blue sapphires on white marble, overhead, soft north light, 50 mm, clean editorial style, deep blue and white · text: "Real or fake?" (render: layout) · consistency: carousel-2 to carousel-7 share the marble and light · format: 4:5 · never: logos, hands with rings, price tags.

## Self-check

- [ ] Does every slot have a prompt, and every prompt all fields?
- [ ] Were the returned stills checked against all 7, with failures re-prompted?

## Traps

- **A vague prompt.** "A nice image about trust" can't be rendered twice the same way, or checked.
- **Accepting "close enough".** A wrong word on an image ships.
