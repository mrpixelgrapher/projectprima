# 99 - archive

**Purpose:** past material, kept whole and read-only. Nothing here is instruction any more: the live instructions are in `01 - commercial/`, `02 - content/`, `03 - video-factory/` and `00 - control/`. Read an archived file only to see where an idea came from; each live node ENTRY lists what it absorbed in its "Past material merged here" table. Paths inside archived files point at the tree as it was, and `check_links.py` does not check them.

## The two snapshots

| Folder | What it is | Replaced by | Why |
|---|---|---|---|
| `2026-09-28-restructure/` | The company as sessions S001–S002 left it: the scaffold (`00-control`, `01-foundation` … `05-convergence`), the departments (`01 - writing-department`, `02 - content-distribution`, `03 - architecture-governance`, `04 - media-department`) and the old company ENTRY | The node structure of S003, and then v2 | The operator's reframe (I-008) and "merge these into the flow… no stubs" (I-010, I-011) |
| `2026-09-28-pipeline-v1/` | Pipeline v1 from S003: ten nodes (`01 - intake` … `10 - delivery`), their law files and the v1 company ENTRY, byte-identical to commit `4c2487f` | The v2 tree of three departments | The design lock (I-012): `00 - control/04 - source-intent/06 - operator-directives-2026-09-28-design-lock.md` |

## Where the S001–S002 folders went (`2026-09-28-restructure/`)

| Archived folder | Its content now lives in |
|---|---|
| `00-control/` (status, execute, asset-intake, work-choices, carbon-input forms, the assembly line, `line_status.py`) | The CARBON form format → `01 - commercial/01 - intake/04 - questions/`; the tools → `00 - control/02 - tools/`; state and source intent → `00 - control/03 - state/`, `04 - source-intent/`. The assembly line and `line_status.py` were superseded by routes and `task.py` |
| `01-foundation/` (customer, problem, value proposition, author voice, offer) | Per-client now: `clients/<client>/` (brief, voice); the offer and pricing → `01 - commercial/` |
| `02-sourcing/` (research plan, source ledger, dossier D-001, question bank, input registry) | The ARENA request and query bank → `02 - content/01 - discovery/01 - requests/`; the source-ledger format → `02 - content/01 - discovery/02 - findings/`; the input registry → `00 - control/05 - registers/` |
| `03-setup/`, `04-interface/`, `05-convergence/` | The positioning core → `02 - content/02 - strategy/01 - positioning/`; the measurable objective → `02 - content/02 - strategy/05 - objectives/` |
| `01 - writing-department/` (prompt library, output contract, working rules) | The five prompts, verbatim → `02 - content/05 - writing/` (research, draft, voice, review); the seeds → `02 - content/05 - writing/05 - seeds/` |
| `02 - content-distribution/` (hub-and-spoke architecture, channel layers, templates, activation) | Channel roles → `02 - content/02 - strategy/04 - channels/channel-roles.md`; channel craft and templates → `02 - content/05 - writing/06 - channels/`; kit and partial publication → `02 - content/06 - packaging/01 - kit/` |
| `03 - architecture-governance/` (doctrines, specs, gap register, external register) | The doctrines → `00 - control/01 - law/`; the external register → `00 - control/05 - registers/`; the specs' rules → the nodes that cite them |
| `04 - media-department/` (visual brief contract) | `02 - content/05 - writing/08 - visuals/` (now scene prompts for the image factory) |

## Where the pipeline v1 nodes went (`2026-09-28-pipeline-v1/`)

| v1 node | v2 location |
|---|---|
| `01 - intake` | `01 - commercial/01 - intake/` (now waits for the client's answers) |
| `02 - discovery` | `02 - content/01 - discovery/` (research through ARENA; the answers stage moved to intake) |
| `03 - strategy` | `02 - content/02 - strategy/` (plus the destination stage) |
| `04 - planning` | `02 - content/04 - planning/` (a month plan and calendar; no branching) |
| `05 - research`, `06 - drafting`, `07 - review`, `08 - shaping` | `02 - content/05 - writing/`, one node (the writing department) |
| `09 - packaging` | `02 - content/06 - packaging/` (no join; the kit is one folder per channel) |
| `10 - delivery` | `02 - content/08 - delivery/` (the proof-run rule was withdrawn; ledgers split with `01 - commercial/ledgers/`) |
| Not in v1 | `01 - commercial/02`–`07`, `02 - content/03 - performance/`, `02 - content/07 - publishing/`, `03 - video-factory/`, `clients/` |
