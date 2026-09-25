# LinkedIn Layer — Output Contract

## Required Output Structure

Every LinkedIn derivative publication produces the following artifacts. The LinkedIn post itself is the derivative; the accompanying artifacts make it traceable back to the Substack master source and forward to business-development impact.

### 1. LinkedIn Post (mandatory)

```
[linkedin-slug]/
├── post.md                   ← The published LinkedIn post (derivative)
├── metadata.json             ← Post type, template, seeds used, LinkedIn URL, Substack link placement, vertical tag, publication date
├── visual-assets/            ← Custom graphics / visual frameworks / branded content (from Media Department)
│   └── asset-N.[png|jpg|pdf]
└── impact-log.md             ← Optional: record of client-acquisition / partnership / recruitment / speaking / business-dev references to this post
```

### 2. Metadata (mandatory)

`metadata.json` must contain all of the following fields:

| Field | Purpose |
|---|---|
| `post_type` | One of: thought-leadership, industry-commentary, case-study-breakdown, contrarian-insight, legal-consulting-perspective, founder-lesson, framework-driven-educational |
| `template_path` | Path to the template used (under `.\..\05 - templates\`) |
| `seeds_used` | Array of 1-3 seed names (core-insight, process, contrarian, framework, implication, visual) |
| `linkedin_url` | Live post URL |
| `substack_source_url` | Upstream Substack article URL |
| `substack_funnel_placement` | `first-comment` or `post-body` (per week-based funnel discipline) |
| `vertical_tag` | One of: law, arbitration, litigation, startup-consulting, advisory, research, professional-services, general |
| `publication_date` | ISO 8601 date |
| `week_in_30day_framework` | 1, 2, 3, or 4 |

### 3. Visual Assets (mandatory)

Every LinkedIn post must have at least one visual asset from the Media Department. The visual asset must be:
- Custom (not stock imagery without provenance).
- Professional-credibility-aligned (no meme-style visuals).
- Referenced inline in `post.md` at an appropriate anchor point.

### 4. Impact Log (optional, recommended)

`impact-log.md` records real-world references to the post in business-development contexts. Entries are append-only:

```
[YYYY-MM-DD] Referenced in [client-acquisition | partnership | recruitment | speaking | business-dev] for [opportunity name].
```

## Non-negotiable rules

1. **Translation, not syndication.** Every LinkedIn post must be a NEW piece of content written in LinkedIn's professional register. Copy-pasting from Substack is a governance violation (per `.\..\WORKING_RULES.md` Rule 1).
2. **Substack is canonical.** The Substack article is the master source. The LinkedIn post declares canonical-link-to-Substack (either in first comment or in body per week discipline).
3. **No orphan posts.** Every LinkedIn post must trace to at least one Substack decomposition seed. A post without a seed reference is ad hoc and incomplete.
4. **Visual assets mandatory.** Every post has at least one Media-Department-produced visual asset. No stock imagery without provenance.
5. **Vertical-tag mandatory.** Every post for a knowledge-based vertical (law, arbitration, litigation, startup-consulting, advisory, research, professional-services) must declare its vertical tag. Posts outside these verticals use `general`.
6. **30-day framework discipline.** Every post declares its week-in-30day-framework (1, 2, 3, or 4). Posts cannot be published out of sequence without explicit reason recorded in metadata.

## Output verification

A LinkedIn derivative is complete only when all of the following are true:

| # | Check | How | Fail Action |
|---|---|---|---|
| 1 | Post on LinkedIn | Verify `metadata.json` `linkedin_url` returns 200 | Publish or re-publish |
| 2 | Metadata complete | All 9 fields in metadata.json present and non-empty | Fill missing fields |
| 3 | Seed traceable | `seeds_used` references a seed in Substack `decomposition-seeds.md` | Rewrite or link correct seed |
| 4 | Translation discipline | Rule 1 test: native LinkedIn user would find it natural | Rewrite |
| 5 | Visual asset present | `visual-assets/asset-1.*` exists and is referenced in post | Request from Media Department |
| 6 | Funnel to Substack | Substack link present in first comment OR post body per week discipline | Add link in correct placement |
| 7 | Vertical-tag declared | `vertical_tag` in metadata matches a knowledge vertical or `general` | Fill field |

## Output location rules

- **LinkedIn derivative artifacts** land in `.\drafts\[linkedin-slug]\` (one folder per post).
- **Published URL** recorded in `metadata.json` `linkedin_url`.
- **Substack article's metadata.json `downstream_derivatives` array** updated with `{platform: "linkedin", url: linkedin_url}`.

## Update rule

When the output contract changes, update this file first, then update `.\WORKFLOW.md` if the workflow steps change, then update `.\..\WORKING_RULES.md` if a department rule is affected, then update `.\..\00 - ENTRY.md` if ancestry changes.
