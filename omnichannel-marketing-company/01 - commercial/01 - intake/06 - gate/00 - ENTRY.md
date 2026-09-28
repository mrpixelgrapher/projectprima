# 06 · Gate

**Purpose:** decide whether intake's work is complete. If it is, compress what intake learned into the carry-forward, publish the client profile, and move the task to scope.

## Contract

- **Reads:** every file in `11-intake/` and `from-client/`.
- **Writes:** the `## 11-intake` section of `CONTEXT.md`; `11-intake/gate.md`; `clients/<client>/profile.md`.
- **Done when:** `gate.md` says `VERDICT: PASS`, the profile is published, and `task.py advance` has moved the task.

## Procedure

1. **Run the checks in order.** Stop at the first failure, write `VERDICT: HOLD` in `gate.md` with the check and the stage to return to, and go back there.

   | # | Check (each one visible in the files) | On failure, go back to |
   |---|---|---|
   | G1 | The text block in `00-request.md` is the request as received | 01 - capture |
   | G2 | Every quote in `01-parse.md` appears word for word in `00-request.md` | 02 - parse |
   | G3 | `01-parse.md` states no fact the request doesn't contain | 02 - parse |
   | G4 | Each statement with more than one meaning has readings and a deciding question, or the parse says "Single reading" with a reason | 02 - parse |
   | G5 | F1, F2 and F4 have values (F1 may be TO STRATEGY only after a "not sure"); F3 lists IN, ASK and central | 03 - frame, then 05 - answers |
   | G6 | Every open item from the parse and the frame appears in `03-routing.md` exactly once, with one route | 04 - questions |
   | G7 | Every client file sent restates the request, has ≤ 4 questions each with why, options or an example, and needed-by, and lists the assumptions; every reply is mapped in the slot board | 04 - questions, 05 - answers |
   | G8 | Every RQ has capture, sources, needed-by and a condition | 04 - questions |
   | G9 | In `06-slot-board.md`, SPEAKER, BRAND, OFFER (one line), GOAL, CHANNELS, LIMITS (budget, timeline), EXECUTION and LANGUAGE are Known | 05 - answers (next round) |

2. **Write the carry-forward.** Only on a pass. Append this section to `CONTEXT.md`, at most 10 bullets, each ending with its source file in square brackets:

       ## 11-intake
       - Ask: "<literal ask>" [client] [11-intake/01-parse.md]
       - Frame: F1 …, F2 …, F3 IN … / central …, F4 … [11-intake/06-slot-board.md]
       - Package shape: <cell> [11-intake/06-slot-board.md]
       - Goal: "<client's words>" [client] [11-intake/06-slot-board.md]
       - Channels today · language: … [client] [11-intake/06-slot-board.md]
       - Budget · timeline: … [client] [11-intake/06-slot-board.md]
       - Open for discovery: <slots and CQs> [11-intake/03-routing.md]
       - Research queued for ARENA: RQ1–RQn, <conditions in short> [11-intake/05-research-questions.md]
       - Assumed: AS1 <short> [assumed] [11-intake/03-routing.md]

3. **Write `gate.md`** (the five-line format in `00 - control/01 - law/TASK_CONTRACT.md` §2), with `Waiting on: —` on a pass.

4. **Publish the client profile.** Fill `clients/<client>/profile.md` from the slot board: each row's value and its source tag. If the file already has values (a returning client), first move it to `clients/<client>/versions/profile-<YYYY-MM-DD>.md`.

5. **Advance:** `python3 "00 - control/02 - tools/task.py" advance <task-id>`.

## Self-check

- [ ] Were the checks run in order, stopping at the first failure?
- [ ] Is the carry-forward at most 10 bullets, each with a source?
- [ ] Does the profile match the slot board, row for row?

## Traps

- **Passing on effort.** A careful parse that still quotes words the client didn't write fails G2. Judge the checks, not the effort.
- **A carry-forward that retells the files.** CONTEXT.md holds decisions and open items, not narrative.
- **Passing with an intake slot "almost known".** G9 is binary. "Budget: flexible" is not a budget; ask again.
