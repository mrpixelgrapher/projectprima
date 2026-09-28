# Client folder

**Purpose:** everything this company knows about one client, kept current by the gates of the nodes that produce it. Read the file you need; each one says what it holds. The client's slug is this folder's name.

| File | Holds | Written by (gate) | Read by |
|---|---|---|---|
| `profile.md` | Who they are: speaker, business, brand mode, offer (one line), goal, channels today, language per channel, execution | `01 - commercial/01 - intake` | every node |
| `rates.md` | Rate per kind of work, currency and tax treatment | `01 - commercial/03 - pricing` | pricing, billing |
| `engagement.md` | What they bought: one-off or retainer, term, deliverables per month, includes, payment schedule | `01 - commercial/04 - proposal` (on acceptance) and `05 - month-review` (on an accepted upsell) | every node; month tasks start from it |
| `brief.md` | The client brief: the 13 slots, each Known or routed | `02 - content/01 - discovery` | strategy onward |
| `voice.md` | The voiceprint: from their own samples, or modelled on named creators | `02 - content/01 - discovery` | planning, writing, video factory |
| `creators.md` | The creator library: top creators per channel and the patterns they use | `02 - content/01 - discovery` | performance, planning, writing |
| `strategy.md` | The approved strategy in full: approval, positioning, messages, the destination, channel plan, objectives | `02 - content/02 - strategy` (after client approval) | performance onward; month tasks |
| `performance.md` | The performance design: conversion path, virality mechanics, tests, tracking | `02 - content/03 - performance` | planning, writing, month-review |
| `results.md` | Retainer results per month, as the client reports them | `01 - commercial/05 - month-review` | performance, planning, upsell |
| `history.md` | One row per task: route, dates, what shipped, invoices, outcome | `01 - commercial/07 - billing-delivery` and any `close` | month-review, pricing |
| `done/` | Finished tasks (DONE or CLOSED), filed by `task.py` | the tool | anyone |
| `versions/` | Replaced client files, dated | gates | anyone |
