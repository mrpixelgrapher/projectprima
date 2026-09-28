# 03 · Spine

**Purpose:** compress the boundary into what the piece will argue: the one thing no single source says, the 3–5 claims that carry it, the tension it resolves, and the particulars behind each claim. The draft expresses these decisions; it does not make them.

## Contract

- **Reads:** `25-writing/<P>/02-boundary-map.md`, `03-observations.md`, `01-sources.md`; the piece brief (`24-planning/briefs/<P>.md`: the question, stage, path job, pillar, limits); `spine-prompt.md` in this folder.
- **Writes:** `25-writing/<P>/04-spine.md`.
- **Done when:** all six parts are filled, the originality check says NONE, and the spine answers the brief's question.

## Procedure

1. **Run the prompt** with the full boundary map as its input.
2. **Aim it at the brief.**
   - THE ONE THING must answer the brief's question.
   - THE READER MOVE starts from what a buyer at the brief's stage believes.
3. **Evidence ledger.** Every spine claim cites the particulars behind it, as O-IDs and L-IDs. `[VERIFY]` items may not be used as evidence.
4. **Limits.** Remove any claim the brief's Limits forbid, e.g. an unverified certification claim.
5. **Pillar conflict.** If the research contradicts the pillar's claim, stop this piece:
   - write a "Pillar conflict" section giving the claim, the contrary evidence and its L-IDs;
   - ask the operator (H2): `25-writing/<P>/04-pillar-conflict-for-operator.md`, and hold the task (`task.py hold … --on "H2 operator: pillar conflict in <P>"`).

   The operator either reframes the piece's question (planning's brief is updated, with the client told if the plan changes) or reopens strategy (`task.py advance <task-id> --to "02 - content/02 - strategy" --reason …`). Writing never edits the strategy.

## Output template

    # Spine — <task id>
    ## 1. The one thing
    ## 2. The spine (numbered claims, in argument order)
    ## 3. The tension
    ## 4. Evidence ledger
    | Claim | Particulars (O-IDs, L-IDs) |
    ## 5. Deliberate omissions (3+, with why)
    ## 6. The reader move
    Originality check: the insight in part 1 appears in source(s): NONE / [list]
    (Pillar conflict: … — only if found)

## Worked example

Gemstone piece P2 `real-or-fake` *(illustrative)*: the one thing is *"The proof that convinces a buyer isn't the lab report itself; it's being shown how to check it in under a minute."* Originality check: NONE. L-004 says reports prove authenticity; L-009 says buyers don't read them; neither says how to make a report usable.

## Self-check

- [ ] Does THE ONE THING answer the brief's question?
- [ ] Does every claim have particulars, with no `[VERIFY]` among them?
- [ ] Does the originality check say NONE?
- [ ] Does the spine respect the brief's Limits?

## Traps

- **A summary pretending to be a spine.** Forty even points and no single argument.
- **An insight found in one source.** If a source says it outright, sharpen it until it's yours, or go back to the boundary.
- **Hiding a pillar conflict.** Bending the evidence to fit the strategy produces an article a buyer won't believe.
