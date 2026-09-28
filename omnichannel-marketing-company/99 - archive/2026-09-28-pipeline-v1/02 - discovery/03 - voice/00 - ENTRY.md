# 03 · Voice

**Purpose:** capture how the client actually talks, so that drafting re-voices every piece toward one real person or brand instead of toward "human in general".

## Contract

- **Reads:** the writing samples in `client/`; `02-discovery/01-slot-board.md` (slots VOICE and BRAND, decision F1); `voiceprint-prompt.md` in this folder.
- **Writes:** `02-discovery/04-voiceprint.md`.
- **Done when:** the voiceprint has all six dimensions, each backed by quoted lines, and it names its source and confidence.

## Procedure

1. **Choose the voice source.**

   | F1 | Samples available | Voice source |
   |---|---|---|
   | EXISTING | 3+ pieces the brand or owner wrote themselves | The brand's own writing |
   | THIRD-PARTY | 3+ pieces from the third party | The third party's writing (supplied by our client) |
   | NEW, or TO STRATEGY | 3+ pieces the founder wrote | The founder. The new brand's voice is set at `03 - strategy/02 - messages/`, starting from this |
   | any | fewer than 3 | Ask in round 2 for samples, **or** 2–3 voice notes or call transcripts (spoken text counts). The gate holds |

2. **Qualify each sample.** Keep only text the person wrote or said themselves. Drop agency-written web copy, templated posts, and AI-edited text, because the voiceprint copies whatever it is given.
3. **Run the prompt.** Put the qualified samples into `{{3-5 PIECES OF THE AUTHOR'S OWN REAL WRITING}}` in `voiceprint-prompt.md`, and run it.
4. **Back every dimension with evidence:** at least 2 short quotes from the samples. Delete any trait you can't quote (e.g. "warm", "professional" with no line showing it).
5. **Record the source and confidence:** high with 5 samples of the person's own writing; medium with 3–4, or with transcripts only; low if any sample is doubtful.

## Output template

    # Voiceprint — <task id>
    Source: <brand / founder / third party> · Samples: <list of client/ files> · Confidence: <high/medium/low>
    ## 1. Sentence rhythm
    ## 2. Punctuation signature
    ## 3. Lexicon and tics (10+ signature words; words they never use)
    ## 4. Openings and closings
    ## 5. Stance
    ## 6. The tell
    (each dimension: 2+ quoted lines from the samples)

## Worked example

Gemstone task, F1 = NEW, founder samples available. Source: founder; the brand voice is set at strategy.

    ## 6. The tell (illustrative)
    Names the stone and its origin before any adjective: "a Ceylon blue, unheated, 2.1 carats — the kind
    you notice across a table." Remove the specific stone, and it stops sounding like them.

## Self-check

- [ ] Were only the person's own words used?
- [ ] Does every dimension have at least 2 quoted lines?
- [ ] Are the source and confidence stated?

## Traps

- **Voiceprint from marketing copy.** Website text written by an agency gives the agency's voice.
- **Adjectives instead of evidence.** "Friendly and authoritative" says nothing the drafter can write toward.
- **Skipping this for a new brand.** The founder's voice is still the raw material strategy shapes.
