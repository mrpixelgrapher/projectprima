# Email

**Purpose:** one short email that brings one idea from the piece to people the client can reach directly, with one call to action.

## Contract

- **Reads:** `08-shaping/01-seeds.md` (core insight or implication); `00-brief.md` (buyer, CTA, voice); `03-strategy/03-channel-plan.md` (the email's role, via CONTEXT).
- **Writes:** `08-shaping/03-channels/email.md`.
- **Done when:** the subject, preview, body and CTA are written.

## Procedure

1. **Choose the type** from the channel plan's role:
   - **newsletter** (to subscribers): it points to the new piece;
   - **outreach** (to named contacts at target companies): it opens a conversation.
2. **Subject:** short, specific, and no clickbait. **Preview text:** one line that completes the subject.
3. **Body:** 80–200 words, one idea, in the client's voice. Outreach opens with a personalised first line using merge fields `{{first_name}}` and `{{company}}`, which the client fills per recipient. These are fields, not invented facts.
4. **One CTA:** the brief's. Include the hub link.
5. **Image slot:** optional, `email-header`. Omit it for outreach; plain emails read as personal.

## Output template

    <metadata block (add Type: newsletter | outreach)>
    Subject: … · Preview: …
    Body: …
    CTA: …

## Self-check

- [ ] Is it one idea, 80–200 words, with one CTA and the hub link?
- [ ] Does outreach use merge fields and no invented names?

## Traps

- **A newsletter that retells the article.** Give the reader a reason to click, not the whole thing.
