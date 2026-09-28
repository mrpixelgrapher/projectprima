# 04 · Gate

**Purpose:** confirm the package is complete and honest about what is waiting. Then advance.

## Contract

- **Reads:** everything in `26-packaging/`.
- **Writes:** the `## 26-packaging` section of `CONTEXT.md`; `26-packaging/gate.md`.
- **Done when:** `gate.md` says `VERDICT: PASS` and the task has advanced.

## Procedure

1. **Run the checks in order.** Stop at the first failure.

   | # | Check | On failure |
   |---|---|---|
   | K1 | Every calendar post has a kit file with a publish block; the text equals the passed variant | 01 - kit |
   | K2 | Every image and video referenced is in the kit | 01 - kit |
   | K3 | Every PARTIAL channel folder has its `partial_publication.yaml` | 01 - kit |
   | K4 | The schedule places every kit file once; counts match the engagement | 02 - schedule |
   | K5 | The package page has all six sections and lists every waiting item | 03 - package |

2. **Write the carry-forward:**

       ## 26-packaging
       - Package: <month>, N pieces × M channels; COMPLETE: … · PARTIAL: … (why) [26-packaging/01-kit-index.md]
       - Schedule: <first date> – <last date>; posted by <us / client> [26-packaging/02-schedule.md]
       - Waiting: client to supply … [26-packaging/03-package.md]

3. **Write `gate.md`** (the five-line format in `00 - control/01 - law/TASK_CONTRACT.md` §2), then run `python3 "00 - control/02 - tools/task.py" advance <task-id>`.

## Self-check

- [ ] Does the package say PARTIAL wherever anything is waiting?

## Traps

- **Hiding the partial.** A client who discovers a gap after posting loses trust. Say it on page one.
