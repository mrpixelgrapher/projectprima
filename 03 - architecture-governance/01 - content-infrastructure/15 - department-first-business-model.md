# 15 — Department-First Business Model

Type: business model document (Gap 05)

## The Gap

Business infrastructure is documented as knowledge in the founder's head. It needs to become executable organizational memory — capability engines that accept an objective and produce a predictable outcome.

## Conversion Process

### From Document to Engine

Each department must transition through four states:

| State | Description | Example |
|---|---|---|
| 1. Documented | Knowledge exists in files, notes, conversations | "We do research before writing" |
| 2. Mapped | Workflows, decision points, inputs, outputs, standards documented | Process map with entry/exit criteria |
| 3. Formalized | Playbooks, frameworks, decision trees, templates created | Writing Department Operational Spec (08) |
| 4. Engineered | Accepts objective → produces predictable outcome | Function folder with verification checks |

### Current State per Department

| Department | State | Next Action |
|---|---|---|
| Media | 3-4 | Formalize remaining workflows as function folders |
| Writing | 2-3 | Complete operational spec, create function folder |
| Law | 3 | Create document templates and compliance frameworks |
| Design | 1-2 | Begin workflow mapping |
| Branding | 1 | Begin knowledge documentation |
| Operations | 1 | Begin cross-department coordination mapping |

### prompt router Structure

Each department as engine has:

```
department-[name]/
├── 00 - ENTRY.md           ← Navigation and reading order
├── WORKING_RULES.md        ← Governing rules for every execution
├── OUTPUT_CONTRACT.md      ← Required output structure
├── ORGAN_WIRING_MAP.md     ← Load order for prompt-bank organs
├── QUALITY_GATES.md        ← Must-pass conditions
├── templates/              ← Reusable output templates
├── playbooks/              ← Step-by-step procedures
└── decision-trees/         ← Branching logic for common decisions
```

### Dependency Resolution

When a department needs output from another:
1. Check the dependency chain (Spec 07)
2. Request the specific output artifact by name
3. Verify the output meets the producing department's quality standards
4. Use the output as input for the current department's workflow

### CE Implementation

Each department maps to a CE function folder under `.\..\..\..\..\..\03 - work-projects\02 - company\02 - working-companies\`. The function folder contains the engine structure above. CE's cognitive sequence dispatches department-specific tasks through the appropriate function folder.
