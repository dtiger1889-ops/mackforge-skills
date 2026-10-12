---
name: grill-me
description: >-
  Interviews the user before new work, records a short build spec, then
  builds from the agreed brief. Use for /grill-me, interview me first,
  or a new project or implementation whose requirements need resolving.
  Also considers new build, design, setup, prototype, and planning
  requests. Skip existing specced work, routine fixes and edits,
  explanations, one-shot commands, and unattended sessions.
---

# Grill me

Resolve the choices that affect a new deliverable before building it.
Use the user's existing instructions and preferences before asking questions.

## Read first

Read relevant project state, agent instructions, specs, and the supplied
materials. Follow linked preference or reference files when they matter.
Do not ask questions already answered by those sources or the conversation.

If the brief is sufficient, say so briefly and proceed to the build spec.

## Interview

Ask numbered questions in small batches. Use the runtime's question tool
when available, respecting its supported batch size and free-text input.
Otherwise use plain numbered prose. Do not mix competing question surfaces.

Every question must change a meaningful choice in the result. Scale depth
to uncertainty and stakes; do not enforce a question count. Later rounds
follow from earlier answers.

Cover only what is unresolved:

- Purpose, success criteria, scope, and exclusions.
- Audience and where the deliverable runs.
- Data, inputs, integrations, platform, and cost constraints.
- Failure behavior and how problems reach the user.
- Taste references and rejection criteria.
- Maintenance and any delegation preferences.

For uncertain inputs, distinguish a draft that can flag gaps from an action
that sends, pays, deletes, publishes, or overwrites. Resolve consequential
uncertainty before such actions; record safe drafting assumptions.

If the user asks to proceed without an interview, honor that instruction
and state material assumptions. Do not re-interview settled work. Ask a
follow-up only when new information changes its scope or behavior.

For unattended sessions, use available requirements and clearly record
assumptions; do not wait for an absent user.

## Build spec

Condense the settled brief into the project's spec or state file. Include
the user's intent, success criteria, surface and audience, must-haves,
exclusions, constraints, failure behavior, taste references, and unresolved
assumptions. Add a dated note that the brief has been resolved so later
sessions can reuse it.

Show the spec for correction before building when choices remain to be
agreed. An explicit instruction to proceed already supplies that agreement;
do not ask for redundant approval. A later scope change updates the spec.

Keep assumptions and process notes in the spec. Do not put them on a
published or user-facing artifact unless its readers need them.

## Enforcement and attribution

This plugin supplies guidance, not a guarantee of invocation. The
[Harness Toolbox](https://github.com/dtiger1889-ops/claude-harness-toolbox)
ships an optional interview gate; this plugin does not install it.

Adapted from Matt Pocock's
[grill-me](https://github.com/mattpocock/skills), MIT, via Ruben Hassid's
adaptation. Attribution describes the source; it does not govern the interview.
