# 01 - intake

Status: BUILT (session S003, 2026-09-28)

**Purpose:** turn one raw client request into a task folder that separates three things (what the client said, what it could mean, and what we must ask), so that every later node works from the client's words and not from our first guess.

**Use when:** a new request arrives (a message, an email, call notes). One request makes one task.

**Never here:** research, recommendations, or answering our own questions. Those belong to later nodes.

## Stages (run in order: each stage folder's `00 - ENTRY.md` is its instruction)

| # | Stage folder | One job | Writes |
|---|---|---|---|
| 1 | `01 - capture/` | Store the request verbatim; the operator creates the task folder | `TASK.md`, `CONTEXT.md`, `01-intake/00-request.md` |
| 2 | `02 - parse/` | Break the request into statements, readings and the 12 brief slots | `01-intake/01-parse.md` |
| 3 | `03 - frame/` | Decide brand mode, horizon, outputs and execution, or name the question that decides each | `01-intake/02-frame.md` |
| 4 | `04 - questions/` | Route every open item to the client, to research, or to a stated assumption; write the client file | `01-intake/03-routing.md`, `01-intake/04-client-questions.md`, `01-intake/05-research-questions.md` |
| 5 | `05 - gate/` | Check the work, write the carry-forward, and float the task | the `CONTEXT.md` section, `01-intake/gate.md` |
| — | `work/` | Tasks currently at this node | — |

Shared definitions: the slots are in `00 - control/01 - law/BRIEF_SLOTS.md`; the IDs, tags and states are in `00 - control/01 - law/TASK_CONTRACT.md`.

## Writes (checked by `00 - control/02 - tools/task.py check`)

| File in the task folder | Step |
|---|---|
| `TASK.md` | 1 |
| `01-intake/00-request.md` | 1 |
| `01-intake/01-parse.md` | 2 |
| `01-intake/02-frame.md` | 3 |
| `01-intake/03-routing.md` | 4 |
| `01-intake/04-client-questions.md` | 4 |
| `01-intake/05-research-questions.md` | 4 |
| `CONTEXT.md#01 - intake` | 5 |
| `01-intake/gate.md` | 5 |

## Passes to

`02 - discovery`. The task may leave with its client questions still unanswered: intake asks; it doesn't wait. Each question names the node that needs its answer, and that node's gate holds the task.

**Send unit:** `01-intake/04-client-questions.md` goes to the client as-is (never for a `rehearsal` task).

## Past material merged here

| From (now in `99 - archive/2026-09-28-restructure/`) | Became |
|---|---|
| `00-control/carbon-input/CARBON_INPUT_FORM-001.md` and `-002.md` (the CARBON_INPUT_FORM format: structured options, a marked recommendation, max 4 questions) | The client-question rules and template in `04 - questions/` |
| `02-sourcing/question_bank.md`, `02-sourcing/01 - dossiers/D-001-buyer-and-problem/DOSSIER.md` (numbered, self-contained, runnable queries with conditions) | The research-question template in `04 - questions/` |
| `01-foundation/META/slot-map.md` and `00-control/asset-intake.md` (the six-slot model: leverage actor, buyer path, offer, tool route, channel split, proof) | The 12 brief slots in `00 - control/01 - law/BRIEF_SLOTS.md`, which `02 - parse/` fills |
| `01 - writing-department/01 - prompt-library/01 - PROMPT_boundary_research.md` (sector 7, the reader's wrong model; `[VERIFY]` instead of invention) | The knowledge-leak trap and the no-outside-facts rule in `02 - parse/` |
| `03 - architecture-governance/function-design-flow-analysis.md` (a raw idea becomes a packet; each stage writes its declared outputs and stops; blocked stages still write their output) | The task folder, the stage convention, and `gate.md` with VERDICT PASS/HOLD |
