# 01 · Request

**Purpose:** ask ARENA, in one request, for everything the month's pieces need: each piece's topic mapped to its full boundary, and the top-performing posts on each topic right now. A precise request gets a dossier the pieces can be built from; a vague one gets a summary.

## Contract

- **Reads:** `24-planning/01-month-plan.md`; each piece brief in `24-planning/briefs/`; `clients/<client>/done/` (earlier pieces on the same topic); `boundary-prompt.md` in this folder; `00 - control/01 - law/HANDOFFS.md` (H3).
- **Writes:** `25-writing/arena-request-1.md`; `25-writing/00-piece-index.md`; one empty folder per piece, `25-writing/<P>-<slug>/`.
- **Done when:** every piece has its section in the request, the index lists every piece, and the task is on HOLD for the dossier.

## Procedure

1. **Index the pieces.** Write `00-piece-index.md`: one row per piece in the plan (P, slug, type, question, video yes/no), with a "stage reached" column set to "research: requested". Create the piece folders.
2. **Reuse first.** For each piece, look in `clients/<client>/done/*/25-writing/*/02-boundary-map.md` for the same topic or keyword. Where one exists, ask ARENA only to update it: name the earlier map and ask for what changed since its date.
3. **One section per piece.** Fill `boundary-prompt.md`'s slots and paste the filled prompt as that piece's research section:

   | Slot | Value |
   |---|---|
   | `{{TOPIC}}` | The brief's question |
   | `{{ANGLE}}` | The pillar's claim, the objection it answers, and the buyer's stage |
   | `{{DOMAIN}}` | The client's field, plus the buyer (who, where) |

4. **Top-post sampling per topic:** for each channel in the plan, the 5 best-performing posts of the last 90 days on this topic (by any creator), with the same six extraction dimensions as discovery's sampling (hook, structure, angle, funnel mechanics, cadence, visual). Patterns and links only.
5. **Write the request** in the ARENA format (`HANDOFFS.md`), with "Return to: `<task>/25-writing/arena-dossier-1/`", and ask for one dossier section per piece and one per topic's sampling.
6. **Hold:** `task.py hold <task-id> --on "H3 ARENA: 25-writing/arena-request-1.md"`. A rehearsal is not sent.

## Output template

`00-piece-index.md`:

    # Piece index — <task id>
    | P | Slug | Type | Question | Video | Stage reached |

`arena-request-1.md`: the ARENA format in `HANDOFFS.md`, with a `## Piece P<n> — <question>` section (the filled boundary prompt) per piece, and a `## Top posts — <topic>` section per topic.

## Worked example

*(illustrative)* `## Piece P2 — How can a firm tell a real gemstone gift from a fake?` · TOPIC: that question · ANGLE: "Every stone can be verified" (objection: "gemstone gifts might be fake"; stage: considering) · DOMAIN: corporate gifting of precious gemstones, bought by HR leads at 50–300-person IT and consulting firms in <city>.

## Self-check

- [ ] Does every piece have a filled boundary prompt in the request?
- [ ] Is there a top-post sampling section per topic, per channel in the plan?
- [ ] Is the task on HOLD naming the request?

## Traps

- **One question per piece.** The boundary prompt asks for seven sectors; send it whole.
- **Researching here.** The node has no browser; everything outside comes back through ARENA.
