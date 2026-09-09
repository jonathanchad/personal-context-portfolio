# Personal AI Chief of Staff & Agent Architecture

**Date:** 9 September 2026

## The problem

Jonathan has many email accounts and calendars across personal,
consulting, nonprofit, school/PNC, swimming, and individual projects.
Because attention naturally goes to whichever inbox is active, important
messages in lower-volume accounts can be missed until someone follows up
by phone or text.

The goal is not simply "inbox zero". It is to create a reliable
**morning chief-of-staff briefing** that looks across everything and
tells Jonathan what actually needs attention.

## Email accounts mentioned

Current accounts include:

-   Personal Gmail
-   Breakthrough Strategies
-   The Charlotte Project
-   PNC / school-related account
-   Rackley swimming / race-timing responsibilities
-   Liberals Against Nuclear --- operations account
-   Australiansafe.net.au --- operations account
-   Other project-specific accounts as they arise

The system should maintain an explicit account registry rather than
relying on Jonathan to remember which inboxes exist.

## Morning briefing: desired behaviour

The morning briefing should scan **every registered inbox every
morning** and produce one unified briefing organised by importance, not
by inbox.

It should:

1.  Look at recent mail, initially using roughly the **last 72 hours**,
    plus anything unread or still pending that may require action.
2.  Identify messages that need Jonathan's attention, even if they are
    sitting in a low-volume account.
3.  Summarise important messages and identify the likely next action.
4.  Learn Jonathan's definition of "important" over time rather than
    relying only on generic email-priority rules.
5.  Explicitly report which accounts were checked.
6.  Include a **"Nothing to worry about"** section listing accounts
    where nothing requires attention. This gives positive confirmation
    that those inboxes were actually checked.

### Initial importance signals

Examples of things likely to deserve priority include:

-   A direct question or request to Jonathan
-   Someone waiting for Jonathan to respond
-   Deadlines
-   Money, invoices, tax or financial administration
-   Legal or governance matters
-   Family, school or parental responsibilities
-   Important project decisions or dependencies
-   Anything likely to create a problem if ignored

The agent should be trained through examples and Jonathan's corrections
so that its judgement becomes increasingly personalised.

## Calendars

The briefing should also look across **all personal and professional
calendars**.

This includes at least:

-   Breakthrough Strategies
-   The Charlotte Project
-   Personal/family commitments
-   School/parental responsibilities
-   Other project calendars as relevant

The calendars should remain separate at the source. A Charlotte meeting
should still be a Charlotte meeting and a Breakthrough meeting should
still be a Breakthrough meeting.

The morning system should create a **unified view without collapsing the
underlying calendars**.

It should also:

-   Deduplicate the same meeting when it appears on multiple calendars
    or invitations.
-   Tell Jonathan clearly what he has **today**.
-   Look ahead across approximately the **next seven days**.
-   Identify calendar conflicts, overbooking, unusually heavy days,
    insufficient preparation time, deadlines, travel/logistics issues
    and other upcoming "landmines".

## Evolving the morning briefing into a Chief of Staff

The morning briefing should do more than report information. It should
help Jonathan allocate his attention.

In addition to email and calendar summaries, it should suggest **1--3
concrete things Jonathan should do in genuinely open blocks of time**.

This turns the briefing into a lightweight **Morning Chief of Staff**
that answers:

-   What matters today?
-   What am I at risk of missing?
-   What should I do next?
-   Where do I actually have time to do it?
-   What is coming up that I should prepare for now?

## Agent architecture decision

The initial instinct was to consider separate agents for email, calendar
and tasks.

The preferred architecture is instead:

### Specialist agents

Specialist agents can handle narrow domains well, for example:

-   Email triage / importance
-   Calendar analysis
-   Tasks / commitments
-   Meeting notes and follow-up

Jonathan already has a separate agent that reviews meeting notes
approximately every two hours, summarises them and drafts follow-up
emails. That should remain a specialist workflow rather than being
duplicated inside the morning briefing.

### Chief-of-Staff agent

A higher-level Chief-of-Staff agent should combine the relevant outputs
of the specialist systems and make cross-domain judgements about
priorities.

The important distinction is:

> **Specialists understand their domain. The Chief of Staff decides what
> matters across domains.**

There is no need to split everything into more agents immediately. Add
specialist agents where specialisation genuinely improves reliability or
execution.

## Portable agent repository

Jonathan raised the idea of putting all of his agents into a repository
so that they are not locked inside Claude and could eventually be used
by Claude, ChatGPT or other systems.

**Decision: yes.**

Create a **private, platform-neutral repository** that becomes the
source of truth for Jonathan's personal AI system.

The repository should eventually contain:

-   Agent definitions/prompts
-   Shared context
-   Shared priority and judgement rules
-   Account/calendar registry
-   Output schemas
-   Documentation
-   Platform-specific adapters/configuration where necessary

The repository should separate the **intelligence/instructions** from
the **execution platform**. Claude, ChatGPT or another system may
execute an agent, but the core definition should live independently.

## First migration step from Claude

Do **not** refactor everything immediately.

First capture the existing system faithfully:

1.  Create a private repository.
2.  Copy each existing Claude agent's complete instructions into its own
    Markdown file.
3.  Preserve the instructions exactly as they currently exist.
4.  For each agent, record basic metadata such as:
    -   Agent name
    -   Purpose
    -   Trigger
    -   Schedule
    -   Systems/accounts it can access
    -   Inputs
    -   Expected outputs
5.  Once all existing agents are captured, review them together and
    refactor shared logic into common context/rules.

This reduces the risk of breaking working automations while migrating.

## Next step when we return to this

Jonathan will provide the **current instructions for the existing
agents**, starting with the morning briefing.

Then:

1.  Inventory the current agents and what each does.
2.  Map overlaps, gaps and dependencies.
3.  Rewrite the morning briefing as the Morning Chief of Staff.
4.  Define the specialist-agent → Chief-of-Staff handoff.
5.  Design the repo structure and shared rules.
6.  Build a feedback mechanism so Jonathan's corrections improve future
    priority decisions.

## Core design principle

The system should reduce the cognitive burden of remembering where to
look.

Jonathan should not have to think:

> "Which inbox or calendar have I forgotten to check?"

The system should instead tell him:

> **"I checked everything. Here is what matters, here is what does not,
> here is what is coming, and here is what I recommend you do with your
> time."**
