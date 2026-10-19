---
type: llm
weight: 1
---

Pass if the response ends with one concrete next action: a single step the user can take next (for example, swapping one page's conversion to a named library and comparing the output). A closing that bundles the step with a short reason or a "then" follow-up still counts as one action.

Fail if the response ends with a menu of several parallel options, a vague "consider your options", or no next action at all.
