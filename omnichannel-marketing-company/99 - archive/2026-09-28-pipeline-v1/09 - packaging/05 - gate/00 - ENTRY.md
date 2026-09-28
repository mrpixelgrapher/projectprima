# 05 · Gate

**Purpose:** confirm the package is complete and honest about what is waiting. Then float it to delivery.

## Contract

- **Reads:** everything in `09-packaging/`.
- **Writes:** the `## 09 - packaging` section of `CONTEXT.md`; `09-packaging/gate.md`.
- **Done when:** `gate.md` says `VERDICT: PASS` and the task has advanced.

## Procedure

1. **Run the checks in order.** Stop at the first failure.

   | # | Check | On failure |
   |---|---|---|
   | K1 | Every child is under `pieces/`, and the join report has a row for each | stage 1 |
   | K2 | Every piece has a kit file for every channel in the plan, with a publish block, the hub first | stage 2 |
   | K3 | Every PARTIAL piece has `partial_publication.yaml` | stage 2 |
   | K4 | The schedule places every kit file once, with no two channels of one piece on the same day | stage 3 |
   | K5 | The package page has all six sections, and lists every waiting item | stage 4 |

2. **Write the carry-forward:**

       ## 09 - packaging
       - Package: N pieces × M channels; COMPLETE: … · PARTIAL: … (why) [09-packaging/02-kit-index.md]
       - Schedule: Day 1 = …; runs N days [09-packaging/03-schedule.md]
       - Waiting: images N (no producer) · client to supply: … [09-packaging/00-package.md]

3. **Write `gate.md`** (the five-line format in `00 - control/01 - law/TASK_CONTRACT.md` §2), then run `python3 "00 - control/02 - tools/task.py" advance <parent-id>`.

## Self-check

- [ ] Does the package state PARTIAL wherever anything is waiting?

## Traps

- **Hiding the partial.** A client who discovers missing images after publishing loses trust. Say it on page one.
