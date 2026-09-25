# Twitter/X + Threads Layer — Output Contract

## Required Output Structure

Every Twitter+Threads derivative pair produces the following artifacts for a single Substack article. The two platforms share one output folder because they come from the same Substack decomposition seeds.

### 1. Article-level folder (mandatory)

```
[article-slug]/
├── twitter-thread.md       ← The published Twitter/X thread (5-12 tweets, one tweet per line or section)
├── threads-post.md         ← The published Threads post (up to 500 chars + image)
├── metadata.json           ← Covers both platforms (see schema below)
└── visual-assets/
    ├── twitter-hero.[png|jpg]     ← Thread's opening visual (tweet 1 or 2)
    ├── threads-implication.[png|jpg]  ← Threads' implication visual (mandatory)
    └── [optional-process-infographic.png]  ← Optional process infographic for Twitter thread
```

### 2. Metadata (mandatory)

`metadata.json` must contain all of the following fields:

| Field | Purpose |
|---|---|
| `substack_source_url` | Upstream Substack article URL |
| `twitter_thread_url` | Live Twitter/X thread URL |
| `threads_post_url` | Live Threads post URL |
| `twitter_seed_used` | Seed name used for Twitter (must be `process` per seed-to-platform mapping) |
| `threads_seed_used` | Seed name used for Threads (must be `implication` per seed-to-platform mapping) |
| `twitter_tweet_count` | Number of tweets in thread (5-12) |
| `threads_post_length` | Character count of Threads post (≤ 500) |
| `twitter_publication_date` | ISO 8601 date |
| `threads_publication_date` | ISO 8601 date |
| `week_in_30day_framework` | 1, 2, 3, or 4 (both platforms share the same week slot; publication days differ) |

### 3. Visual Assets (mandatory)

| Platform | Required visual |
|---|---|
| Twitter/X | At least one custom graphic (the `twitter-hero`) |
| Threads | Mandatory custom graphic illustrating the implication (`threads-implication`) |

All visuals from Media Department. No stock imagery without provenance.

## Non-negotiable rules

1. **Translation, not syndication.** Each platform's content is a NEW piece written in that platform's native register. Copy-pasting from Substack or cross-posting identical content between Twitter and Threads is a governance violation (per `.\..\WORKING_RULES.md` Rule 1).
2. **Substack is canonical.** Both platforms funnel back to Substack. Twitter: final tweet of thread. Threads: direct link in post body.
3. **Seed-split discipline.** Twitter uses the `process` seed. Threads uses the `implication` seed. A derivative pair that uses the same seed on both platforms is a collapse violation — rewrite one.
4. **Audience-split discipline.** Twitter content is process / methodology / execution mechanics. Threads content is implications / outcomes / discussion. A process thread on Threads or an outcomes post on Twitter is a mismatch — swap or rewrite.
5. **Thread length discipline.** Twitter threads must be 5-12 tweets. Under 5 is not a thread. Over 12 loses attention.
6. **Threads post length discipline.** Threads posts must be ≤ 500 characters. Longer violates the platform's native form.
7. **Visual assets mandatory on both.** No text-only derivatives on either platform.
8. **No same-day publication.** Twitter and Threads derivatives for the same article must not publish on the same day (space them within the 30-day framework).

## Output verification

A Twitter+Threads derivative pair is complete only when all of the following are true:

| # | Check | How | Fail Action |
|---|---|---|---|
| 1 | Thread on Twitter | Verify `metadata.json` `twitter_thread_url` returns 200 | Publish or re-publish |
| 2 | Post on Threads | Verify `metadata.json` `threads_post_url` returns 200 | Publish or re-publish |
| 3 | Metadata complete | All 10 fields in metadata.json present and non-empty | Fill missing fields |
| 4 | Seed-split discipline | Twitter seed = `process`, Threads seed = `implication` | Rewrite mismatched derivative |
| 5 | Audience-split discipline | Twitter thread is process-focused; Threads post is outcome-focused | Rewrite or swap |
| 6 | Translation discipline (Twitter) | Native Twitter user would find the thread natural | Rewrite |
| 7 | Translation discipline (Threads) | Native Threads user would find the post natural | Rewrite |
| 8 | Thread length | `twitter_tweet_count` between 5 and 12 | Extend or condense |
| 9 | Threads length | `threads_post_length` ≤ 500 | Condense |
| 10 | Visual assets present | `twitter-hero.*` and `threads-implication.*` exist | Request from Media Department |
| 11 | Funnel to Substack | Twitter final tweet has Substack link; Threads post has Substack link | Add link in correct placement |
| 12 | Same-day publication avoided | `twitter_publication_date` ≠ `threads_publication_date` | Reschedule one |

## Output location rules

- **Article-level folders** land in `.\drafts\[article-slug]\` (one folder per Substack article).
- **Published URLs** recorded in `metadata.json` `twitter_thread_url` and `threads_post_url`.
- **Substack article's metadata.json `downstream_derivatives` array** updated with two entries: `{platform: "twitter", url: twitter_thread_url}` and `{platform: "threads", url: threads_post_url}`.

## Update rule

When the output contract changes, update this file first, then update `.\WORKFLOW.md` if the workflow steps change, then update `.\..\WORKING_RULES.md` if a department rule is affected, then update `.\..\00 - ENTRY.md` if ancestry changes.
