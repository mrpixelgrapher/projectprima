# Perfectionism Doctrine — Enforcement Binding

**Source:** `05 - INPUT/01 - intake/01 - gaps/06 - mission-blueprint/04 - PERFECTIONISM_DOCTRINE.md`
**Binding date:** 2026-06-14
**Authority:** Carbon doctrine, not CE interpretation
**Status:** ENFORCED — this is not advisory

## The Gate

Every artifact a paying stranger touches MUST pass this question before shipping:

> "Does this carry visible evidence of more thought than anyone would reasonably expect?"

**Not** "is it correct." **Not** "is it complete." Those are floors. The gate is the **surplus** — the detail the client didn't ask for that proves someone thought past the brief.

## Machine-Checkable Rules

### Rule 1: crafted_surplus criterion (mandatory for all quality Signal Registries)

Every quality Signal Registry in every company OS MUST include:

```yaml
crafted_surplus:
  required: true
  test: "Name the specific element that exceeds expectation. If you cannot name it, the artifact is not done."
  anti_theater: "Surplus means substantive thought, not decoration. A gradient is not surplus. A clause the counterparty's lawyer will thank us for is."
```

**Affected Signal Registries (known):**
- NB 8-point Signal Registry → add criterion 9: crafted_surplus
- LexBridge quality Function Node → add crafted_surplus check
- Writing department OUTPUT_CONTRACT gates → add gate 7: crafted_surplus
- IMAGE_CREATION quality Signal Registry → add crafted_surplus dimension

### Rule 2: SURPLUS declaration (mandatory for all delivery packets)

Every QA-cleared delivery packet MUST include:

```
SURPLUS: [one-line statement of what the over-craft is]
```

Without this line, the packet is not done. This trains the habit and leaves an auditable trail.

### Rule 3: Template inheritance

All output-generating templates (fee-schedule-generator, engagement-letter-generator, cold-email organs, article templates) MUST include the surplus requirement in their output contracts. The doctrine flows into artifacts by default, not by memory.

### Rule 4: Anti-theater clause

When evaluating surplus, reject:
- Visual decoration without substance (gradients, borders, formatting flourishes)
- Aspirational claims ("we aim to..." "our commitment to...")
- Generic personalization ("Dear [NAME]" alone is not surplus)

Accept:
- A jurisdiction checked that the client didn't ask about
- A contradiction flagged before the client noticed
- A packaging detail that anticipates the unboxing moment
- An email that reads like it was written for exactly one person because it was

## Verification

To verify this doctrine is enforced:
1. Check each company's quality Signal Registry for `crafted_surplus` criterion
2. Check each delivery packet for `SURPLUS:` line
3. Check each output template for surplus requirement
4. Run anti-theater check on any claimed surplus

## Economic Rationale (do not skip — this is load-bearing)

The whole game runs on a two-node graph crossing the membrane with zero existing reputation. Over-craft is the moat a single carbon + silicon stack can actually build, because thought is the one input we have in industrial quantity. Price accordingly: luxury of craft is priced as luxury — never compete on cheap.
