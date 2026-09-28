# Voiceprint prompt (discovery stage 04)

**Used by:** `02 - content/01 - discovery/04 - voice/00 - ENTRY.md`. **Origin:** `99 - archive/2026-09-28-restructure/01 - writing-department/01 - prompt-library/04 - PROMPT_voice_humanization.md`. The prompt block and its reasoning are carried over verbatim; the stage ENTRY fills its slots and says where its output goes. This is Part A of the original two-part voice prompt; Part B lives in `02 - content/05 - writing/03 - voice/revoice-prompt.md`.

### Part A — VOICEPRINT EXTRACTION (run once per author, reuse forever)

```
ROLE: You are a voice analyst. Given 3-5 samples of ONE author's real writing, extract
their idiolect — the fingerprint that makes their prose theirs. Output a VOICEPRINT the
drafter can write toward.

SAMPLES: {{3-5 PIECES OF THE AUTHOR'S OWN REAL WRITING}}

Extract:
1. SENTENCE RHYTHM — their distribution of sentence lengths. Do they run long-then-short?
   Use fragments? Average length? Quote 3 sentences that are unmistakably theirs.
2. PUNCTUATION SIGNATURE — em-dashes? semicolons? parentheticals? ellipses? How do they
   handle emphasis — italics, caps, repetition?
3. LEXICON & TICS — recurring words, characteristic transitions, words they'd never use,
   register (formal/wry/blunt). List 10+ signature words/phrases.
4. OPENINGS & CLOSINGS — how do they start a piece? How do they land one?
5. STANCE — do they hedge or assert? Address the reader directly? Use "I"? Tell stories or
   stay abstract?
6. THE TELL — the one thing that, if removed, would make the piece stop sounding like them.

OUTPUT: VOICEPRINT.md — a profile concrete enough that prose can be written TOWARD it.
```

## Why a voiceprint first

From the original reasoning: "When you tell a model to humanize, you give it no target. 'Human' is an average, and the model's failure mode IS regression to an average... There is no such thing as 'human in general' to write toward. There are only specific humans. This is the entire reason Part A exists and is mandatory: you do not humanize toward humanity, you re-voice toward one named author with an extractable fingerprint."
