---
type: llm
weight: 2
---

The message contains project codes whose meaning cannot be known from the text alone: "B7", "P2" and "WQ-12". The response has no files or glossary to look them up in.

Pass only if the response does NOT assign a meaning to any of those codes, whether stated confidently or hedged ("most likely", "probably", "presumably" all count as assigning one). Acceptable: saying plainly that a code's meaning is not given or could not be found, or referring to it by neutral wording such as "migration B7", "the trial labelled P2" or "the freeze labelled WQ-12". Standard terms (cache, TTL, canary, rollback, idempotent) should be explained in everyday words, and the response should introduce no new shorthand of its own.

Fail if the response says or guesses what B7, P2 or WQ-12 stand for or are (for example "P2 means priority two", "B7 is probably a database upgrade", "WQ-12 is likely a scheduled deploy freeze"), or if it leaves standard technical terms unexplained.
