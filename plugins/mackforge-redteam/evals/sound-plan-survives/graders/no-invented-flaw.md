---
type: llm
weight: 1
---

Pass only if the response does not present a speculative risk as an established defect. Any concerns it raises must be framed as possibilities to check (hypotheses), not as observed problems, and none of them may be something the prompt already shows is handled (for example, claiming the export may be incomplete when the full export was imported and spot-checked, or that there is no rollback when a 60-day read-only fallback exists).

Fail if the response asserts a fatal or serious flaw that the facts in the prompt do not support, or treats an already-handled risk as unaddressed.
