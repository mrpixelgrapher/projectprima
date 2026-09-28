# Brief Slots

**Purpose:** the fixed list of facts every job needs. `01 - commercial/01 - intake` marks every slot for a new task and does not let the task go until the slots scope and pricing need are Known; `02 - content/01 - discovery` fills the rest (through the client and ARENA); every later node reads the slots by name. This is the pipeline's shared vocabulary. Version 2 (S003 design lock: slots now first needed at the nodes of the three departments; LANGUAGE added).

## The 13 slots

| # | Slot | The question it answers | Usually filled by | First needed at |
|---|---|---|---|---|
| 1 | SPEAKER | Who is asking, and what is their role in the business (owner, employee, marketer, agency)? | client | intake |
| 2 | BRAND | Whose name does the content speak under: an existing brand, a new brand, or a third party's brand? | client | intake (a new brand adds naming and positioning work to the scope) |
| 3 | OFFER | What is being sold, does it exist yet, and at what price per unit or order? | client | intake (one line); discovery (in full) |
| 4 | BUYER | Who buys, who decides, and who pays? For companies: what kind, what size, where? | client names them; ARENA describes them | discovery |
| 5 | GOAL | What outcome does the client want, how will they measure it, and by when? | client | intake (scope sizes the work to it) |
| 6 | CHANNELS | What do they run today (site, accounts, newsletter, list), what has worked, and where should traffic land? | client | intake (scope decides which channels we cover) |
| 7 | ASSETS | What exists to work with: name, logo, photos, product facts, past content, reviews? | client | writing |
| 8 | VOICE | How does the brand talk? 3–5 real samples, or, when none exist, 1–2 creators to model it on | client | discovery |
| 9 | PROOF | Why should a buyer believe them: certifications, results, clients, credentials? | client states them; ARENA sets the standard buyers expect | strategy |
| 10 | MARKET | What else does the buyer consider: competitors and alternatives? | ARENA | strategy |
| 11 | LIMITS | Budget, timeline, geography, and any legal or claims rules | client (budget, time, place); ARENA (rules) | intake (budget, timeline); strategy (rules) |
| 12 | EXECUTION | Who publishes, and who answers leads and orders? | client | intake (decides `includes publishing`) |
| 13 | LANGUAGE | Which language(s), per channel (e.g. English on LinkedIn, Hinglish on Instagram)? | client | intake (effort per piece depends on it) |

## Slot status

| Status | Meaning | Evidence required |
|---|---|---|
| Known | The slot is fully answered | A quote from the client (in the request or in `from-client/`) or a logged research source |
| Partly known | Part is answered, part is open | The quote for the known part; the open part named in one line |
| Assumed | Not stated, but we proceed on it | Allowed only when a wrong assumption is cheap **and** easy to reverse **and** is shown to the client. Otherwise the slot is Unknown |
| Unknown | Not answered | The open question in one line |

A slot is **filled** when its status is Known. The intake gate (`01 - commercial/01 - intake/06 - gate/00 - ENTRY.md`) requires every slot first needed at intake to be Known. The discovery gate (`02 - content/01 - discovery/06 - gate/00 - ENTRY.md`) requires every slot first needed at intake or discovery to be Known, and every other slot to be Known or routed.
