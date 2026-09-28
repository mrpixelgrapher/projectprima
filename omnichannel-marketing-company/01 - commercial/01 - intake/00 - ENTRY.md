# 01 - intake

Status: BUILT (session S003, 2026-09-28; v2 after the design lock)

**Purpose:** turn one raw client request into a task that knows what the client said, what it could mean, and every fact scope and pricing need — asked of the client and answered, round by round, before the task moves. It is the company's front door.

**Use when:** a new request arrives (a message, an email, call notes). One request makes one task, on the `engagement` route.

**Never here:** research (it goes to ARENA at discovery), recommendations, prices, or answering our own questions.

## Stages (run in order: each stage folder's `00 - ENTRY.md` is its instruction)

| # | Stage folder | One job | Writes |
|---|---|---|---|
| 1 | `01 - capture/` | Store the request verbatim; the operator creates the task and the client folder | `TASK.md`, `CONTEXT.md`, `11-intake/00-request.md` |
| 2 | `02 - parse/` | Break the request into statements, readings and the 13 brief slots | `11-intake/01-parse.md` |
| 3 | `03 - frame/` | Decide brand mode, horizon, outputs and execution, or name the question that decides each | `11-intake/02-frame.md` |
| 4 | `04 - questions/` | Route every open item to the client, to research or to a stated assumption; send the client questions and hold | `11-intake/03-routing.md`, `11-intake/04-questions-round-N-for-client.md`, `11-intake/05-research-questions.md` |
| 5 | `05 - answers/` | Turn the client's reply into slot values; settle the frame; ask the next round until the intake slots are Known | `11-intake/06-slot-board.md` |
| 6 | `06 - gate/` | Check; carry forward; publish the client profile; advance | the `CONTEXT.md` section, `11-intake/gate.md`, `clients/<client>/profile.md` |
| — | `work/` | Tasks at this node | — |

Shared definitions: `00 - control/01 - law/BRIEF_SLOTS.md` (slots), `TASK_CONTRACT.md` (IDs, tags, states), `HANDOFFS.md` (H1, the client hand-off).

## Writes (checked by `00 - control/02 - tools/task.py check`)

| File in the task folder | Stage |
|---|---|
| `TASK.md` | 1 |
| `11-intake/00-request.md` | 1 |
| `11-intake/01-parse.md` | 2 |
| `11-intake/02-frame.md` | 3 |
| `11-intake/03-routing.md` | 4 |
| `11-intake/04-questions-round-1-for-client.md` | 4 |
| `11-intake/05-research-questions.md` | 4 |
| `11-intake/06-slot-board.md` | 5 |
| `CONTEXT.md#11-intake` | 6 |
| `11-intake/gate.md` | 6 |

## Passes to

`01 - commercial/02 - scope`, only when every slot first needed at intake (SPEAKER, BRAND, OFFER in one line, GOAL, CHANNELS, LIMITS: budget and timeline, EXECUTION, LANGUAGE) is Known. The task waits here, round after round, until they are. Nothing is skipped: a scope built on a guess fails later.

## Past material merged here

| From | Became |
|---|---|
| `99 - archive/2026-09-28-restructure/00-control/carbon-input/CARBON_INPUT_FORM-001.md` and `-002.md` (structured options, a marked recommendation, max 4 questions) | The client-question rules and template in `04 - questions/` |
| `99 - archive/2026-09-28-restructure/02-sourcing/01 - dossiers/D-001-buyer-and-problem/DOSSIER.md` (numbered, self-contained queries with conditions) | The research-question template in `04 - questions/`; the questions go to ARENA at discovery |
| `99 - archive/2026-09-28-restructure/01-foundation/META/slot-map.md`, `99 - archive/2026-09-28-restructure/00-control/asset-intake.md` (the six-slot model) | The 13 brief slots in `00 - control/01 - law/BRIEF_SLOTS.md`, which `02 - parse/` fills |
| `99 - archive/2026-09-28-restructure/03 - architecture-governance/function-design-flow-analysis.md` (a raw idea becomes a packet; each stage writes its declared outputs and stops) | The task folder, the stage convention, and `gate.md` |
| Pipeline v1 `99 - archive/2026-09-28-pipeline-v1/02 - discovery/01 - answers/` | `05 - answers/`: answers are now taken at intake, because the line is sequential |
