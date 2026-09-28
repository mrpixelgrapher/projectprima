# Omnichannel Distribution — Enforcement Binding

**Source:** `05 - INPUT/01 - intake/01 - gaps/06 - mission-blueprint/05 - OMNICHANNEL_DISTRIBUTION.md`
**Binding date:** 2026-06-14
**Authority:** Carbon doctrine, not CE interpretation
**Status:** ENFORCED — this is not advisory

## The Doctrine

**One source artifact → channel-shaped variants → every channel, every time.**

No public artifact ships to a single channel. Publishing is a matrix operation, not a destination choice.

## Channel Set (initial, extensible)

| Channel | Shape | Role |
|---------|-------|------|
| Website (own domain) | Canonical long-form | Counterparty workspace area — where retainers get signed |
| Substack | Essay/newsletter | Depth + owned audience (email list = membrane asset) |
| Medium | Republished essay | Discovery/SEO workspace area |
| Twitter/X | Thread + atomic insight | Reach, velocity, public thinking-in-progress |
| LinkedIn | Professional authority | Where legal/B2B buyers actually look |

**Extensions:** YouTube (DREAM-24), Instagram (lumina-arts B2C). Add channels as machinery activates.

## Machine-Checkable Rules

### Rule 1: Fan-out terminal (mandatory for all public artifacts)

Every "public artifact" route in the routing table MUST end with a fan-out terminal:

```
source artifact → PUBLISH_KIT/
  ├── website/[slug].md
  ├── substack/[slug].md
  ├── medium/[slug].md
  ├── twitter-x/[slug]-thread.md
  └── linkedin/[slug].md
```

### Rule 2: Independent perfection gate per variant

Each channel variant MUST pass the perfectionism gate independently. A lazy crosspost is a doctrine violation. A thread must read like it was born a thread.

### Rule 3: Publish kit completeness

A publish kit is COMPLETE only when ALL channel variants are:
- Final (not draft)
- Channel-native (not reformatted — reshaped for the channel)
- Paste-ready (Carbon publishes, never adapts)
- Channel-ordered (in the order Carbon will publish)

### Rule 4: Partial publication logging

A public artifact that shipped to fewer than the full channel set WITHOUT a stated reason is an **unenforced-rule violation**. Log it:

```yaml
partial_publication:
  artifact: [name]
  channels_shipped: [list]
  channels_skipped: [list]
  reason: [must be specific — "not relevant to this channel" is acceptable; "didn't get to it" is not]
```

## Verification

To verify this doctrine is enforced:
1. Check every public artifact for a PUBLISH_KIT/ folder
2. Verify all 5 channel variants exist in the kit
3. Run perfection gate on each variant independently
4. Check for partial_publication logs where channels are missing

## Carbon's Send Cost

The machine delivers a **publish kit** — every variant final, channel-ordered, paste-ready. Carbon publishes in one sitting, never adapts. If Carbon has to rewrite a variant for a channel, the machine failed.

## Standing Effects

- Every company OS gains distribution as a Function Node-level concern
- New companies must instantiate WITH the distribution matrix, not bolt it on
- DREAM-09/19/24/27 outputs all flow through this matrix
- The authority engine and the distribution matrix are the same machine seen from two sides
