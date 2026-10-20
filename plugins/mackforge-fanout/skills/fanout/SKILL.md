---
name: fanout
description: >-
  Explores an open-ended problem through five distinct thinking frames
  followed by one critic pass. Use only for /fanout, run a fanout, fanout
  this, or give me frames on this. Not routine debugging or verification
  with one checkable answer. Multiple agent passes consume more usage
  than a single response.
---

# Fanout

Generate different approaches, then assess their fit and failure modes.

## Select and ground the task

Use this for a problem with multiple valid answers. If the request has
one checkable answer, explain why a focused analysis fits and ask whether
the user still wants the five-frame treatment. Clarify a vague topic before
launching agents.

For project work, read relevant state and instructions. Give every frame
and the critic the same problem, source material, and load-bearing
constraints, including settled decisions and rejected approaches.

## Five frames

Use the runtime's native agent tool for five parallel frames, within its
concurrency and model limits. If no agent tool exists, work through the
frames sequentially and disclose that they share one model context.
Do not launch nested CLI sessions as a workaround.

Assign each frame one vantage:

1. **Systems:** states, data flows, transformations, concurrency and scale.
2. **Adversarial:** hidden assumptions, failure mechanisms and decoys.
3. **First principles:** actual requirements and underlying mechanisms.
4. **Operator:** field failures, edge cases, recovery and maintenance.
5. **Outsider:** intuitive alternatives and jargon that conceals weak reasoning.

Ask each for 4-6 distinct approaches where the problem supports them,
with mechanisms and traps. Keep outputs compact, without self-ranking
or file writes unless requested. Do not fill a quota with redundant ideas.

## Critic

After the frames return, give one critic the original brief, constraints,
and all five outputs. Ask it to:

- Score approaches on novelty, viability, and fit, with reasons.
- Cluster equivalent strategies and identify agreement across frames.
- Deduplicate traps while retaining their mechanisms.
- Deepen the strongest three directions, or fewer if fewer are viable:
  sharpen the idea, identify its riskiest assumption, and name a concrete
  test and first step.
- Synthesize the strongest direction and the evidence still needed.
- Spread: list each frame's single highest-scored idea in one line,
  labelled "chance another AI gives this: N%", ordered high to low so the
  rarest comes last.

Agreement is a useful signal, not proof that an approach is correct.
Scores are judgments, not calibrated probabilities.

## Deliver

Show the spread first, so an idea only one frame reached is not buried
under the ones several frames agreed on. Then present the strongest
directions, distinct traps, and synthesis, with a concise note on
convergence. Do not dump raw frame transcripts unless
asked. Offer to save useful conclusions in the project's own records;
keep raw outputs ephemeral unless saving was requested.

One run per invocation. Do not claim a fixed cost multiplier or a
guaranteed improvement without a relevant measurement.
