# 07 - review

Status: BUILT (session S003, 2026-09-28)

**Purpose:** judge one piece against a fixed set of checks, and return a binary verdict. PASS sends it to shaping. FAIL sends it back to the stage where the defect was born, with the defect named.

**Use when:** a child task arrives from `06 - drafting`. **Child tasks only.**

## Stages (run in order: each stage folder's `00 - ENTRY.md` is its instruction)

| # | Stage folder | One job | Writes |
|---|---|---|---|
| 1 | `01 - judge/` | Score every check; name the first failure and where it goes back to; on a PASS, name the crafted surplus | `07-review/01-review-report.md` |
| 2 | `02 - gate/` | PASS → carry forward and float. FAIL → send the task back with its reason | the `CONTEXT.md` section, `07-review/gate.md` |
| — | `work/` | Child tasks at this node | — |

## Writes (checked by `00 - control/02 - tools/task.py check`)

| File in the task folder | Stage |
|---|---|
| `07-review/01-review-report.md` | 1 |
| `CONTEXT.md#07 - review` | 2 |
| `07-review/gate.md` | 2 |

## Passes to

`08 - shaping` on a PASS. On a FAIL, back to `05 - research` or `06 - drafting`, as routed.

## Past material merged here

| From (now in `99 - archive/2026-09-28-restructure/`) | Became |
|---|---|
| `01 - writing-department/01 - prompt-library/05 - PROMPT_perfection_gate.md` | `01 - judge/gate-prompt.md` (verbatim) |
| `01 - writing-department/OUTPUT_CONTRACT.md` gates 1–7 (gate 7 = crafted surplus) | The G-checks and P1 in `01 - judge/` |
| `00 - control/01 - law/PERFECTIONISM_ENFORCEMENT.md` (the SURPLUS line; the anti-theater clause) | The surplus rule in `01 - judge/` |
