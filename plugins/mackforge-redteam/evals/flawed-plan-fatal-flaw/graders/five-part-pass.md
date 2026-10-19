---
type: llm
weight: 1
---

Pass only if the response contains all five of these, each recognizable on its own (headings are not required, but each must be clearly present, not merely implied):

1. The strongest failure case, with how it would actually happen.
2. The single assumption whose failure would invalidate the plan, stated as an assumption (for example, that daily prices are fresh enough for the promise being made).
3. A plausible alternative explanation or decoy concern that the obvious critique could hide or that looks important but is not the real problem.
4. A cheapest concrete check that could confirm or disprove the suspected flaw (for example, comparing one day of hourly feed data against the 6:00 am snapshot and counting the sales missed).
5. An explicit overall verdict that a reader can map without guessing to one of "survives", "needs revision", or "abandon" (those words or plain equivalents), together with the most consequential fix or reason.

Fail if any of the five is missing.
