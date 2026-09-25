# Department-First Business Model

Type: business model document — declares that organizational capability is built as a collection of discrete departments in strict sequence, with the infrastructure layer largely complete and the operational-execution layer currently underway. Departments are modeled as prompt routers, not document collections.

## Authority

This file bridges three existing architecture documents:

- `.\COMPANY_DEPENDENCY_GRAPH.md` — cross-entity dependency view (4 companies, 7 departments, shared CE systems)
- `.\DEPARTMENT_REGISTRY.md` — department inventory (status, function folder, core output, depends-on)
- `.\MULTI_VERTICAL_CONTENT_OS.md` — cross-vertical view (5 verticals on shared infrastructure)

When this file conflicts with any of those, the more specific workspace area wins. This file adds the **operational memory** dimension that the other three do not.

## Source intent

Derived from `.\..\..\..\..\99 - ARCHIVE\tech-bro\2026-06-13-lrp6-infrastructure-buildout\gaps\05 - codify-department-first-infrastructure.md`. The source declares: the business infrastructure must be modeled as a collection of discrete departments rather than a single monolithic system. Organizational capability emerges from layered dependencies, not from parallel construction of unrelated functions.

## Core principle

Departments are discrete operational units. Media, Writing, Law, Design, Branding, Operations, Research — each has its own:
- Workflows
- Standards
- Processes
- Outputs
- Success criteria

**Rule:** departments are built in strict sequence, not simultaneously. The output of one department creates the foundation required for the next. This is a factory pipeline.

## Current state of departments (as of 2026-06-14)

| Department | Status (per DEPARTMENT_REGISTRY) | Role in the model |
|---|---|---|
| Media | COMPLETE | Foundational — provides visual asset infrastructure, production workflows, prompt-bank patterns |
| Writing | ACTIVE | Second — builds on Media's visual capabilities, produces research-first articles |
| Law | OPERATIONAL | Third — legal frameworks for content, IP, contracts, compliance (formalization pending) |
| Design | PLANNED | Fourth — brand identity systems require established content and legal frameworks |
| Branding | PLANNED | Fifth — strategic positioning depends on content + legal + design |
| Operations | PLANNED | Sixth — cross-department coordination only makes sense when multiple departments exist |
| Research | (implicit) | Cross-cutting — KSE Gate 8 is the CE realization of research-first discipline |

## Two-phase development model

### Phase 1: Infrastructure creation (largely complete)

> The infrastructure itself represents more than two years of continuous development, research, and refinement. Each department was reverse-engineered through direct study of real-world organizations — office visits, practitioner discussions, books, academic research, internet-based investigation, AI-assisted analysis, extensive foundational inquiry. The objective was not merely to replicate visible outputs but to understand how professional organizations actually function beneath the workspace area. The infrastructure now contains a substantial portion of the organizational intelligence normally distributed across a fully staffed company.

**CE realization:** this infrastructure is the WORKSPACE_ORCHESTRATION_CONTRACT + WORK_AXIOM_BANK + RESEARCH_FIRST_CONTENT_PRODUCTION governance + the Media and Writing department function folders + the content-distribution company + the lrp6 content-infrastructure specs. These are the assets that would normally live across a fully staffed company's institutional memory.

### Phase 2: Operational execution (currently underway)

> Execution remains an ongoing phase, but the strategic foundation — what to build, who to target, where to operate, how to operate, what to create, and how departments interact — has already been established. CE should preserve and reinforce this distinction between infrastructure creation and operational execution, treating the former as a largely completed asset and the latter as the process of activating and scaling the capabilities that have already been designed.

**CE realization:** the current LRP6 execution (this 16-step run) is the transition between Phase 1 and Phase 2 — taking documented infrastructure and converting it into executable organizational memory.

## Departments as prompt routers (not document collections)

The next stage converts documented knowledge into executable organizational memory.

**Old frame:** a department is a collection of documents (WORKFLOW.md, OUTPUT_CONTRACT.md, templates).

**New frame:** a department is a prompt router that accepts an objective and produces a predictable outcome.

| Aspect | Document-collection frame | Capability-engine frame |
|---|---|---|
| Inputs | List of templates | Explicit input contract (what must be provided to invoke the department) |
| Outputs | Example artifacts | Explicit output contract (what the department guarantees to produce) |
| Workflows | Procedural steps | Decision tree with deterministic branches |
| Standards | Implicit in prose | Explicit pass/fail verification gates |
| Dependencies | Mentioned in ancestry | Explicit input contracts from upstream departments |
| Success criteria | Implied | Explicit completion checklist |

## What "executable organizational memory" requires

For every department, extract from existing materials and formalize into:

1. **Process map** — the full decision tree from objective to outcome, including branches and failure modes.
2. **Playbook** — the step-by-step execution procedure a cold CE instance can follow without reconstruction.
3. **Framework** — the reusable patterns (templates, prompt-bank organs, axioms) that the department contributes to the infrastructure.
4. **Decision tree** — the explicit pass/fail criteria at every branch point.
5. **Linkage to other departments** — the explicit input contracts (what upstream departments must provide) and output contracts (what downstream departments receive).

**CE realization:** much of this is already in place:
- Process maps = each department's WORKFLOW.md
- Playbooks = each department's OUTPUT_CONTRACT.md + verification gates
- Frameworks = prompt-bank organs + WORK_AXIOM_BANK axioms + templates
- Decision trees = verification gates with explicit pass/fail criteria
- Linkage = each department's ENTRY.md ancestry + MEDIA_DEPARTMENT_DEPENDENCY.md + DEPARTMENT_REGISTRY's "depends on" column

**The gap (now CLOSED):** the existing workspace areas describe what the department is. The invocation workspace area — a deterministic dispatcher that, given an objective, identifies which department owns it, what prerequisites are required, what standards must be met, and what sequence of actions executes — is realized at:

`.\..\..\03 - company-creation-protocol\03 - function-folder\04 - runtime\00 - QUERY\DEPARTMENT_ROUTER.py`

## The invocation workspace area (realized 2026-06-14)

When a task arrives, the system can now determine:
- Which department is responsible for the task.
- What prerequisite outputs are required from other departments.
- What standards must be met.
- What sequence of actions should be executed.

**Tool:** `DEPARTMENT_ROUTER.py` (lives in the same `00 - QUERY` folder as `WORK_ROUTER.py` and `working_rules.py` — the runtime query workspace area for deterministic dispatchers).

**Invocation forms:**

```
python DEPARTMENT_ROUTER.py --objective "<objective text>"    # classify to department + prereqs + sequence
python DEPARTMENT_ROUTER.py --list                            # show all departments from the registry
python DEPARTMENT_ROUTER.py --info "<Department Name>"        # show one department's full record
```

**Exit-code contract:**

| Code | Meaning |
|---|---|
| 0 | Objective matched a department; prerequisites all OPERATIONAL or better; department executable |
| 2 | Objective matched a department; at least one prerequisite is PLANNED (cannot execute yet) OR target itself is PLANNED |
| 3 | NO_DEPARTMENT_MATCH — objective did not match any department's keyword signals |
| 4 | Registry parse error or missing registry file |

**How it works:**
- Parses `.\DEPARTMENT_REGISTRY.md`'s `## Registry` table into structured records (rank, name, status, function folder, core output, depends-on).
- Resolves each department's function folder on disk (registry paths elide the `03 - work-projects/02 - company/` segment; the tool recovers by taking the last path segment and joining to the working-companies root).
- Workspace areas WORKING_RULES.md, OUTPUT_CONTRACT.md, and 00 - ENTRY.md paths when those files exist in the department's function folder.
- Classifies objectives against a per-department keyword-signal map (matches the pattern used by `WORK_ROUTER.py`'s TYPE_A / TYPE_B taxonomy and `domain-organ-map.md`). Ties are broken by registry rank (upstream preferred).
- Walks the `Depends On` graph depth-first to emit the prerequisite sequence (upstream first, target last).

**Verification evidence (2026-06-14):**
- `--objective "publish a research article on Substack"` → Writing (Media prereq OK), standards on disk, exit 0.
- `--objective "produce a LinkedIn thought-leadership post"` → Content Distribution (Media + Writing prereqs OK), standards on disk, exit 0.
- `--objective "create visual assets for a newsletter"` → Media (no prereqs), standards on disk, exit 0.
- `--objective "build a brand identity system"` → Design (PLANNED), prereqs OK but target blocked, exit 2.
- `--objective "fix the CI pipeline"` → NO_DEPARTMENT_MATCH, exit 3.
- `--info "Media"` → full record rendered with keyword signals, exit 0.
- `--list` → registry table rendered (7 rows), exit 0.

**Relationship to WORK_ROUTER.py:** DEPARTMENT_ROUTER sits above WORK_ROUTER. A task arrives → DEPARTMENT_ROUTER identifies the responsible department and the prerequisite chain → within that department's function folder, WORK_ROUTER identifies the specific execution path (Location | Protocol | First step). Both tools are invoked by cold CE instances to inherit without reconstruction.

## Integration with existing CE systems

| Existing system | How department-first model uses it |
|---|---|
| COMPANY_DEPENDENCY_GRAPH.md | The cross-entity dependency view this model operates within |
| DEPARTMENT_REGISTRY.md | The department inventory this model treats as prompt routers |
| MULTI_VERTICAL_CONTENT_OS.md | The cross-vertical view this model serves |
| WORKSPACE_ORCHESTRATION_CONTRACT | The workspace-level contract every department obeys |
| WORK_AXIOM_BANK | The accumulated axioms extracted from department operations |
| WORK_ROUTER.py | The task-level router (department router would sit above this) |
| KSE Gate 8 | The research-depth gate every department passes through |
| RESEARCH_FIRST_CONTENT_PRODUCTION | The research-first discipline every department obeys |

## Verification

The department-first model is fully operationalized when every department satisfies:

| # | Check | How | Fail Action |
|---|---|---|---|
| 1 | Department in DEPARTMENT_REGISTRY | Registry has row for the department | Add row |
| 2 | Function folder exists | Department's function folder path resolves on disk | Create folder with ENTRY.md |
| 3 | Capability-engine frame adopted | Department's ENTRY.md declares input contract + output contract + verification gates (not just workflow steps) | Rewrite ENTRY.md in capability-engine frame |
| 4 | Process map on disk | Department's WORKFLOW.md has explicit decision branches | Add decision branches |
| 5 | Playbook on disk | Department's OUTPUT_CONTRACT.md has explicit pass/fail criteria | Add criteria |
| 6 | Framework contributed | Department has contributed at least one prompt-bank organ or WORK_AXIOM_BANK axiom | Contribute framework |
| 7 | Linkage explicit | Department's ENTRY.md names upstream input contracts and downstream output contracts | Declare linkage |
| 8 | Department router can identify responsibility | `python DEPARTMENT_ROUTER.py --objective "<objective>"` returns this department with correct prerequisites and standards | Add this department's keyword signals to `OBJECTIVE_KEYWORDS` in `DEPARTMENT_ROUTER.py`; add a registry row if missing |

## Read order (cold instance arriving at this file)

1. This file — see the department-first principle and the capability-engine frame.
2. `.\DEPARTMENT_REGISTRY.md` — the department inventory.
3. `.\..\..\03 - company-creation-protocol\03 - function-folder\04 - runtime\00 - QUERY\DEPARTMENT_ROUTER.py` — the invocation workspace area (objective → department + prerequisites + standards + sequence).
4. `.\COMPANY_DEPENDENCY_GRAPH.md` — the cross-entity dependency view.
5. `.\MULTI_VERTICAL_CONTENT_OS.md` — the cross-vertical view.
6. The specific department's ENTRY.md + WORKFLOW.md + OUTPUT_CONTRACT.md — see the capability-engine frame applied.

## Update rule

When a department transitions from PLANNED → OPERATIONAL → ACTIVE → COMPLETE:
1. Update `DEPARTMENT_REGISTRY.md` first.
2. Update `COMPANY_DEPENDENCY_GRAPH.md` if the department adds a new company edge.
3. Update this file's "Current state of departments" table.
4. Update the department's own ENTRY.md to adopt the capability-engine frame.

When the department router is built:
1. Create `.\..\..\03 - company-creation-protocol\03 - function-folder\04 - runtime\00 - QUERY\DEPARTMENT_ROUTER.py`.
2. Update this file to remove the "missing piece" section.
3. Update `WORKSPACE_ORCHESTRATION_CONTRACT` if the router changes the workspace-level contract.
