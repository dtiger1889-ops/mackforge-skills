---
name: redteam
description: >-
  Reviews a claim, plan, or answer from one adversarial perspective. Use only
  for /redteam, push back on this, red-team this, or stress-test this.
  Identifies the strongest failure mechanism and the check that could
  settle it. Not broad ideation or routine fact-checking.
---

# Red team

Test the target's strongest assumptions without manufacturing a flaw.

## Review

1. Resolve the target from the request, referenced artifact, or prior turn.
   Ask once if the target is materially ambiguous.
2. For project artifacts, read the relevant state and instructions.
   Account for actual constraints and decisions already resolved.
3. Identify:
   - The strongest failure case and how it would occur.
   - The assumption whose failure would invalidate the plan.
   - Any plausible alternative explanation the obvious answer hides.
   - The cheapest concrete check that could disprove the suspected flaw.
4. Give a verdict: survives, needs revision, or abandon, with the most
   consequential reason or fix. Distinguish observed defects from hypotheses.

## Opinion mode

Use this only when the user hands over their own stated opinion together
with material in the same request ("here is what I think, here is the
data"). A bare claim, plan, or answer gets the ordinary review above.

- Read the relevant project state even if no project file is named, so
  current state outranks a stale excerpt. If there is no project, say so.
- Replace the first three items of step 3 with the three strongest
  arguments against the user's opinion. Each one quotes the line from the
  material or project files that supports it. Use nothing from general
  knowledge. If the material supports fewer than three, give fewer and say
  so; never pad. The cheapest check and the verdict still follow.

## Delivery and scope

Use one focused pass. Be direct about the evidence and its limits; do not
express certainty beyond it. If the target holds up, say why.

When the original task authorizes revision of your own draft, apply the
confirmed fix and report it. Otherwise deliver the review; a review request
does not itself authorize edits or external actions.
