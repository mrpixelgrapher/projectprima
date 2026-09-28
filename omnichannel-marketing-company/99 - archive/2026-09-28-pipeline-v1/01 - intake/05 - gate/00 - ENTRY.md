# 05 · Gate

**Purpose:** decide whether intake's work is fit to float. If it is, compress what intake learned into the task's carry-forward, and move the task to `02 - discovery`.

## Contract

- **Reads:** every file in `01-intake/`.
- **Writes:** the `## 01 - intake` section of `CONTEXT.md` and `01-intake/gate.md` (whose `Waiting on:` line becomes the task's `waiting on` field when it floats).
- **Done when:** `gate.md` says `VERDICT: PASS` and `python3 "00 - control/02 - tools/task.py" advance <task-id>` has moved the task.

## Procedure

1. **Run the checks in order.** Stop at the first failure, write `VERDICT: HOLD` in `gate.md`, and return to the named step.

   | # | Check (each one visible in the files) | On failure, go back to |
   |---|---|---|
   | G1 | The text block in `00-request.md` is the request as received | step 1 |
   | G2 | Every quote in `01-parse.md` appears word for word in `00-request.md` | step 2 |
   | G3 | `01-parse.md` states no fact the request doesn't contain | step 2 |
   | G4 | Each statement with more than one meaning has readings and a deciding question, or the parse says "Single reading" with a reason | step 2 |
   | G5 | F1–F4 each have evidence, or are UNDECIDED with a deciding question; the package is the lookup cell or "pending" | step 3 |
   | G6 | Every open item from the parse and the frame appears in `03-routing.md` exactly once, with one route | step 4 |
   | G7 | The client file restates the request, has ≤ 4 questions each with why, options or example, and needed-by, and lists the assumptions | step 4 |
   | G8 | Every RQ has capture, sources, needed-by and a condition | step 4 |

2. **Write the carry-forward.** Only on a pass. Append this section to `CONTEXT.md`, at most 10 bullets, each ending with its source file in square brackets:

       ## 01 - intake
       - Ask: "<literal ask>" [client] [01-intake/01-parse.md]
       - Frame: F1 …, F2 …, F3 …, F4 … [01-intake/02-frame.md]
       - Package: <cell or pending on …> [01-intake/02-frame.md]
       - Open readings: <I-A vs I-B, decided by CQn — or none> [01-intake/01-parse.md]
       - Slots known: <slot names and one-word values — or none> [client] [01-intake/01-parse.md]
       - Round 1 out: CQ1 <topic> · CQ2 … [ask: CQ1–CQn] [01-intake/04-client-questions.md]
       - Research queued: RQ1–RQn, <conditions in short> [01-intake/05-research-questions.md]
       - Assumed: AS1 <short> [assumed] [01-intake/03-routing.md]

3. **Write `gate.md`:**

       VERDICT: PASS
       First failed check: —
       Return to: —
       Waiting on: client CQ1–CQ4; research RQ1–RQ4 (after CQ2)
       Notes for 02 - discovery: <anything that doesn't fit in CONTEXT.md, or "none">

4. **On a HOLD only,** set `status` to `HOLD` and the `waiting on` field in `TASK.md` by hand. On a PASS, step 5 copies "Waiting on" into `TASK.md` for you.

5. **Float:** `python3 "00 - control/02 - tools/task.py" advance <task-id>`. Then send `04-client-questions.md` to the client, unless the task's kind is `rehearsal`.

## Self-check

- [ ] Were the checks run in order, stopping at the first failure?
- [ ] Is the carry-forward at most 10 bullets, each with a source?
- [ ] Do `gate.md` and `TASK.md` name the same waiting items?

## Traps

- **Passing on effort.** A long, careful parse that still quotes words the client didn't write fails G2. Judge the checks, not the effort.
- **A carry-forward that retells the files.** CONTEXT.md holds decisions and open items, not narrative.
- **Blocking on answers.** Intake passes with questions still out; the node that needs an answer holds the task.
