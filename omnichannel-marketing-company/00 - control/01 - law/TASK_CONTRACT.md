# Task Contract

**Purpose:** what a task folder is, how it is laid out, its IDs, tags and states, how it moves, and where each node may write. The operator `00 - control/02 - tools/task.py` enforces the moving rules. Version 2 (S003 design lock); version 1 is in `99 - archive/2026-09-28-pipeline-v1/00 - control/01 - law/TASK_CONTRACT.md`.

## 1. A task is one folder

- **One LLM, one node at a time.** An LLM works a task at one node, using only that node's instructions and the files in the task and the client folder. When the node's gate passes, it moves the task to the next node, where the next LLM picks it up from the files alone. Nothing is carried in memory.
- **Name:** `T-YYYYMMDD-<slug>`. For a new request, the slug is 2–5 lowercase words: the business, then the ask. For a retainer month, the slug is `<client>-<yyyy-mm>` (the month being planned).
- **Where it lives:** in exactly one node's `work/` folder while it is being processed, and in `clients/<client>/done/` when it is finished. Its location is its state.
- **Sequential:** a task does one node at a time, in its route's order (`ROUTES.md`). Nothing is skipped and nothing runs ahead. A node that needs something from outside (the client, the operator, ARENA, the image factory) holds the task until it arrives.
- **Paths:** every path to a task file is relative to the task folder (`11-intake/01-parse.md`). Paths to instruction files are relative to the company root (`02 - content/05 - writing/00 - ENTRY.md`). Paths to client files start with `clients/<client>/`.

## 2. Layout

    T-YYYYMMDD-<slug>/
    ├── TASK.md          identity, state, route, history (the operator keeps the field table, Route and History)
    ├── CONTEXT.md       carry-forward: each node appends one section of at most 10 cited bullets
    ├── from-client/     the client's words, verbatim, as the operator relays them: answers, approvals, receipts, results data
    ├── from-operator/   the operator's inputs: sign-offs, rates, payment confirmations
    ├── 11-intake/       one folder per node visited (ROUTES.md names them), files numbered in the order they were made
    ├── 12-scope/
    └── …

Hand-offs outside the pipeline (to ARENA, the image factory, motion generation) put the request **and what comes back** inside the node's own folder, side by side: `HANDOFFS.md`.

Every node's last file in the task is `<folder>/gate.md`, written in these five lines, so the operator and the next reader can rely on it:

    VERDICT: PASS | HOLD
    First failed check: — | <check id, e.g. G6>
    Return to: — | <stage, e.g. 04 - questions>
    Waiting on: — | <what is outstanding, e.g. client answers to CQ1–CQ4>
    Notes for <next node>: none | <anything the carry-forward can't hold>

On `advance`, the operator copies the `Waiting on:` line into the task's `waiting on` field, and an `Includes:` line (a sixth line only the proposal and month-review gates write) into `includes`.

## 3. IDs and tags

| ID | Meaning | Made at |
|---|---|---|
| S1… | A statement of the request | intake, parse |
| I-A… | A reading (interpretation) of an ambiguous statement | intake, parse |
| F1–F4 | A frame decision | intake, frame |
| CQ1… | A client question (numbering continues across rounds and nodes) | any node that asks the client |
| RQ1… | A research question (goes to ARENA) | intake, discovery, writing |
| AS1… | A stated assumption | intake, discovery |
| D1… | A deliverable (one item the client receives) | scope |
| ST1… | A sub-task (one unit of work, with a kind and an effort) | scope |
| L-001… | A source logged from a dossier | discovery, writing |
| P1… | A piece in the month plan | planning |
| INV-… | An invoice | billing |

| Tag (in CONTEXT.md and intermediaries) | Meaning |
|---|---|
| [client] | The client said it: a quote, or an answer in `from-client/` |
| [operator] | The operator said it: a file in `from-operator/` |
| [src: L-nnn] | A logged source supports it |
| [assumed] | Not stated; we proceed on it until the client corrects it |
| [ask: CQn] | Waiting on client question CQn |
| [research: RQn] | Waiting on research question RQn |

CONTEXT.md bullets end with the file they came from, in square brackets, e.g. [11-intake/01-parse.md].

## 4. TASK.md fields and states

Fields: `id`, `kind` (real / rehearsal), `client` (the client folder's slug), `route`, `includes`, `created`, `arrived via`, `node`, `folder`, `status`, `waiting on`.

| Status | Meaning | Set by |
|---|---|---|
| IN-NODE | Being worked at its node | operator (`new`, `resume`) |
| ARRIVED | Just moved into a node | operator (`advance`) |
| HOLD | Waiting on something from outside the node; `waiting on` says what | operator (`hold`), run by the stage that needs it |
| RETURNED | Sent back to an earlier node on its route; the reason is in History | operator (`advance --to`) |
| DONE | Finished; filed in `clients/<client>/done/` | operator (`advance` from the last step) |
| CLOSED | Stopped before the end (e.g. the proposal was declined); filed in `clients/<client>/done/` | operator (`close`) |

## 5. Moving

- **Forward:** `task.py advance T-…`. It checks the node's `## Writes` table against the task, and `gate.md` must say `VERDICT: PASS`. Then it moves the folder to the next step of the route that runs.
- **Hold and resume:** `task.py hold T-… --on "<what>"` when a stage sends something out and must wait; `task.py resume T-… --note "<what arrived>"` when it lands. The stage then continues where it stopped.
- **Backward:** `task.py advance T-… --to "<department>/<node>" --reason "…"`, to an earlier step of the same route only. The tool marks that node's old `gate.md` and CONTEXT section as superseded (renamed, never deleted), so the node must pass its gate again.
- **Close:** `task.py close T-… --reason "…"` when the engagement stops (declined proposal, client withdraws). The task is filed with status CLOSED.
- **Earlier intermediaries** are not edited after the task has left their node. To correct one, send the task back to that node.

## 6. The client folder

Each client has one permanent folder, `clients/<client>/`, that all of their tasks read and build on: profile, engagement, rates, brief, voice, creator library, strategy, performance design, results and history (`clients/00 - ENTRY.md`). `task.py new` creates it from `clients/00 - template/` the first time.

Only a gate writes to the client folder, and only by copying a file its node produced and the gate passed (or the client approved) into the client file named in that node's ENTRY. Before a file is overwritten, the gate moves the old one to `clients/<client>/versions/<file>-<YYYY-MM-DD>.md`.

**Reading an earlier node's output on a month task.** A month task skips discovery and strategy, so their files are not in it. Wherever an instruction names one of these task files and the task has no such file, read its published copy instead:

| Task file named in an instruction | Read instead (month task) |
|---|---|
| `21-discovery/07-client-brief.md` | `clients/<client>/brief.md` |
| `21-discovery/05-creator-library.md` | `clients/<client>/creators.md` |
| `21-discovery/06-voiceprint.md` | `clients/<client>/voice.md` |
| any `22-strategy/…` file | `clients/<client>/strategy.md` (the section of the same name) |
| `23-performance/06-performance-design.md` from an earlier month | `clients/<client>/performance.md` |

## 7. Where nodes may write

| Where | Who |
|---|---|
| The task folder | every node, only in its own folder, `CONTEXT.md`, and (when a hand-off returns) the place `HANDOFFS.md` names |
| `clients/<client>/` | gates only, as in §6 |
| `01 - commercial/ledgers/` | commercial nodes: one row per event (proposal, invoice, payment, upsell, client) |
| `02 - content/08 - delivery/ledgers/` | delivery: one row per task (delivery, lessons) |

## 8. Kinds

| Kind | Meaning |
|---|---|
| real | A request from an actual client. Its outputs may be sent |
| rehearsal | A sample run that tests the nodes. Nothing is sent to anyone, and its ledger rows are marked `rehearsal` |
