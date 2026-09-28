# 03 · Voice

**Purpose:** re-voice the draft so the client could have written it: their rhythm, their words and their tell, with the machine tells removed. The argument, evidence and structure stay exactly as drafted.

## Contract

- **Reads:** `25-writing/<P>/05-draft.md`; the Voice section of the piece brief (`24-planning/briefs/<P>.md`: the voiceprint, voice rules, words to use and never use, language); `revoice-prompt.md` in this folder.
- **Writes:** `25-writing/<P>/06-article.md`.
- **Done when:** the article ends with the voice note, and no `[src: …]` marker remains.

## Procedure

1. **Run Part B** of `revoice-prompt.md`, with the draft as `DRAFT.md` and the brief's voiceprint as `VOICEPRINT.md`.
2. **Apply the brief's word lists.** Use the "use" words where they fit naturally. Remove every "never" word.
3. **Strip the `[src: …]` markers.** The draft keeps them for review (review traces through `05-draft.md`). Keep the `[LINK: …]` and `[GRAPHIC: …]` markers.
4. **Fidelity.** Every paragraph of the article must map to a paragraph of the draft. Merge or split sentences for rhythm, never to add a claim.
5. **Language.** Write in the language the brief sets for the long-form home. Channel variants in another language are written natively in that language at `06 - channels/`, never translated from this article.
6. **End with the voice note:** `Voice note: voiced toward <basis from voiceprint>; tells killed: N; read-aloud: PASS`.

## Output template

    <the article, same skeleton as the draft, markers stripped except LINK and GRAPHIC>

    Voice note: voiced toward …; tells killed: N; read-aloud: PASS

## Worked example

*(illustrative)* Draft: "It is important to note that certificates play a crucial role in establishing authenticity." Voiced toward the founder's tell (the stone first): "A Ceylon blue with its lab report beats a 'premium gemstone' without one. Every time."

## Self-check

- [ ] Does the voice note exist, with a tell count and read-aloud PASS?
- [ ] Are no `[src: …]` markers left, and are all LINK and GRAPHIC markers kept?
- [ ] Does every paragraph map to a draft paragraph?
- [ ] Are no "never" words present?

## Traps

- **"Humanizing" toward nobody.** Write toward the voiceprint, not toward "natural".
- **Voice smuggling in claims.** A new example or number added "for colour" is a new claim, and review will fail it.
