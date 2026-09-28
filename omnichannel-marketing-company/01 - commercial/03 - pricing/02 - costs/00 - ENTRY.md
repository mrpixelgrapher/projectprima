# 02 · Costs

**Purpose:** add what is paid for outside the work (image generation, motion generation, tools), so no deliverable is priced below what it costs to make.

## Contract

- **Reads:** `12-scope/01-deliverables.md`; `13-pricing/01-rates.md` (unit costs).
- **Writes:** `13-pricing/02-costs.md`.
- **Done when:** every deliverable that consumes a unit cost has a cost line; deliverables with no cost say "none".

## Procedure

1. **For each deliverable,** count its costed units: stills (image factory), motion clips (one per transition in a video; estimate 6 per video until the video factory reports actuals), and any tool named in `01-rates.md`.
2. **Multiply** units × unit cost. Pass-through costs are billed at cost unless the operator's rates file sets a margin; if it does, apply it and show it.
3. **Sum** per deliverable, and for setup, monthly base and each add-on.

## Output template

    # Costs — <task id>
    | D | Cost | Units | Unit cost | Margin | Amount | Source |
    ## Totals
    | Block | Costs |

## Worked example

*(illustrative)* D1 core pieces × 6 → 18 stills × 40 = 720, no margin, source [13-pricing/01-rates.md].

## Self-check

- [ ] Does every deliverable with stills, clips or tools have a cost line?
- [ ] Is every unit cost from `01-rates.md`?

## Traps

- **Forgetting stills in text channels.** Every piece carries images; count them.
