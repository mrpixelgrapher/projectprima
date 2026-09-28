# 02 · Hub

**Purpose:** make the canonical, hub-ready version of the article and its metadata. Every spoke points back to this version.

## Contract

- **Reads:** `06-drafting/02-article.md`; `07-review/01-review-report.md` (the SURPLUS line); `05-research/02-boundary-map.md` (the keyword); `00-brief.md` (cluster, links, CTA); `article-template.md` in this folder.
- **Writes:** `08-shaping/02-hub-article.md`, `08-shaping/02-hub-metadata.md`.
- **Done when:** the article follows the template, every LINK and GRAPHIC marker is resolved, and every metadata field is filled.

## Procedure

1. **Lay the article into `article-template.md`.** Change no argument or sentence, except to resolve the markers below.
2. **Resolve the link markers.** Replace each `[LINK: <slug>]` with a paste instruction: `[link to "<title of that piece>" — paste its hub URL once published]`. The first piece in a cluster has none; the second links to the first; from the third on, each links to at least 2.
3. **Resolve the graphic markers.** The first `[GRAPHIC: …]` becomes the `featured` slot; the rest become `inline-1`, `inline-2`…. Keep the description, for `04 - visuals/`.
4. **Close.** Add the subscribe line and the brief's CTA.
5. **Audit trail.** Fill it, including `SURPLUS:` copied from the review report.
6. **Metadata:**

   | Field | Rule |
   |---|---|
   | title | ≤ 70 characters, with the keyword near the front |
   | meta description | 150–160 characters: the problem and the promise |
   | keywords | 3–5, the confirmed keyword first |
   | cluster | the brief's cluster; the cornerstone is its index |
   | week | the piece's start week |
   | upstream research | `05-research/` |
   | downstream variants | the channels from the brief (URLs are added after posting) |
   | hub URL | blank until published |

## Output template

`02-hub-article.md` follows `article-template.md`. `02-hub-metadata.md`:

    # Hub metadata — <task id>
    | Field | Value |

## Worked example

*(illustrative)* Title: "Real or fake gemstone gifts: the 60-second check for HR" (56 characters). Meta description: "HR teams buying festival gifts can't tell real gemstones from fakes. Here's how to check any lab report in a minute before you order." (Count it at the time of writing, and trim to 150–160.)

## Self-check

- [ ] Is the title ≤ 70 characters, with the keyword near the front?
- [ ] Is the meta description 150–160 characters?
- [ ] Is every LINK marker a paste instruction, and every GRAPHIC marker a slot ID?
- [ ] Does the audit trail carry the SURPLUS line?

## Traps

- **Rewriting at the hub.** The review passed this text. Change only the markers and the metadata.
- **Links to pieces that don't exist yet.** Follow the first-piece rule.
