---
type: llm
weight: 2
---

The original message carries these substantive points: (1) a change was rolled back; (2) it was rolled back because a trial run on a small slice of traffic failed, tied to permissions data not syncing; (3) the cause was an out-of-date expiry setting on one cache, so some reads returned old, pre-merge data; (4) a fix is waiting behind a freeze on changes and is expected at the next window, provided an overnight stability test shows no new problems; (5) until then the old path stays in use; (6) writes can safely be repeated, so nothing is lost.

Pass only if the response conveys all six points in ordinary sentences. Wording may differ and the response may be longer than the original.

Fail if any of the six points is dropped, distorted, or replaced by a shorter summary that omits a qualification (for example the "assuming no regression" condition or the "nothing is lost" reassurance).
