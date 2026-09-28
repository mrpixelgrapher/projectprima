# 01 · Shot list

**Purpose:** turn each frame of the shooting script into shots described in full: the stills node renders their keyframes from this, and the motion node moves between them from this.

## Contract

- **Reads:** `31-script/<V-id>-shooting-script.md` (every video); the piece brief (limits); `clients/<client>/profile.md` and ASSETS (products, brand).
- **Writes:** `32-shots/<V-id>-shot-list.md` (one per video).
- **Done when:** every frame has its shots; every shot has every field below; every shot's transition to the next is described; the durations add up to the script's.

## Procedure

1. **Shots per frame.** A frame with one visual idea is one shot; a frame whose "move to next" changes the subject or the angle is two.
2. **Describe each shot** with every field, using the vocabulary below:

   | Field | What to write | Vocabulary |
   |---|---|---|
   | Scene | Subject, setting, action (what moves inside the frame) | Concrete nouns and verbs |
   | Framing | How much of the subject is in frame | extreme close-up · close-up · medium · wide · overhead (flat lay) · over-the-shoulder |
   | Lens and angle | The look of the image | 24 mm wide · 50 mm natural · 85 mm portrait · macro; eye level · low · high · top-down |
   | Camera move | How the camera moves during the shot | static · pan · tilt · push-in · pull-out · dolly (track) · orbit · crane · handheld |
   | Light | Where light comes from and its quality | soft window light · hard sun · studio softbox · backlight · practical lamps; warm / cool |
   | Style | The look | editorial · documentary · product studio · cinematic · illustrated |
   | Transition out | How this shot becomes the next | cut · match cut (on shape or motion) · whip pan · dissolve · morph (A becomes B) · stop-motion |
   | Stop-motion (if used) | What moves, how far per frame, frames per second, frame count | e.g. "the stones slide 1 cm per frame, 12 fps, 18 frames" |
   | Keyframes | The stills this shot needs: its first frame, and its last frame if it moves or morphs | K-<V-id>-<shot>-a / -b |
   | Sound and text | The voice-over line under it; the on-screen text | from the shooting script |
   | Duration | Seconds | adds up to the frame's duration |

3. **Honest shots only.** A product shot shows the client's real product (from ASSETS) or is marked "illustrative render" on screen; a claim shown on screen is one the piece proved.

## Output template

    # Shot list <V-id>
    | Shot | Frame | Duration | Scene | Framing | Lens · angle | Camera move | Light | Style | Transition out | Stop-motion | Keyframes | VO · on-screen text |

## Worked example

*(illustrative)* `S1 · F1 · 2.2 s · two identical blue sapphires on white marble; nothing moves · close-up · macro, top-down · slow push-in · soft window light from the left, cool · product studio · match cut on the round shape into S2 · — · K-V2a-S1-a, K-V2a-S1-b · "Your festival gift might be fake." / "Real or fake?"`

## Self-check

- [ ] Does every shot have every field?
- [ ] Does every moving or morphing shot name two keyframes?
- [ ] Do the durations add up?

## Traps

- **"A nice shot of the product."** The stills and motion nodes can only render what is written.
- **Moves nobody can render.** A shot with three camera moves at once breaks in the motion model; one move per shot.
