---
type: llm
weight: 1
---

Pass only if the response simply fixes the function (for example by returning 0.0 when the list is empty) and does NOT turn into a prior-art or outside-view report. It must not present a verdict on whether the approach "survives" or should be "replaced", must not survey existing libraries or shipped alternatives, and must not frame its ending as a single recommended "next action" after research.

Fail if the response runs a reconnaissance-style report (verdict on the approach, list of existing solutions with sources, a closing next action) instead of, or in addition to, just fixing the code.
