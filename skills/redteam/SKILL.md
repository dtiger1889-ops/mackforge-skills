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
3. Assume the target is wrong and look for how it breaks, then write the
   output below.

## Output

Write these five parts in this order, each under its own bold label. Never
drop or merge a part: the decoy and the check are what a quick critique
skips. If one has nothing real to report, keep the label and say so in a
sentence with the reason.

1. **Strongest failure case**: how the target actually breaks, as a
   mechanism, not a vague risk.
2. **Load-bearing assumption**: the one assumption that sinks the target if
   it is false, stated as an assumption.
3. **Decoy**: the objection that looks important but is not the real problem,
   or the alternative explanation the obvious answer hides, and why.
4. **Cheapest check**: the quickest concrete test (a query, a file read, a
   measurement) that would confirm or disprove the failure case.
5. **Verdict**: exactly one of `survives`, `needs revision`, or `abandon`,
   written verbatim, then the single most consequential fix or reason.
   `survives`: no observed defect breaks the target's goal; checks to run
   and small additions can sit alongside it. `needs revision`: an observed
   defect breaks the goal, but a fix keeps the approach. `abandon`: the
   approach itself cannot meet the goal.

Mark each concern as observed (shown by the facts given) or a hypothesis to
check. Never present a hypothesis as a defect, and never raise a risk the
target already handles. A hypothesis alone does not move the verdict off
`survives`; it becomes the check.

## Delivery and scope

Use one focused pass. Be direct about the evidence and its limits; do not
express certainty beyond it. If the target holds up, say why.

When the original task authorizes revision of your own draft, apply the
confirmed fix and report it. Otherwise deliver the review; a review request
does not itself authorize edits or external actions.
