# 02 - tools

**Purpose:** the operators. Mechanics are scripts; judgment lives in the stage ENTRY files. Run them from the company root (`omnichannel-marketing-company/`).

| Tool | Does | Exit codes |
|---|---|---|
| `task.py` | Stages a request (`new`); shows the board (`status`); checks a node's gate (`check`); floats a task (`advance`, forward or `--to` backward with a reason); branches children and parks the parent (`branch`); reports the join, then absorbs the children into the parent (`join`, `join --absorb`). Which nodes branch and join is read from their ENTRY (`**Branch node:**`, `**Join node:**`) | 0 ok · 1 refused by a rule · 2 bad usage |
| `check_links.py` | Checks that every backticked path in a live `.md` file resolves, or is registered as external. Skips `99 - archive/` and `00 - control/04 - source-intent/` | 0 pass · 1 broken |
| `derive_phase.py` | Re-derives the company phase from disk (handoff §3); `--write-manifest` records it | 0 ok · 3 manifest overclaims |
