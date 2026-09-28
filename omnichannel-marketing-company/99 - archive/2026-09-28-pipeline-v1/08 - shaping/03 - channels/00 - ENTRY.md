# 03 · Channels

**Purpose:** write one native variant for each channel in the piece's plan, each in its own sub-folder's rules, and list them in one index.

## Contract

- **Reads:** `00-brief.md` (Channels and image slots); `08-shaping/01-seeds.md`, `02-hub-article.md`; the Voice section of the brief.
- **Writes:** `08-shaping/03-channels/<channel>.md` (one per channel in the brief) and `08-shaping/03-channel-index.md`.
- **Done when:** every channel in the brief has a variant, and the index lists each one's seeds, image slots and status.

## Procedure

1. **Run only the channel sub-folders listed in the brief's Channels.** Each sub-folder's `00 - ENTRY.md` is that channel's instruction:

   | Sub-folder | Channel |
   |---|---|
   | `01 - linkedin/` | LinkedIn post |
   | `02 - twitter-x/` | Twitter/X thread |
   | `03 - threads/` | Threads post |
   | `04 - facebook/` | Facebook post |
   | `05 - instagram/` | Instagram carousel |
   | `06 - medium/` | Medium republish |
   | `07 - website/` | Website summary page or landing block |
   | `08 - email/` | Email |
   | `09 - ads/` | Ad creative and copy |
   | `10 - sales-collateral/` | One-pager or catalogue copy |

2. **Head each variant file** with its metadata block:

       # <Channel> — <piece slug>
       Seeds: … · Angle: … · Week: … · Link to hub: <placement> · Image slots: <IDs> · Status: text-complete
       ---
       <the paste-ready content>

3. **Write in the client's voice.** Take the voiceprint and word lists from the brief. Voice checks at the gate apply to every variant.
4. **Never paste a sentence from the hub article or from another variant.** Re-say it natively.
5. **Missing client facts** (product details, prices, contact details) are written as `[CLIENT TO SUPPLY: <what>]`, never invented. The variant's status then reads `text-complete, needs client input`.
6. **Write the index.**

## Output template

    # Channel index — <task id>
    | Channel | File | Seeds | Image slots | Status |

## Self-check

- [ ] Does every channel in the brief have a variant, and no channel outside it?
- [ ] Does every variant have its metadata block?
- [ ] Is every missing fact marked CLIENT TO SUPPLY?

## Traps

- **Running every sub-folder.** Only the channels in the plan get variants.
- **One text, ten formats.** Channel rules change the words, not just the line breaks.
