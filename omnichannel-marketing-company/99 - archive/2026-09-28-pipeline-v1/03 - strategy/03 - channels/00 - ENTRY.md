# 03 · Channels

**Purpose:** choose the hub and the spokes for this client, give each one a role, and log every channel left out with its reason. Shaping produces a variant for exactly the channels in this plan.

## Contract

- **Reads:** `02-discovery/05-client-brief.md` (buyer profiles "where they pay attention"; slots CHANNELS and EXECUTION); `01-intake/02-frame.md` (F3 output families); `channel-roles.md` in this folder.
- **Writes:** `03-strategy/03-channel-plan.md`.
- **Done when:** one hub, 1–3 spokes, the extra output families from F3 (IN or approved ASK), and a "left out" row for every other channel in `channel-roles.md`.

## Procedure

1. **Hub.** The hub is the owned, canonical home of every long-form piece. Everything else links back to it, never the reverse.

   | Situation | Hub |
   |---|---|
   | The client has a site they control, with a blog or news section | The site's blog |
   | The client has a newsletter they own | That newsletter |
   | Neither | Recommend Substack (free, owned list, archive). It is an approval item |

2. **Candidate spokes.** A channel is a candidate only if it passes both tests:
   - **(a)** a buyer profile says the buyer pays attention there;
   - **(b)** the client can run it (slot EXECUTION: someone to publish and to reply).

   Take the channels and their roles from `channel-roles.md`.
3. **First spoke.** The candidate with the strongest evidence for the primary buyer (most citations in "where they pay attention"). On a tie, take the channel that week 1 of the 30-day plan pairs with the hub (LinkedIn, for professional buyers).
4. **Cap the first package at the hub plus 3 spokes,** unless the client explicitly asked for more. Every added channel multiplies the work. More channels open after `10 - delivery` records what worked.
5. **Output families.** Add the F3 families that are IN or approved (ad creative and copy, website or landing copy, email, sales collateral). Each is a "channel" row with a role from `channel-roles.md`.
6. **Left out.** Every channel in `channel-roles.md` not chosen gets one line of reason. The omnichannel doctrine requires a stated reason for any channel skipped (`00 - control/01 - law/OMNICHANNEL_ENFORCEMENT.md` Rule 4).
7. **Per channel:** its role, the buyer profile it reaches, the seeds it will use (the seed map in `channel-roles.md`), the focus for this client, its cadence, who publishes it (EXECUTION), and its link-back rule.

## Output template

    # Channel plan — <task id>
    ## Hub
    <channel> — why (rule row) · owner: …
    ## Channels in the plan
    | Channel | Role | Buyer | Seeds | Focus for this client | Cadence | Publishes | Link back |
    ## Left out
    | Channel | Reason |

## Worked example

Gemstone task *(illustrative)*:
- **Hub:** Substack. The client has no blog, so this is an approval item.
- **First spoke:** LinkedIn (HR leads [L-004]).
- **Also:** email, for direct outreach to HR at firms the client knows [client]; sales collateral, a one-page catalogue for HR (F3 ASK, approved).
- **Left out:** Twitter/X, Threads and Instagram (the buyer profile shows no attention there); Facebook (the client can't run it); Medium (no reach gain for a local B2B buyer).

## Self-check

- [ ] Does the hub follow the rule table?
- [ ] Does every spoke pass both tests, with citations?
- [ ] Is the plan within the cap, or does it quote the client's request for more?
- [ ] Does every channel in `channel-roles.md` appear either in the plan or under "left out"?

## Traps

- **Every channel "because omnichannel".** Omnichannel means every piece reaches every channel *in the plan*. It does not mean every platform.
- **A spoke nobody can run.** Content for a channel with no publisher is waste.
- **A hub the client doesn't own.** A social account is not a hub.
