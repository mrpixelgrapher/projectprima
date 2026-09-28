# 03 · Gate

**Purpose:** the pre-drafting gate. Drafting starts only when the research is wide enough, the spine is original, and the evidence is on disk.

## Contract

- **Reads:** every file in `05-research/`; `00-brief.md`.
- **Writes:** the `## 05 - research` section of `CONTEXT.md`; `05-research/gate.md`.
- **Done when:** `gate.md` says `VERDICT: PASS` and the task has advanced, **or** it says HOLD with the reason.

## Procedure

1. **Run the checks in order.** Stop at the first failure.

   | # | Check | On failure |
   |---|---|---|
   | R1 | Sources span ≥ 3 independent categories | stage 1 |
   | R2 | ≥ 5 observations, each citing ≥ 1 L-ID | stage 1 |
   | R3 | The boundary map's saturation says YES; sector 5 has ≥ 12 particulars | stage 1 |
   | R4 | The spine has all six parts; the originality check says NONE | stage 2 |
   | R5 | Every spine claim has particulars; no `[VERIFY]` item is used as evidence | stage 2 |
   | R6 | There is no pillar conflict, or the operator's decision on it is logged in `client/` or in History | **HOLD** (waiting on the operator) |

2. **On a PASS, write the carry-forward** (at most 10 bullets, each with its source):

       ## 05 - research
       - The one thing: "…" [05-research/04-spine.md]
       - Spine: 1 … · 2 … · 3 … [05-research/04-spine.md]
       - Tension: … [05-research/04-spine.md]
       - Keyword: … [05-research/02-boundary-map.md]
       - Sources: N across categories … [05-research/01-sources.md]

3. **Write `gate.md`** (the five-line format in `00 - control/01 - law/TASK_CONTRACT.md` §2). On a PASS, run `python3 "00 - control/02 - tools/task.py" advance <task-id>`.

## Self-check

- [ ] Was every check run against the files, not from memory?

## Traps

- **"Good enough" research.** Drafting will feel hard, and the piece will read hollow. A HOLD here is cheaper.
