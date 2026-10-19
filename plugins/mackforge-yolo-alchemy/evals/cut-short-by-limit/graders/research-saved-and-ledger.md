---
type: llm
weight: 1
---

The skill says to save `research.md` in the run folder during the research step (the field, each source URL, the mechanisms extracted), and to always append one JSON line to `ledger.jsonl` at the end, even for a short run, with the keys `date`, `project`, `field`, `folder`, `mechanisms`, `pairings`, `verified` and `sources`.

Pass if the response shows both: research notes written to a `research.md` in a run folder under `yolo-alchemy/runs/` that names a source URL, and a ledger line appended with those keys (a short or empty `pairings` list is acceptable for a cut-short run, and nothing should be claimed in `verified` that was not measured).

Fail if there is no research file, no ledger line, or the ledger line claims measurements or a prototype that did not happen.
