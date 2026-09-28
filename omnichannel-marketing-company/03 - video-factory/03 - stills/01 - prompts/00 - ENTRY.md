# 01 · Prompts

**Purpose:** one scene prompt per keyframe, precise enough that the image factory renders exactly the shot, consistent with every other keyframe.

## Contract

- **Reads:** `32-shots/01-continuity.md` (the keyframe list, references, the look); `32-shots/<V-id>-shot-list.md`; `00 - control/01 - law/HANDOFFS.md` (H4).
- **Writes:** `33-stills/stills/<keyframe>.prompt.md` (one per keyframe); `33-stills/00-still-index.md`.
- **Done when:** every keyframe has a prompt with every field, the prompts are handed off, and the task is on HOLD.

## Procedure

1. **One prompt per keyframe,** in the format of `02 - content/05 - writing/08 - visuals/00 - ENTRY.md` (idea, scene, text, consistency, format, brand, never, data, alt text), with the shot's framing, lens, angle, light and style written into `scene`, and every recurring element described with the continuity bible's exact words.
2. **The -b keyframe** of a moving shot describes the frame at the end of the move (e.g. after a push-in: tighter framing, same light).
3. **Text:** on-screen text is added in the edit, not rendered in the still, unless the shot list says otherwise.
4. **Hand off (H4)** and hold: `task.py hold <task-id> --on "H4 image factory: 33-stills/stills/ (<n> keyframes)"`. A rehearsal is not sent.

## Output template

`00-still-index.md`:

    # Keyframe index — <task id>
    | Keyframe | Video · shot | Prompt | Status | Check notes |

## Worked example

*(illustrative)* `K-V2a-S1-a` · scene: "two identical oval sapphires (Sapphire A per continuity) on white Carrara marble, top-down macro, soft cool window light from the left, product studio style, palette deep blue / white / brushed silver" · format 9:16 · never: hands, logos, price tags.

## Self-check

- [ ] Does every prompt use the continuity bible's exact element descriptions?

## Traps

- **Describing the same product two ways.** Two different stones will come back.
