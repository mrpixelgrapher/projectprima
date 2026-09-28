# 07 · Gate

**Purpose:** confirm the design is complete and honest, publish it to the client folder, and move to planning.

## Contract

- **Reads:** `23-performance/*.md`.
- **Writes:** the `## 23-performance` section of `CONTEXT.md`; `23-performance/gate.md`; `clients/<client>/performance.md`.
- **Done when:** the task has advanced with the design published.

## Procedure

1. **Checks, in order:**

   | # | Check | On failure |
   |---|---|---|
   | PF1 | The baseline or last month's results are sourced; every test has a decision | 01 - results |
   | PF2 | Every principle used has its true basis; Act points to the destination's one action | 02 - conversion |
   | PF3 | Every channel has its triggers, hooks, format and cadence, citing the library or a result | 03 - virality |
   | PF4 | 1–2 tests, one variable each, ≥ 4 posts per variant | 04 - tests |
   | PF5 | The tag scheme is set; the report list is ≤ 8 numbers | 05 - tracking |
   | PF6 | The design file compresses the stages with no new decisions | 06 - design |

2. **Carry forward** (at most 8 bullets): the weakest link and its change; the principles per stage in short; hooks first per channel; tests; the tag scheme; the report list.
3. **Publish** `06-performance-design.md` to `clients/<client>/performance.md` (old one to `versions/` first).
4. **Write `gate.md`** (five-line format), then `task.py advance <task-id>`.

## Self-check

- [ ] Is every persuasion principle backed by something true?

## Traps

- **Passing a design writers can't apply.** If "Rules for writing" is vague, PF6 fails.
