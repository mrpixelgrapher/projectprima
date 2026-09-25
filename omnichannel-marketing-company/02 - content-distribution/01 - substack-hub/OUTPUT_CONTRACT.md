# Substack Hub — Output Contract

## Required Output Structure

Every Substack Hub publication produces the following artifacts. The Substack article itself is the master source; the accompanying artifacts make it consumable by downstream layers and traceable back to upstream inputs.

### 1. Substack Article (mandatory)

```
[substack-slug]/
├── article.md                ← The published Substack article (canonical source)
├── metadata.json             ← SEO title, meta description, keywords, cluster tag, publication date, Substack URL
├── visual-assets/            ← Inline images + featured image (from Media Department)
│   ├── featured.[png|jpg]
│   └── inline-N.[png|jpg]
└── decomposition-seeds.md    ← 6 seeds for downstream platform derivatives
```

### 2. Metadata (mandatory)

`metadata.json` must contain all of the following fields:

| Field | Purpose |
|---|---|
| `title` | SEO-optimized title (≤70 characters, primary keyword first) |
| `meta_description` | 150-160 character summary for search engines |
| `keywords` | Array of 3-5 target SEO keywords |
| `cluster_tag` | Content-cluster identifier (from the cluster taxonomy in WORKFLOW.md) |
| `publication_date` | ISO 8601 date |
| `substack_url` | Live publication URL |
| `upstream_article_path` | Path to Writing Department source article |
| `upstream_research_path` | Path to research folder |
| `downstream_derivatives` | Array of `{platform, url}` objects — populated as derivatives publish |

### 3. Decomposition Seeds (mandatory)

`decomposition-seeds.md` must contain exactly 6 seeds, each with a one-sentence core and a 2-3 sentence development:

| Seed | Downstream consumer |
|---|---|
| Core insight | LinkedIn (B2B thought leadership) + Medium (condensed takeaway) |
| Process breakdown | Twitter/X (how outcomes were achieved) |
| Contrarian perspective | LinkedIn + Twitter/X (disruption framing) |
| Framework | LinkedIn (educational) + Instagram (visual carousel) |
| Implication / discussion | Threads (deeper conversation) |
| Visual concept | Instagram + Facebook (visual storytelling) |

Every seed must be extractable without reading the full article — a downstream layer can take the seed and produce a platform-native derivative from it alone.

### 4. Internal Links (mandatory)

Every Substack article must contain at least two internal links to previous articles in the same content cluster. This is the compounding-SEO discipline — every new article strengthens the visibility and credibility of previous work.

## Non-negotiable rules

1. **No orphan Substack articles.** Every article must be accompanied by `metadata.json` and `decomposition-seeds.md`. An article without these artifacts is incomplete.
2. **Research-first gate enforced.** The Writing Department's pre-drafting gate must have passed before the article reaches Substack. The metadata must reference the gate evidence.
3. **Visual assets from Media Department.** Every Substack article has at least one featured image and inline visual assets produced by the Media Department's output contract. No stock imagery without provenance.
4. **Substack is canonical.** If the same content appears elsewhere (website, Medium), the Substack version is the canonical source. Other versions declare canonical-link-to-Substack in their metadata.
5. **Cluster tag mandatory.** Every article declares at least one cluster tag. Articles without a cluster tag violate the archive-building discipline.
6. **Decomposition seeds are actionable.** Each seed is self-contained enough to produce a platform-native derivative without re-reading the article. If a seed requires the full article to interpret, it is not a seed — rewrite it.

## Output verification

A Substack Hub publication is complete only when all of the following are true:

| # | Check | How | Fail Action |
|---|---|---|---|
| 1 | Article on Substack | Verify `metadata.json` `substack_url` returns 200 | Publish or re-publish |
| 2 | Metadata complete | All 8 fields in metadata.json present and non-empty | Fill missing fields |
| 3 | 6 decomposition seeds | Count seeds in `decomposition-seeds.md` | Write missing seeds |
| 4 | Internal links present | Count internal cluster links in `article.md` (≥ 2) | Add links to cluster peers |
| 5 | Visual assets present | `visual-assets/featured.*` exists and is referenced in article | Request from Media Department |
| 6 | Research-first gate passed | `metadata.json` `upstream_research_path` points at a real research folder with sources/observations/synthesis | Return to Writing Department |
| 7 | Canonical-link discipline | If website/Medium versions exist, they declare canonical-to-Substack | Update website/Medium metadata |

## Output location rules

- **Substack-hub artifacts** land in `.\drafts\[substack-slug]\` (one folder per publication).
- **Published URL** recorded in `metadata.json` `substack_url`.
- **Downstream derivative URLs** recorded in `metadata.json` `downstream_derivatives` as each layer publishes.

## Update rule

When the output contract changes, update this file first, then update `.\WORKFLOW.md` if the workflow steps change, then update `.\..\WORKING_RULES.md` if a department rule is affected, then update `.\..\00 - ENTRY.md` if ancestry changes.
