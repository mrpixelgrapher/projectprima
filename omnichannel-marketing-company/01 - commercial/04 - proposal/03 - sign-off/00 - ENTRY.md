# 03 · Sign-off

**Purpose:** get the operator's approval of scope and numbers before anything reaches the client.

## Contract

- **Reads:** `14-proposal/01-package.md`, `02-proposal-for-client.md`; `12-scope/02-breakdown.md` (adjustments noted for the operator); `00 - control/01 - law/HANDOFFS.md` (H2).
- **Writes:** `14-proposal/03-signoff-for-operator.md`.
- **Done when:** `from-operator/14-proposal-signoff.md` says APPROVED, or says what to change and the change has been made and signed off again.

## Procedure

1. **Write the request:** the proposal file to review; the totals; the budget fit; every effort adjustment or deviation from the cadence table; any gap the package stated for the operator. End with: "Reply APPROVED, or list the changes."
2. **Hold:** `python3 "00 - control/02 - tools/task.py" hold <task-id> --on "H2 operator: 14-proposal/03-signoff-for-operator.md"`.
3. **When the answer lands,** resume the task, then:

   | Answer | Action |
   |---|---|
   | APPROVED | Go to `04 - acceptance/` |
   | Changes | Make them at the stage they belong to (package or document), write a v2 document, and ask again |

## Output template

    # Sign-off request — <task id>
    Proposal: 14-proposal/02-proposal-for-client.md
    Totals: setup … · monthly base … · add-ons …
    Budget fit: …
    Deviations for your decision: …
    Reply APPROVED, or list the changes.

## Self-check

- [ ] Is every deviation from the tables listed?
- [ ] Is the approval in `from-operator/`, not assumed?

## Traps

- **Sending while waiting.** The proposal never goes to the client before APPROVED.
