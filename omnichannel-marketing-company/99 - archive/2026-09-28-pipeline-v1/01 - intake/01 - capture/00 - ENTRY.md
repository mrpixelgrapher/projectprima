# 01 · Capture

**Purpose:** store the request exactly as it arrived, and create the task folder around it. Every later judgment is checked against this file, so it must be the client's words and nothing else.

## Contract

- **Reads:** the request as received (message, email, call notes, attachments).
- **Writes:** the task folder in `01 - intake/work/`, with `TASK.md`, `CONTEXT.md`, `client/` and `01-intake/00-request.md`.
- **Done when:** the text block in `00-request.md` is character-for-character the request as received.

## Procedure

1. **Choose the slug:** 2–5 lowercase words joined by hyphens. Take the business noun from the request, then the ask noun. If the request names no business, use the speaker's role. Never use a person's name.
2. **Choose the client label:** the role or business as the request states it ("gemstone seller"). Use a name only if the client gave one.
3. **Set `--via`:** how the request arrived (`chat`, `email`, `call notes`, `form`). For call notes, the file will show that the text is notes and not a quote.
4. **Set `--kind`:** `real` for a client request; `rehearsal` for a sample used to test the nodes.
5. **Run the operator, pasting the text unchanged.** Keep typos, missing punctuation, slang and line breaks. For long text, save it to a file first and use `--file`.

       python3 "00 - control/02 - tools/task.py" new --slug SLUG --client "LABEL" --via VIA --kind KIND --text "REQUEST"

6. **Save attachments:** put each attachment in `client/`, and replace "None." under **Attachments** in `00-request.md` with one line per file.

## Output template

`00-request.md` is written by the operator: a provenance list (via, from, kind), the request in a `text` block, and an Attachments list. Don't edit the text block.

## Worked example

| Request as received | `--slug` | `--client` |
|---|---|---|
| I'm into precious gemstones selling and want to like build corporate gifts as a sub branch | `gemstones-corporate-gifts` | `gemstone seller` |
| I'm a performace marketer, I want you to do performance marketing for me for xyz | `performance-marketer-xyz` | `performance marketer` |

Both keep their typos ("performace", "like build"). A fast-typed message tells the next step how settled the idea is.

## Self-check

- [ ] Is the text block identical to the request as received?
- [ ] Is the slug built from nouns in the request, with no personal name?
- [ ] Is every attachment in `client/` and listed?

## Traps

- **Cleaning the text.** A corrected or summarised request replaces the client's words with ours, and every later quote becomes a quote of us.
- **Splitting early.** One message that seems to hold two asks is still one request. Splitting is decided at step 3 by a rule, not here.
