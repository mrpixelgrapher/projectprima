# 06 · Channels

**Purpose:** write one native variant per channel in the plan, for every piece, each by its own channel's craft in its sub-folder, and each sending readers to the destination. Omnichannel means every piece reaches every channel in the plan, re-said natively each time, never cross-posted.

## Contract

- **Reads:** the piece brief (`24-planning/briefs/<P>.md`: channels, dates, language, performance rules, CTA and tagged links); `24-planning/02-calendar.md`; `25-writing/<P>/06-article.md`, `08-seeds.md`; `23-performance/03-virality.md` (hooks first, format, triggers); `21-discovery/05-creator-library.md` (month task: `clients/<client>/creators.md`).
- **Writes:** `25-writing/<P>/channels/<channel>.md` (one per channel in the plan, per piece); the piece's row in `00-piece-index.md`.
- **Done when:** every piece has a variant for every channel in the plan (and none for other channels), each with its metadata block, and the index shows "channels: done".

## Procedure

1. **Run only the sub-folders for channels in the plan.** Each sub-folder's `00 - ENTRY.md` is that channel's craft:

   | Sub-folder | Channel |
   |---|---|
   | `01 - substack/` | Substack post (the full article when it is the long-form home) |
   | `02 - medium/` | Medium republish |
   | `03 - website-blog/` | Blog post on the client's site |
   | `04 - newsletter/` | Newsletter issue or email |
   | `05 - landing-page/` | The destination page (built once as setup; updated when the month needs it) |
   | `06 - linkedin/` | LinkedIn post |
   | `07 - x-twitter/` | X thread |
   | `08 - threads/` | Threads post |
   | `09 - facebook/` | Facebook post |
   | `10 - instagram/` | Instagram carousel or post |
   | `11 - pinterest/` | Pinterest pin |

2. **Head each variant** with its metadata block:

       # <Channel> — <P>-<slug>
       Date: <from the calendar> · Seed: … · Angle: … · Test variant: … · Language: …
       Link: <tagged link> (placement: …) · Image slots: <IDs> · Status: text-complete
       ---
       <the paste-ready content>

3. **Apply the performance design:** the hook forms to use first, the format, and the share, save and comment triggers for this channel (`23-performance/03-virality.md`); the call to action for the piece's path job. A test variant follows its variant exactly and nothing else changes.
4. **Write in the client's voice and in the channel's language.** A channel in a different language is written natively in it from the seeds, never translated from the article.
5. **Never paste a sentence from the article or from another variant.** Re-say it natively.
6. **Missing client facts** (product details, prices, contact details) are `[CLIENT TO SUPPLY: <what>]`, never invented. The status then reads `text-complete, needs client input`.
7. **Update `00-piece-index.md`** for the piece.

## Worked example

Gemstone P2 on Instagram *(illustrative)*: `Date: 2026-11-10 · Seed: framework · Angle: the three steps as three slides · Test variant: T1-A (price-in-headline cover) · Language: English · Link: bio link …&utm_content=P2-a · Image slots: carousel-1…7`.

## Self-check

- [ ] Does every piece have a variant for every channel in the plan, and none outside it?
- [ ] Does every variant carry its metadata block, tagged link and test variant?
- [ ] Is every missing fact marked CLIENT TO SUPPLY?

## Traps

- **Running every sub-folder.** Only the channels in the plan get variants.
- **One text, eleven formats.** Channel craft changes the words, not just the line breaks.
