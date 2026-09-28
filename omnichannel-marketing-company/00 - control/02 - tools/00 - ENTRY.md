# 02 - tools

**Purpose:** the operators. Mechanics are scripts; judgment lives in the stage ENTRY files. Run them from the company root (`omnichannel-marketing-company/`).

| Tool | Does | Exit codes |
|---|---|---|
| `task.py` | Opens a task on a route (`new`); shows the board (`status`); checks a node's gate (`check`); moves a task along its route (`advance`, forward, or `--to` back with a reason, which supersedes the gates it passes back over); holds a task for a hand-off and resumes it (`hold`, `resume`); stops one (`close`). Reads the route from `00 - control/01 - law/ROUTES.md` and each node's `## Writes` table from its ENTRY. Files finished tasks in `clients/<client>/done/` | 0 ok · 1 refused by a rule · 2 bad usage |
| `check_links.py` | Checks that every backticked path in a live `.md` file resolves, or is registered as external. Skips `99 - archive/` and `00 - control/04 - source-intent/` | 0 pass · 1 broken |
| `derive_phase.py` | Re-derives the company phase from disk (handoff §3), mapped onto the commercial and delivery ledgers and the built nodes; `--write-manifest` records it | 0 ok · 3 manifest overclaims |
