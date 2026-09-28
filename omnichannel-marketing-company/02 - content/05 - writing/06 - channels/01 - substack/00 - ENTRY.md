# Substack

**Purpose:** the piece as a Substack post: the full article when Substack is the long-form home (usually also the destination, as the newsletter people subscribe to), or a republished version that points to the long-form home.

## Contract

- **Reads:** `25-writing/<P>/06-article.md`; `25-writing/<P>/07-review.md` (the SURPLUS line); `25-writing/<P>/02-boundary-map.md` (the keyword); the piece brief (`24-planning/briefs/<P>.md`: topic, links, CTA); `22-strategy/04-channel-plan.md`; `article-template.md` in this folder.
- **Writes:** `25-writing/<P>/channels/substack.md`.
- **Done when:** the post follows the template, every LINK and GRAPHIC marker is resolved, and every metadata field is filled.

## Procedure

1. **Lay the article into `article-template.md`.** Change no argument or sentence, except to resolve the markers below. If Substack is not the long-form home, add a first line pointing to the full piece, and keep the article at most 1,500 words by cutting whole sections (never rewording the argument).
2. **Resolve the link markers.** Replace each `[LINK: <slug>]` with a paste instruction: `[link to "<title of that piece>" — paste its URL once published]`. The first piece of a topic has none; the second links to the first; from the third on, each links to at least 2.
3. **Resolve the graphic markers.** The first `[GRAPHIC: …]` becomes the `featured` slot; the rest become `inline-1`, `inline-2`…. Keep each description for `08 - visuals/`.
4. **Close.** The subscribe line (if Substack is the destination), and the brief's CTA with its tagged link.
5. **Audit trail.** Fill it, including `SURPLUS:` copied from the review. It is removed before posting (packaging keeps it in the kit's log).
6. **Metadata:**

   | Field | Rule |
   |---|---|
   | title | ≤ 70 characters, with the keyword near the front |
   | subtitle / meta description | 150–160 characters: the problem and the promise |
   | keywords | 3–5, the confirmed keyword first |
   | topic | the brief's topic |
   | date | from the calendar |
   | URL | blank until published |

## Output template

The metadata block from `../00 - ENTRY.md`, then the metadata table, then the post in `article-template.md`'s layout.

## Worked example

*(illustrative)* Title: "Real or fake gemstone gifts: the 60-second check for HR" (56 characters). Subtitle: "HR teams buying festival gifts can't tell real gemstones from fakes. Here's how to check any lab report in a minute before you order." (Count it when writing; trim to 150–160.)

## Self-check

- [ ] Is the title ≤ 70 characters, with the keyword near the front?
- [ ] Is every LINK marker a paste instruction, and every GRAPHIC marker a slot ID?
- [ ] Does the audit trail carry the SURPLUS line?

## Traps

- **Rewriting the reviewed article.** Change only the markers, the close and the metadata.
- **Links to pieces that don't exist yet.** Follow the first-piece rule.
