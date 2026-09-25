# Facebook Layer — Output Contract

## Required Output Structure

Every Facebook derivative produces the following artifacts. The Facebook post itself is the derivative; the accompanying artifacts make it traceable back to the Substack master source and forward to the funnel targets.

### 1. Facebook Post (mandatory)

```
[facebook-slug]/
├── post.md                   ← The published Facebook post (derivative)
├── metadata.json             ← Persona, seed used, Facebook URL, funnel targets, SEO keywords, publication date
└── visual-assets/            ← Compelling custom graphics / visual storytelling (from Media Department)
    └── asset-N.[png|jpg]
```

### 2. Metadata (mandatory)

`metadata.json` must contain all of the following fields:

| Field | Purpose |
|---|---|
| `persona` | One of: mature-reader, approaching-retirement-professional, business-owner, investor, high-income-segment |
| `seed_used` | Seed name (core-insight, implication, or visual per Substack seed-to-platform mapping) |
| `facebook_url` | Live post URL |
| `substack_source_url` | Upstream Substack article URL |
| `funnel_targets` | Object with `substack_url`, optional `website_url`, optional `knowledge_base_url` |
| `seo_keywords` | Array of 2-4 SEO keywords from the Substack article's `metadata.json` |
| `publication_date` | ISO 8601 date |
| `week_in_30day_framework` | 1, 2, 3, or 4 (typically 2 or 3 for Facebook) |

### 3. Visual Assets (mandatory)

Every Facebook post has at least one compelling custom graphic from the Media Department:
- High-production-value.
- Storytelling-oriented (image that tells a story, not just illustrates a point).
- On-brand and professional-credibility-aligned.

No stock imagery without provenance.

## Non-negotiable rules

1. **Translation, not syndication.** Every Facebook post is a NEW piece of content written in Facebook's native register for the target persona. Copy-pasting from Substack or cross-posting identical content is a governance violation (per `.\..\WORKING_RULES.md` Rule 1).
2. **Substack is canonical.** The Substack article is the master source. The Facebook post declares canonical-link-to-Substack in post body.
3. **Persona discipline.** Every post is mapped to one of the five personas. Persona-less posts are incomplete.
4. **Seed traceability.** Every post traces to a Substack decomposition seed. A post without a seed reference is ad hoc.
5. **Visual discipline.** Every post has at least one compelling Media-Department-produced visual asset. High production value expected.
6. **SEO-informed messaging.** `seo_keywords` field populated with 2-4 keywords from the Substack article; post copy uses these keywords naturally.
7. **Funnel to controlled assets.** Every post links to at least Substack. Website and knowledge-base links optional but encouraged.
8. **Brand-narrative consistency.** Persona-aligned does not mean brand-deviant. Facebook posts must be recognizable as the same voice that publishes on LinkedIn, Twitter, and Threads.
9. **No same-day publication with other platform derivatives.** Facebook publication date for an article must differ from LinkedIn, Twitter, and Threads publication dates for the same article.

## Output verification

A Facebook derivative is complete only when all of the following are true:

| # | Check | How | Fail Action |
|---|---|---|---|
| 1 | Post on Facebook | Verify `metadata.json` `facebook_url` returns 200 | Publish or re-publish |
| 2 | Metadata complete | All 8 fields in metadata.json present and non-empty | Fill missing fields |
| 3 | Persona declared | `persona` in metadata matches one of the 5 personas | Declare persona |
| 4 | Seed traceable | `seed_used` references a seed in Substack `decomposition-seeds.md` | Link correct seed |
| 5 | Translation discipline | Rule 1 test: native Facebook user (of the target persona) would find it natural | Rewrite |
| 6 | Visual asset present | `visual-assets/asset-1.*` exists and is compelling | Request from Media Department |
| 7 | SEO keywords declared | `seo_keywords` array has 2-4 entries matching Substack's keywords | Fill field from Substack metadata |
| 8 | Funnel to Substack | Substack link in post body | Add link |
| 9 | Brand-narrative consistency | Voice recognizable across platforms | Rewrite |
| 10 | Same-day publication avoided | `publication_date` differs from LinkedIn, Twitter, Threads dates for same article | Reschedule |

## Output location rules

- **Facebook derivative artifacts** land in `.\drafts\[facebook-slug]\` (one folder per post).
- **Published URL** recorded in `metadata.json` `facebook_url`.
- **Substack article's metadata.json `downstream_derivatives` array** updated with `{platform: "facebook", url: facebook_url}`.

## Update rule

When the output contract changes, update this file first, then update `.\WORKFLOW.md` if the workflow steps change, then update `.\..\WORKING_RULES.md` if a department rule is affected, then update `.\..\00 - ENTRY.md` if ancestry changes.
