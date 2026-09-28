# 04 · Voice

**Purpose:** capture how the client talks, so writing re-voices every piece toward one real person or brand instead of toward "human in general". When the client has no writing of their own, model the voice on creators they choose.

## Contract

- **Reads:** the writing samples in `from-client/`; `21-discovery/02-slot-board.md` (slots VOICE and BRAND, decision F1); `21-discovery/05-creator-library.md`; `voiceprint-prompt.md` in this folder.
- **Writes:** `21-discovery/06-voiceprint.md`.
- **Done when:** the voiceprint has all six dimensions, each backed by quoted lines, and it names its basis ("own samples" or "modelled on <creators>") and its confidence.

## Procedure

1. **Choose the basis.**

   | F1 | What the client supplied | Basis |
   |---|---|---|
   | EXISTING | 3+ pieces the brand or owner wrote or said | Own samples: the brand's writing |
   | THIRD-PARTY | 3+ pieces from the third party | Own samples: the third party's writing (supplied by our client) |
   | NEW, or TO STRATEGY | 3+ pieces the founder wrote or said | Own samples: the founder. Strategy shapes the new brand's voice from this at `02 - content/02 - strategy/02 - messages/` |
   | any | fewer than 3 samples, and 1–2 named creators | **Modelled on creators:** the named creators' public posts (the dossier's samples, or an ARENA request for 5 posts each) |
   | any | neither | Ask (H1): "Name 1–2 people whose way of talking you want to sound like; or pick from these 3", listing 3 creators from the library with one short line each. Hold |

2. **Qualify each sample.** Keep only text the person wrote or said themselves. Drop agency copy, templated posts and AI-edited text: the voiceprint copies whatever it is given.
3. **Run the prompt.** Put the qualified samples into `{{3-5 PIECES OF THE AUTHOR'S OWN REAL WRITING}}` in `voiceprint-prompt.md`, and run it. When modelling on creators, run it on the creators' posts, then add a line under each dimension: "Adapted for <client>: …" (the creator's pattern, not their words or persona).
4. **Back every dimension with evidence:** at least 2 short quotes from the samples. Delete any trait you can't quote.
5. **Record the basis and confidence:** high with 5 samples of the person's own writing; medium with 3–4, transcripts only, or modelled on creators; low if any sample is doubtful.

## Output template

    # Voiceprint — <client> · from <task id>
    Basis: own samples (<brand / founder / third party>) | modelled on <creators> · Samples: <files or links> · Confidence: <high/medium/low>
    ## 1. Sentence rhythm
    ## 2. Punctuation signature
    ## 3. Lexicon and tics (10+ signature words; words they never use)
    ## 4. Openings and closings
    ## 5. Stance
    ## 6. The tell
    (each dimension: 2+ quoted lines from the samples)

## Worked example

Gemstone task, F1 = NEW, founder samples available *(illustrative)*. Basis: own samples (founder); the brand voice is shaped at strategy.

    ## 6. The tell (illustrative)
    Names the stone and its origin before any adjective: "a Ceylon blue, unheated, 2.1 carats — the kind
    you notice across a table." Remove the specific stone, and it stops sounding like them.

## Self-check

- [ ] Were only the person's own words used?
- [ ] Does every dimension have at least 2 quoted lines?
- [ ] Are the basis and confidence stated?

## Traps

- **Voiceprint from marketing copy.** Website text written by an agency gives the agency's voice.
- **Adjectives instead of evidence.** "Friendly and authoritative" says nothing the drafter can write toward.
- **Skipping this for a new brand.** The founder's voice is still the raw material strategy shapes.
- **Becoming the creator.** A voice modelled on a creator borrows their rhythm and devices, never their persona, claims or catchphrases.
