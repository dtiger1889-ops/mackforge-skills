---
name: outside
description: >-
  Checks shipped solutions, relevant project decisions, and available notes
  before choosing an approach. Use for /outside, check prior art, get an
  outside view, or has anyone already built this. Performs one bounded
  research pass; not multi-frame ideation or a requirements interview.
---

# Outside view

Compare the current approach with what already exists. Prefer adoption or
adaptation when it meets the goal; explain any reason to build from scratch.

## Gather context

1. Establish the problem and current approach from the request. For project
   work, read the relevant state and instruction files before searching.
   Account for settled decisions, constraints, and rejected approaches.
2. Search for shipped solutions and maintained components for this exact
   problem. Start with 1-3 focused searches and inspect the strongest sources.
   Consider major platforms when their workflows are relevant, without
   forcing an agent-platform search onto an unrelated task.
   Always ask one more question: how do the best practitioners of this
   deliverable do it? Look for people who do the work well, not only tools
   built for it, because the default answer tends to be the average one.
   Fold it into one of the searches above when the cap is tight, but never
   drop it. Answer it with a link like any other finding, or say not found.
3. Check the 2-3 most plausible sibling projects for an existing solution.
   Skip when there is no accessible workspace beyond this project.
4. Read a relevant note if the project points to one. Do not sweep an entire
   notes collection. Report any material source-access gap.

Use available free search tools before metered scraping. If an ignore-aware
search hides the target files, explicitly include ignored files or use an
appropriate filesystem search.

## Report

Lead with whether the current approach survives, needs revision, or should
be replaced, and why. Show up to five useful findings or alternatives, with
source links or file locations. Do not manufacture alternatives when the
evidence supports the current approach.

End with one concrete next action. If the original task already authorizes
a repair and the evidence identifies it, complete that repair and report
what changed. Otherwise give the recommendation without assuming permission
to change the artifact.

## Boundaries

One pass, no helper agents. Distinguish not found from confirmed absent.
Keep citations with their claims. Save findings when requested or when the
project's established workflow requires a durable record. If more research
is needed, name the unresolved question and the next check.
