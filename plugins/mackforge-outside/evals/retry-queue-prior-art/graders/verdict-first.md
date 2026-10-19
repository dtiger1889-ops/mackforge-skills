---
type: llm
weight: 1
---

Pass only if the response opens with (or clearly leads with, before any list of alternatives) a verdict on the current plan that a reader can map without guessing to "survives", "needs revision/changes", or "replace/abandon", together with a reason. A plain-word equivalent counts (for example "don't build this from scratch" or "use an existing library instead").

Fail if the response starts with a list of tools or background and states the verdict only at the end, or never states one.
