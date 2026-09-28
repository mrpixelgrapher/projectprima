# Author Voice — whose voice this line produces

Station **S1a (who: voice)** in `00-control/ASSEMBLY_LINE.md`. Nothing downstream may write a sentence until this station is FILLED.
Created: 2026-09-28, session S002, from input I-001 (`02-sourcing/input_registry.md`).
Sessions maintain `## Claims`. The friend answers in `## Fill-in`.

## Claims

- The author is the friend: every piece this line produces is written in the friend's expertise and voice. The friend is not a client of this line. [src: I-001]
- The author's real name: [CARBON-BLOCKED: F-002 Q1]
- The field the content must show expertise in is omnichannel marketing for founder-led and small businesses, because that is what the company sells. [src: L-001]
- The friend's own specialty within that field, and the facts their expertise rests on: [CARBON-BLOCKED: F-002 Q1]
- The author's way of talking (sentence rhythm, words they use and never use, how they open and close, whether they say "I") is extracted by Stage 04 Part A from 3–5 real samples into `01 - writing-department/voiceprints/[author-slug].md`. It is never written by hand from impressions. [src: L-009] Samples: [CARBON-BLOCKED: F-002 Q2]
- The author publishes under their own name on the hub and the first spoke: the voice and the publishing identity are the same person. [src: I-001, I-004] Account handles are read at posting time, not writing time, so they live in `02 - content-distribution/CHANNEL_ACTIVATION.md` (F-002 Q4).
- The identity that sat in the platform folders' defaults, from an earlier project about a lawyer and a consultant, is not this author. No piece may be written in that identity. [src: I-001, L-010]

## What reads this file

Each reader below has a one-line pointer back to this file, appended in S002. Filling this file is therefore the only change needed for the whole line to read the right identity.

| Reader | Reads | Where |
|---|---|---|
| Writing chain input | name, samples | `01 - writing-department/01 - prompt-library/00 - WIRING_MANIFEST.md`, "INPUT: topic + author name (+ 3-5 writing samples)" |
| Stage 01 boundary research | field | `01 - writing-department/01 - prompt-library/01 - PROMPT_boundary_research.md`, slot `{{DOMAIN}}` |
| Stage 04 voice | samples → voiceprint | `01 - writing-department/01 - prompt-library/04 - PROMPT_voice_humanization.md`, Part A SAMPLES and Part B "named author" |
| Stage 05 gate | name, voiceprint | `01 - writing-department/01 - prompt-library/05 - PROMPT_perfection_gate.md`, check V1 |
| Channel activation | publishing name, handles | `02 - content-distribution/CHANNEL_ACTIVATION.md`, "Publishes as" |
| Vertical profile | field, name | `03 - architecture-governance/MULTI_VERTICAL_CONTENT_OS.md`, this company's vertical (appended S002) |

## Fill-in

For the friend. Answer here, or in `00-control/carbon-input/CARBON_INPUT_FORM-002.md`. Write facts only. Leave a blank rather than guess.

- Name as it should appear when publishing:
- Field or specialty, in one line:
- What your expertise rests on (years, roles, notable work):
- 3–5 pieces of your own writing: paste them below or add them as files in `01 - writing-department/voiceprints/samples/`

When this is filled, the next session logs each answer in `02-sourcing/input_registry.md`, moves it into `## Claims` as `[src: I-nnn]`, and runs Stage 04 Part A to produce the voiceprint.
