# 05 · Tracking

**Purpose:** make every result traceable to the channel and piece that caused it, and fix the short list of numbers the client reports each month.

## Contract

- **Reads:** `22-strategy/03-destination.md`, `05-objectives.md`, `04-channel-plan.md`; `23-performance/04-tests.md`.
- **Writes:** `23-performance/05-tracking.md`.
- **Done when:** the link tag scheme is set, every objective's metric has a place it is read, and the monthly report list is at most 8 numbers.

## Procedure

1. **Link tags.** Every link to the destination carries: `utm_source=<channel>`, `utm_medium=organic`, `utm_campaign=<client>-<yyyy-mm>`, `utm_content=<piece id>-<variant>`. Where a platform allows one link only (e.g. Instagram's bio), use one tagged link per month and name the piece in the bio text.
2. **Where each number is read:** the destination (form entries, sign-ups, orders), the site or newsletter analytics (visits by source), each platform's post insights (saves, shares, comments, reach).
3. **The monthly report list** (what `01 - commercial/05 - month-review/01 - results/` asks for): each objective's metric; destination visits by channel; each test's metric per variant; the top 3 posts per channel. At most 8 numbers. Nothing else.
4. **Who sets it up:** the tagged links are written into every piece by writing; if the destination needs an analytics or form setting, name it as a client action (or ours, if the destination build is ours).

## Output template

    # Tracking — <task id>
    Tag scheme: …
    | Number | Read where | Serves (objective / test) |
    Monthly report list (≤ 8): …
    Setup actions: …

## Worked example

*(illustrative)* `utm_source=instagram&utm_medium=organic&utm_campaign=gemstone-seller-2026-11&utm_content=P3-a` · report list: catalogue requests; landing-page visits by source; saves per carousel (T1 A vs B); top 3 posts on Instagram.

## Self-check

- [ ] Does every objective and test have a number and a place to read it?
- [ ] Is the report list at most 8 numbers?

## Traps

- **Measuring what's easy.** Likes are easy; the objective is the destination's action.
