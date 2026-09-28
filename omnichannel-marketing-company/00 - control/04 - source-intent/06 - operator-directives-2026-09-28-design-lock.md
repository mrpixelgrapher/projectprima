# Operator directives — 2026-09-28 — design lock (session S003)

Tier 1: verbatim. Never edited. The operator's words are quoted exactly, typos included. Where an answer was a choice between options the assistant offered, the question and the chosen option are recorded as shown, followed by any note the operator typed.

Context: building was paused at the operator's request ("man can you discuss with me. stop the whole building process so we can lock on things properly"), and the design was then dialled in through a discussion and ten rounds of structured questions. Checkpoint before the discussion: commit `4c2487f`.

## Message 1 — answers to the six open decisions

> 1. looks good. but wouldnt it need a wiriting department, and like the sub folder and content for content marketting, for x twitter, linkedin and what not. where the whole cogitive pricess of getting the best content and writing and all gets done as well.
> 2. well I think, per request, creates the calendar the plan, per channel folder, etc etc
> 3. BS, this goes sequentially, because anything skipped will result into faileure.
> 4. nah it doesnt applies! it is for the pricing and offer, upseeling thing. this is a different department. wherein the prices and proposal is set so that this can lead to invioicing and generation of what all will be delivered etc.
> 5. that was for the pricing and offer, upseeling thing
> 6. well an LLM works through one node, using the instructions therein on the task folder and files inside of it. and then once congitively done moves it to the next folder where the LLM then uses the files therein to perform the functions of the task folder.

The six decisions it answered: (1) the ten nodes; (2) the branch unit (one child task per piece); (3) intake sends ≤ 4 questions and moves on without waiting; (4) the free proof-run rule; (5) the phase ladder; (6) one LLM per node.

## Message 2 — answers to A, B, C

> A. it is one node and should be one node. but like basis what the client does and what they want, the ocntent that will need to be pulled from the top creators will be sampled, per client, so the cogintive instructions should be about getting the things and how to carry the research in such detailed steps tha tit make something complicated simple and easy to follow.
> B. some posts will be from different angles on the same topic all leading upto a place on the internet to drive traffic, be it a newsletter or anything else, cross platform integrations and all diving traffix to a single place that lives on the net. as well as indivisual pieces.
> C. your guess is correct! you will build it as a sibling dpeartment.
>
> show me the next round of questions. or yet better keep on using askuserquestions tool to dial in everything

A asked: is the writing department one node? B asked: hub and spoke, or separate per channel? C asked: where the pricing department sits (guess: request → pricing and proposal → content pipeline).

## Structured rounds

| # | Question | Answer (verbatim) |
|---|---|---|
| 1 | Should each client get a permanent folder (brand facts, voice, audience, top-creator samples) that all of their tasks reuse and add to? | Yes, a client folder (Recommended) |
| 1 | Where should the top-creator sampling happen? | Both levels (Recommended) — discovery samples the niche once; writing samples the top posts per topic |
| 1 | Every post drives traffic to one destination online. Who decides it, and do we make what lives there? | Strategy picks, we make it (Recommended) |
| 1 | Once the content is made, who publishes it? | Set per proposal (Recommended) — a publishing node runs only when the proposal includes it |
| 2 | Where does the pricing department sit in the flow? | Intake → pricing → content (Recommended) |
| 2 | How are jobs priced? (fixed packages + add-ons / per deliverable / monthly retainer / custom quote) | 4 leading to 1 then 2 and then 3. |
| 2 | When must the client approve before the task moves on? (proposal / strategy / plan and calendar / final content) | 1, 2 and 3 |
| 2 | Who produces the images and visuals the posts need? | We brief, producer makes (Recommended) |
| 3 | The pricing path: how the company matures, or how one client is upsold? | custom quote is what the client comes for. we give them a proposal of packaged retainers with addons. where the scope and all is fixed as well as deliverables. per deliverable keeps it flexible and retainers gets us quanitity |
| 3 | How does the LLM in a node reach the internet for research and top-creator sampling? | a good research dissier gets created per the ARENA piepline (external piepline that takes a vague request and creates a research dossier out of it). so your point will be limited to option B, with moving that into the aRENA piepline for processing |
| 3 | Which channel families should the writing department cover from the start? | substack, medium and any other,Text social,Visual social,Owned + long-form |
| 3 | After delivery, do we track how the content performed and feed it back? | Only if on retainer |
| 4 | ARENA lives outside this repo. How should our nodes hand work to it and get the dossier back? | do option 2. it doesnt hold once that files get cretaed just write in the relevant instruction file to send it to 'D:\ROOT\CE\03 - work-projects\01 - arena' wherein it has to be processed and once the exec.md file is generated following the arena piepline the dossier will be returned which will then to be ran by the user. |
| 4 | How does a retainer run over time? | a merge of 1 and 2. where last month is reffered and the plan updates every month. it always starts with the next month |
| 4 | What should proposals and invoices use for currency and tax? | Per client |
| 4 | Who approves the price before a proposal reaches the client? | no price book shit. it is derived per sub task that will be done so that detailed invoices can be sent |
| 5 | How is each sub-task's price worked out, since there's no price book? | Effort × rate + costs |
| 5 | When a new retainer month starts, where does that month's cycle enter the line? | At planning (Recommended) |
| 5 | Who carries messages between the pipeline and the client? | You relay (Recommended) |
| 5 | While ARENA works on a request, what happens to the task? | Task waits at that stage |
| 6 | Before a proposal goes to the client, does it wait for your sign-off? | Yes, you sign off (Recommended) |
| 6 | Where does the hourly rate for a client come from? | Rate per kind of work (Recommended) |
| 6 | How are invoices timed? | setup upfront. 50% monthly advance 50 on delivery |
| 6 | Before content is delivered or published, who gives the final check? | review gate. + instructions for manually checking and making sure that it is written like a human showing high degree of clairty of thought compressing excessive knowledge into wisdom |
| 7 | Is every engagement a retainer, or can a client buy a one-off job? | Both (Recommended) |
| 7 | When does the pricing department propose upsells? | At each monthly review,On client request |
| 7 | The CE phase ladder (derive_phase) — what should happen to it? | Map to pricing dept (Recommended) |
| 8 | Intake sits in the commercial department as the company's front door. OK? | Yes, in commercial (Recommended) |
| 8 | Tasks travel by named route, so a task can come back to commercial billing after delivery. OK? | Yes, routes (Recommended) |
| 8 | Is the tree above right overall? | More questions first |
| 9 | One of your sample requests is a performance marketer. Are paid ads in scope? | we do everything. the client and their team runs it. but we provide the performance with testing and optimise campaigns. the organic content is also created around these only. real growth is what we want to deliver |
| 9 | Which languages do we write in? | Per client (Recommended) |
| 9 | When a client has no writing of their own, how is the voice set? | Model on creators |
| 9 | What do we extract from top creators' content? (Never copy text — only patterns.) | all of these. so these criterias and how to do this goes into the congitive documents. these level of breakdowns etc |
| 10 | Where does performance marketing (campaign design) live? | Own node after strategy (Recommended) |
| 10 | Which ad platforms are in scope? | none of the ads. organic content created to go viral on it's own and optimised for ad conversion based on neurological marketing principles so that our organic content has that boost |
| 10 | Should the writing department produce video scripts and storyboards? | the scripts and storyboard. these then goes to one new factory that you will establish for video generation. the key here is to note down that this pipeline will from this storyboard and scripts will then go on to congitively refine, we have an image generation piepline whihc is not a part of this repo but usues NB (nano banana, cutom prompting for scenes, so basically the video deprtment will tell what it wants in the shots, with the trnaisition of camera movement and stop motion everything clearly described. the image generation part goes through the image generation factory to get you all the stills required next to the prompt file, and then using the trnaistion and conematic prompting that you create we will get the motion between the shots. |
| 10 | How often are campaigns optimised, and how does the data come back? | Monthly only |
| 11 | Where does the new video factory sit? | Sibling department (Recommended) |
| 11 | The image generation factory is outside this repo. How do still requests reach it? | Like ARENA, by path |
| 11 | Do all visuals go through the image factory, not just video stills? | Yes, all stills (Recommended) |
| 11 | After the motion between shots is generated, who assembles the final video? | We write the edit plan (Recommended) |
| 12 | What is the image generation factory's folder path in CE? | .CE\03 - work-projects\02 - company\02 - working-companies\design-visual-artist-brand\01 - foundation\13-media-department\03 - media-production\IMAGE_CREATION\00 - INTAKE\01 - queue |
| 12 | Is the revised tree with its routes right? | Approve, build it |
| 12 | Build order: what should be built and shown to you first? | Skeleton, then depth (Recommended) — the whole tree with ENTRYs, routes and tools working end to end for review, then the deep craft files |

## The tree the operator approved (round 12, as shown)

    omnichannel-marketing-company/
    ├── 00 - control/          law (+ task routes, + virality & conversion principles) · tools · state · registers (ARENA + image-factory paths)
    ├── clients/<client>/      profile · voice (own samples, or modelled on creators) · creator library ·
    │                          rates per kind of work · currency & tax · language per channel · results · history
    ├── 01 - commercial/
    │   01 intake → 02 scope → 03 pricing → 04 proposal (your sign-off → client accepts) → 05 billing → 06 month-review · ledgers/
    ├── 02 - content/
    │   01 discovery (ARENA: niche + creator sampling) → 02 strategy (destination; client approves) →
    │   03 performance (virality + neuromarketing conversion design, organic tests, tracking) →
    │   04 planning (month calendar: funnel angles + standalone; client approves) →
    │   05 writing (ARENA per topic · draft · voice · 11 channel crafts · scripts + storyboards · still prompts · review + human check) →
    │   06 packaging → 07 publishing (if in proposal) → 08 delivery
    ├── 03 - video-factory/
    │   01 refine → 02 shots (scene, camera move, transition, stop-motion) → 03 stills (→ image factory, wait) →
    │   04 motion (prompts between stills → you run → clips back) → 05 edit-plan
    └── 99 - archive/

    Routes
    New / one-off:   intake → scope → pricing → proposal → billing → discovery → strategy → performance → planning →
                     writing → [video factory] → packaging → [publishing] → delivery → billing → done
    Retainer month:  month-review (results, upsell) → billing (50% advance) → performance (optimise) → planning →
                     writing → [video] → packaging → [publishing] → delivery → billing → done
