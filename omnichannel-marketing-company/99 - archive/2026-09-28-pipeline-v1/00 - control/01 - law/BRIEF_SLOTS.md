# Brief Slots

**Purpose:** the fixed list of facts every job needs before content can be made. `01 - intake` marks each slot for a new task, `02 - discovery` fills what intake left open, and every later node reads the slots by name. This is the pipeline's shared vocabulary.

## The 12 slots

| # | Slot | The question it answers | Usually filled by | First needed at |
|---|---|---|---|---|
| 1 | SPEAKER | Who is asking, and what is their role in the business (owner, employee, marketer, agency)? | client | 01 - intake |
| 2 | BRAND | Whose name does the content speak under: an existing brand, a new brand, or a third party's brand? | client | 02 - discovery |
| 3 | OFFER | What is being sold? Does it exist yet? What is the price per unit or order? | client | 02 - discovery |
| 4 | BUYER | Who buys, who decides, and who pays? For companies: what kind, what size, where? | client names them; research describes them | 02 - discovery |
| 5 | GOAL | What outcome does the client want, and how will they measure it? | client | 03 - strategy |
| 6 | CHANNELS | What do they run today (site, accounts, email list, ads), and what has worked? | client | 03 - strategy |
| 7 | ASSETS | What exists to work with: name, logo, photos, product facts, past content, reviews? | client | 08 - shaping |
| 8 | VOICE | How does the brand talk? (3–5 real samples) | client | 02 - discovery (voiceprint; planning copies it into every piece brief) |
| 9 | PROOF | Why should a buyer believe them: certifications, results, clients, credentials? | client states them; research sets the standard buyers expect | 03 - strategy |
| 10 | MARKET | What else does the buyer consider: competitors and alternatives? | research | 03 - strategy |
| 11 | LIMITS | Budget, timeline, geography, and any legal or claims rules | client (budget, time, place); research (rules) | 02 - discovery |
| 12 | EXECUTION | Who publishes, who runs ads and spend, who answers leads? | client | 01 - intake (scope) |

## Slot status

| Status | Meaning | Evidence required |
|---|---|---|
| Known | The slot is fully answered | A quote from the client (in the request or in `client/`) or a logged research source |
| Partly known | Part is answered, part is open | The quote for the known part; the open part named in one line |
| Assumed | Not stated, but we proceed on it | Allowed only when a wrong assumption is cheap **and** easy to reverse **and** is shown to the client. Otherwise the slot is Unknown |
| Unknown | Not answered | The open question in one line |

A slot is **filled** when its status is Known. The discovery gate (`02 - discovery/05 - gate/00 - ENTRY.md`) requires every slot first needed at 01 or 02 to be Known, and every other slot to be Known or routed.
