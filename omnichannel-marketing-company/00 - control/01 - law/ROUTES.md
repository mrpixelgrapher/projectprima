# Routes

**Purpose:** the ordered list of nodes a task passes through. A task follows exactly one route, named in its `TASK.md` (`route`). The operator `00 - control/02 - tools/task.py` reads the tables below, so this file is the single place a route is defined. Change a route here, and the tool follows.

## How to read a route table

- **Step:** the order. A task never skips ahead: it leaves a step only when that node's gate passes.
- **Node:** the node folder, relative to the company root.
- **Runs when:** `always`, or `includes <item>`. An `includes` step runs only when the task's `includes` field lists that item. The proposal fixes `includes` (`01 - commercial/04 - proposal/`); a step that doesn't run is passed over, and the task's History records it.

A node visited by a task writes into one folder inside the task, named `<department digit><node digit>-<node name>`, e.g. `01 - commercial/01 - intake` → `11-intake/`, `02 - content/05 - writing` → `25-writing/`. The name is the same on every route, so every instruction can name its files exactly.

## Route: engagement

Used for every new request: a one-off job, or the first month of a retainer. It starts at intake and ends when the delivery invoice has gone out.

| Step | Node | Runs when |
|---|---|---|
| 1 | `01 - commercial/01 - intake` | always |
| 2 | `01 - commercial/02 - scope` | always |
| 3 | `01 - commercial/03 - pricing` | always |
| 4 | `01 - commercial/04 - proposal` | always |
| 5 | `01 - commercial/06 - billing-advance` | always |
| 6 | `02 - content/01 - discovery` | always |
| 7 | `02 - content/02 - strategy` | always |
| 8 | `02 - content/03 - performance` | always |
| 9 | `02 - content/04 - planning` | always |
| 10 | `02 - content/05 - writing` | always |
| 11 | `03 - video-factory/01 - script` | includes video |
| 12 | `03 - video-factory/02 - shots` | includes video |
| 13 | `03 - video-factory/03 - stills` | includes video |
| 14 | `03 - video-factory/04 - motion` | includes video |
| 15 | `03 - video-factory/05 - edit-plan` | includes video |
| 16 | `02 - content/06 - packaging` | always |
| 17 | `02 - content/07 - publishing` | includes publishing |
| 18 | `02 - content/08 - delivery` | always |
| 19 | `01 - commercial/07 - billing-delivery` | always |

## Route: month

Used for every retainer month after the first. It starts from the client folder (`clients/<client>/`), refers to last month, and plans the next month. The last node of the previous task opens it (`01 - commercial/07 - billing-delivery/`).

| Step | Node | Runs when |
|---|---|---|
| 1 | `01 - commercial/05 - month-review` | always |
| 2 | `01 - commercial/06 - billing-advance` | always |
| 3 | `02 - content/03 - performance` | always |
| 4 | `02 - content/04 - planning` | always |
| 5 | `02 - content/05 - writing` | always |
| 6 | `03 - video-factory/01 - script` | includes video |
| 7 | `03 - video-factory/02 - shots` | includes video |
| 8 | `03 - video-factory/03 - stills` | includes video |
| 9 | `03 - video-factory/04 - motion` | includes video |
| 10 | `03 - video-factory/05 - edit-plan` | includes video |
| 11 | `02 - content/06 - packaging` | always |
| 12 | `02 - content/07 - publishing` | includes publishing |
| 13 | `02 - content/08 - delivery` | always |
| 14 | `01 - commercial/07 - billing-delivery` | always |

## Includes

| Item | Means | Set by |
|---|---|---|
| `video` | The accepted proposal (or an accepted upsell) has video deliverables: the task passes through the video factory | the `Includes:` line of the `01 - commercial/04 - proposal/` or `01 - commercial/05 - month-review/` gate |
| `publishing` | We publish on the client's accounts: the task passes through publishing | the same |
