---
type: llm
weight: 1
---

Pass only if the response opens with (or clearly leads with, before any list of alternatives) a verdict that the regex-based converter plan should be replaced or revised in favour of an existing parser, with a reason. Plain-word equivalents count (for example "don't write this yourself; use an existing Markdown library").

Fail if the response supports building the regex converter from scratch, hides the verdict at the end, or never states one.
