# Instruction Standard

**Purpose:** the bar every instruction file in this company must meet. Use it when you write a stage, and when you review one.

## Folder convention

| Level | Folder | Its `00 - ENTRY.md` says |
|---|---|---|
| Root | `omnichannel-marketing-company/` | What the company does, the line of nodes, how to start |
| Node | `NN - <node>/` (01–10) | The node's one job, its stages in order, what it reads and writes in the task, its gate, where the task goes next |
| Stage | `NN - <node>/NN - <stage>/` | **The stage instruction itself** (the seven parts below), plus a table of any other files in the folder |
| Sub-stage | a folder inside a stage (e.g. one per channel) | The same as a stage |

Other files in a stage folder are only templates, prompts or reference tables that its ENTRY uses. An agent reads the ENTRY of the folder it is in, and nothing else, until that ENTRY sends it somewhere.

## A stage ENTRY has exactly these parts, in this order

| # | Part | What it must contain |
|---|---|---|
| 1 | Title + purpose | `# NN · Verb`, then one line: what this stage produces, and what the next stage needs from it |
| 2 | Contract | **Reads:** exact task paths. **Writes:** exact task paths. **Done when:** a condition you can check by looking at the output |
| 3 | Procedure | Numbered imperative actions. Every judgment call comes with a **decision rule** whose condition is visible in the input. Never an adjective ("if appropriate") |
| 4 | Output template | The exact skeleton of each file written |
| 5 | Worked example | Input and matching output (an excerpt is enough) |
| 6 | Self-check | Yes/no questions the output must pass. The node's gate reuses them |
| 7 | Traps | The 2–4 ways this stage typically goes wrong, and how each shows up in the output |

## Rules

1. **One job per folder; one home per fact.** Shared vocabulary lives only in `00 - control/01 - law/`: slots in `BRIEF_SLOTS.md`; task layout, IDs, tags and states in `TASK_CONTRACT.md`.
2. **Every choice comes with its rule.** When a rule can't decide, the value is UNDECIDED and gets a deciding question: one question whose every answer maps to exactly one value.
3. **Every open item has a route:** client, research, or a stated assumption. Nothing is left "to consider".
4. **No invented facts.** Worked examples after intake use the gemstone sample task. Any value in an example that isn't in a real task file is marked *(illustrative)*, and must never be copied into a task.
5. **Cut every sentence that doesn't change what the reader does.** Plain words, imperative voice, no hedging.

## Review checklist

- [ ] The folder has exactly one `00 - ENTRY.md`, and it follows the convention above.
- [ ] All seven parts are present, in order.
- [ ] Every decision has a rule you can check against the input.
- [ ] The worked example obeys the stage's own rules.
- [ ] The self-check could be run by someone who didn't write the stage.
