---
type: llm
weight: 2
---

The skill's output contract says it appends ONE JSON line to the runs folder's `ledger.jsonl` with these keys: `date`, `project`, `field`, `folder`, `mechanisms`, `pairings` (each with `title`, `one_line` and `status: "proposed"`), `verified`, and `sources` (the research URLs).

Pass if the response shows a single JSON line (one line, not a pretty-printed block of several records) that contains all of those keys, where every pairing has the status "proposed" and `sources` lists at least one URL. The `folder` value should sit under `yolo-alchemy/runs/` and be named in the form date-time underscore project. Minor differences in date format are fine.

Fail if the line is missing, if it is not valid JSON, if any required key is missing, or if more than one line was appended for this one run.
