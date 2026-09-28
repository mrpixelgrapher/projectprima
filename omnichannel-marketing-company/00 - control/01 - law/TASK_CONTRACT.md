# Task Contract

**Purpose:** what a task folder is, how it is laid out, its IDs, tags and states, and how it floats, branches and joins. The operator `00 - control/02 - tools/task.py` enforces the moving rules.

## 1. A task is one folder

- **Name:** `T-YYYYMMDD-<slug>`, where the slug is 2–5 lowercase words: the business, then the ask. A child task is `T-YYYYMMDD-<slug>.<piece-slug>`.
- **Where it lives:** in exactly one node's `work/` folder while it is being processed, and in `10 - delivery/done/` when it is finished. Its location is its state.
- **Self-contained:** every path inside a task is relative to the task folder. The only paths that point outside are to instruction files, which are relative to the company root (e.g. `02 - discovery/02 - research/00 - ENTRY.md`).

## 2. Layout

    T-YYYYMMDD-<slug>/
    ├── TASK.md          identity, state, history (the operator keeps the field table and History)
    ├── CONTEXT.md       carry-forward: each node appends one section of at most 10 cited bullets
    ├── client/          everything from the client, verbatim: answers, approvals, attachments
    ├── 00-brief.md      child tasks only: the self-contained brief written by 04 - planning
    ├── 01-intake/       one subfolder per node passed, files numbered in the order they were made
    ├── 02-discovery/
    └── …

Every node's last file in the task is `<NN-node>/gate.md`. Every gate writes it in the same five lines, so the operator and the next reader can rely on it:

    VERDICT: PASS | HOLD
    First failed check: — | <check id, e.g. G6>
    Return to: — | <stage, e.g. 04 - questions>
    Waiting on: — | <what is outstanding, e.g. client CQ1–CQ4; research RQ1–RQ3 (after CQ2)>
    Notes for <next node>: none | <anything the carry-forward can't hold>

On `advance`, the operator copies the `Waiting on:` line into the task's `waiting on` field.

## 3. IDs and tags

| ID | Meaning | Made at |
|---|---|---|
| S1… | a statement of the request | 01 - intake, parse |
| I-A… | a reading (interpretation) of an ambiguous statement | 01 - intake, parse |
| F1–F4 | a frame decision | 01 - intake, frame |
| CQ1… | a client question (numbering continues across rounds) | intake, discovery |
| RQ1… | a research question | intake, discovery, research |
| AS1… | a stated assumption | intake, discovery |
| L-001… | a row in a source ledger | discovery, research |
| PR-001… | a proof run (the first delivered unit of an offer) | 10 - delivery |

| Tag (in CONTEXT.md and intermediaries) | Meaning |
|---|---|
| [client] | The client said it: a quote or an answer in `client/` |
| [src: L-nnn] | A logged source supports it |
| [assumed] | Not stated; we proceed on it until the client corrects it |
| [ask: CQn] | Waiting on client question CQn |
| [research: RQn] | Waiting on research question RQn |

CONTEXT.md bullets end with the file they came from, in square brackets, e.g. [01-intake/01-parse.md].

## 4. TASK.md fields and states

Fields: `id`, `kind` (real / rehearsal), `client`, `created`, `arrived via`, `node`, `status`, `waiting on`, `parent`, `children`.

| Status | Meaning | Set by |
|---|---|---|
| IN-NODE | Being worked at its node | operator (`new`, `branch`) |
| ARRIVED | Just floated into a node | operator (`advance`) |
| HOLD | The node's gate did not pass; the reason is in `gate.md` | a gate stage |
| RETURNED | Sent back to an earlier node; the reason is in History | operator (`advance --to`) |
| WAITING-CHILDREN | A parent parked at the join node until its children arrive | operator (`branch --join`) |
| JOINED | A child absorbed into its parent at `09-packaging/pieces/`; its travel is over | operator (`join --absorb`) |
| DONE | Filed in `10 - delivery/done/` | operator (`advance` from 10) |

`waiting on` lists what is outstanding from outside the node (e.g. `client CQ1–CQ4; research RQ1–RQ3 after CQ2`), or `—`. Each gate writes a `Waiting on:` line in its `gate.md`; `advance` copies that line into the field when the task floats, so the two can't disagree. A gate that holds sets `status` to HOLD and `waiting on` by hand.

## 5. Floating

- **Forward:** `task.py advance T-…`. It checks the node's `## Writes` table against the task, and `gate.md` must say `VERDICT: PASS`. Then it moves the folder to the next node's `work/`.
- **Backward:** `task.py advance T-… --to "<node>" --reason "…"`. Always with a reason; it is written to History.
- **Earlier intermediaries** are not edited after the task has left their node. To correct one, send the task back to that node.

## 6. Branching and joining

- **Branch** only at `04 - planning` (one plan → N pieces), or at intake's branch check (two brands, or two offers with different buyers).
- `04 - planning` writes one self-contained brief per piece, at `04-planning/briefs/<piece-slug>.md`.
- `task.py branch T-… --start "05 - research" --join "09 - packaging" --children <slug> …` refuses unless the planning gate has passed and every brief exists. Then it does three things:
  - creates each child in `05 - research/work/`, with the brief as `00-brief.md` and a copy of the parent's CONTEXT.md;
  - records the children in the parent;
  - parks the parent at `09 - packaging` with status WAITING-CHILDREN.
- **Which nodes branch and join** is declared in their ENTRY: `**Branch node:**` (a task leaves only by `branch`, never by `advance`) and `**Join node:**` (a parent may wait there). Today these are `04 - planning` and `09 - packaging`.
- **A child** floats on its own from its start node, and may be sent back only as far as its start node. When it reaches its parent's join node, it stops there (`waiting on: join by parent T-…`) and cannot advance.
- **Join:** `task.py join T-…` reports where each child is (READY or NOT READY). When every child has arrived, `task.py join T-… --absorb` moves each child folder inside the parent, at `09-packaging/pieces/<child-id>/`, marks it JOINED, and sets the parent back to IN-NODE. From then on, the parent holds the whole job.

## 7. Where nodes may write

A node writes only inside the task folder. There is one exception: `10 - delivery` appends one row per task to the company ledgers in `10 - delivery/ledgers/`.

## 8. Kinds

| Kind | Meaning |
|---|---|
| real | A request from an actual client. Its outputs may be delivered |
| rehearsal | A sample run that tests the nodes. It is never sent to anyone |
