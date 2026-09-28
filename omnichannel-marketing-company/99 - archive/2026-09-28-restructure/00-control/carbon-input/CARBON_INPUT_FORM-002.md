# CARBON_INPUT_FORM-002 — for the friend: who you are, who first, where

Staged: 2026-09-28 (session S002). Status: **OPEN — awaiting answers**.
For: the friend, the author whose voice this whole line produces (input I-001).
Time to complete: 20–30 minutes, most of it choosing writing samples.

**Why only you can answer.** The line is stuck at its first station (`python3 00-control/tools/line_status.py`). Nothing downstream may write a sentence until it knows whose voice it writes in and who it's writing for. Guessing either would put a false name into every file that reads them.

**How to answer.** Fill the blanks below, or write straight into `01-foundation/author-voice.md` and `01-foundation/customer.md` (their `## Fill-in` sections). Leave a blank rather than guess.

---

## Q1. Who are you, as the author?

- Name, as it should appear when publishing: ______________________
- Your field or specialty, in one line (within marketing for founder-led and small businesses, or tell us if it's different): ______________________
- What your expertise rests on, as facts (years, roles, notable work, results you can stand behind): ______________________

**Unblocks:** station S1a; the `{{DOMAIN}}` slot of the research stage; the "Publishes as" column in `02 - content-distribution/CHANNEL_ACTIVATION.md`.

## Q2. How do you write?

Paste or link 3–5 pieces of **your own** writing. Stage 04 extracts your voiceprint from them, so every piece is re-voiced toward you and not toward "human in general" (`01 - writing-department/01 - prompt-library/04 - PROMPT_voice_humanization.md`).

- [ ] **A. Recommended: things you wrote yourself, unedited by AI**, such as long emails to clients, posts, proposals or notes. *Why:* the voiceprint copies whatever it is given. AI-edited text would teach it the flat rhythm it exists to remove.
- [ ] **B.** Published pieces that an editor polished.
- [ ] **C.** Transcripts of you talking (calls, voice notes). Useful if you write little, since spoken rhythm still carries your voice.

Samples (paste below, or add files to `01 - writing-department/voiceprints/samples/`):
1. ______________________
2. ______________________
3. ______________________

**Unblocks:** station S1a (way of talking) and Stage 04 Part A.

## Q3. Who is the one real buyer first?

The buyer *type* is already fixed by what's built: a founder or small-business owner making a professional marketing decision (I-002). We need **one real** person or company of that type. They are the recipient of the free proof-run audit PR-001 (`01-foundation/offer.md`).

- [ ] **A. Recommended: someone in your network already running marketing on 2 or more channels.** *Why:* the audit maps the channels they already run against one hub-and-spoke system (`01-foundation/value-proposition.md`). With only one channel, there is little to map.
- [ ] **B.** Your own business, or one you are part of.
- [ ] **C.** Someone just starting out, with no channels yet.

- Name, or an anonymised label if they'd prefer: ______________________
- Industry: ______________________
- Size (staff, or rough revenue band): ______________________
- What they've already tried for marketing, and why it didn't hold: ______________________
- Have they agreed to receive a free audit? yes / not yet: ______________________

**Unblocks:** station S1b, the buyer lane of research D-001, and the proof run PR-001.

## Q4. Where do the hub and the first spoke live?

The order is already decided by the wiring: the Substack hub plus LinkedIn go first (`02 - content-distribution/CHANNEL_ACTIVATION.md`). Only the accounts are missing.

| Channel | Existing URL or handle | Or create new? |
|---|---|---|
| Substack (hub) | | yes / no |
| LinkedIn (spoke 1) | | yes / no |

- [ ] **A. Recommended: both under your own name.** *Why:* the author and the publishing identity are the same person (I-001).
- [ ] **B.** Both under a company name.
- [ ] Other: ______________________

**Unblocks:** station S7 (posting) and the Substack URL every variant links back to. Not needed to start writing.

---

## Deliberately not asked yet

- **Prices.** Set after the free proof run records what it cost (`01-foundation/offer.md`, input I-003).
- **What may be published as proof.** Asked once the proof run exists, because there is nothing to grant permission for yet.

## When answered

The next session logs each answer in `02-sourcing/input_registry.md` as `I-nnn`, replaces the matching `[CARBON-BLOCKED: F-002 Qn]` markers with `[src: I-nnn]`, runs Stage 04 Part A on the samples, and re-runs `line_status.py`.
