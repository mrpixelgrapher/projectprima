# 01 · Capture

**Purpose:** store the request exactly as it arrived, and create the task folder around it. Every later judgment is checked against this file, so it must be the client's words and nothing else.

## Contract

- **Reads:** the request as received (message, email, call notes, attachments).
- **Writes:** the task folder in this node's `work/` folder, with `TASK.md`, `CONTEXT.md`, `from-client/`, `from-operator/` and `11-intake/00-request.md`; for a new client, the client folder `clients/<client>/` (copied from the template).
- **Done when:** the text block in `00-request.md` is character-for-character the request as received.

## Procedure

1. **Choose the client.** If the sender already has a folder in `clients/` (same person or business), use that folder's name. Otherwise make a new client slug: 1–5 lowercase words, the business noun from the request plus the role (`gemstone-seller`). Never use a person's name.
2. **Choose the task slug and the label.** Task slug: 2–5 lowercase words, the business noun, then the ask noun. Label: the role or business as the request states it ("gemstone seller"); a name only if the client gave one.
3. **Set `--via`:** how the request arrived (`chat`, `email`, `call notes`, `form`). For call notes, the file will show that the text is notes and not a quote.
4. **Set `--kind`:** `real` for a client request; `rehearsal` for a sample used to test the nodes.
5. **Run the operator, pasting the text unchanged.** Keep typos, missing punctuation, slang and line breaks. For long text, save it to a file first and use `--file`.

       python3 "00 - control/02 - tools/task.py" new --route engagement --client CLIENT --slug SLUG --label "LABEL" --via VIA --kind KIND --text "REQUEST"

6. **Save attachments:** put each attachment in `from-client/`, and replace "None." under **Attachments** in `00-request.md` with one line per file.

## Output template

`00-request.md` is written by the operator: a provenance list (via, from, kind), the request in a `text` block, and an Attachments list. Don't edit the text block.

## Worked example

| Request as received | `--client` | `--slug` | `--label` |
|---|---|---|---|
| I'm into precious gemstones selling and want to like build corporate gifts as a sub branch | `gemstone-seller` | `gemstones-corporate-gifts` | `gemstone seller` |
| I'm a performace marketer, I want you to do performance marketing for me for xyz | `performance-marketer` | `performance-marketer-xyz` | `performance marketer` |

Both keep their typos ("performace", "like build"). A fast-typed message tells the next step how settled the idea is.

## Self-check

- [ ] Is the text block identical to the request as received?
- [ ] Is the slug built from nouns in the request, with no personal name?
- [ ] Is every attachment in `from-client/` and listed?
- [ ] Does a returning client reuse their existing folder in `clients/`?

## Traps

- **Cleaning the text.** A corrected or summarised request replaces the client's words with ours, and every later quote becomes a quote of us.
- **Splitting early.** One message that seems to hold two asks is still one request. Splitting is decided at step 3 by a rule, not here.
