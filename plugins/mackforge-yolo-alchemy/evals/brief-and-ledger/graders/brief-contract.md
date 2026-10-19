---
type: llm
weight: 2
---

The skill's output contract says the morning brief names the project and the foreign field, gives one paragraph per supported pairing with the mechanism first, says what was prototyped (or that nothing was), and ends with exactly ONE next action the user could take.

Pass if the pasted brief has all of these:

1. One of the two projects (pantry-tracker or route-planner) is named as the target, and one field clearly unrelated to it is named (biology, logistics, game design and so on).
2. At least one pairing, written so that the field's mechanism is stated before or as the lead of how it applies to a named open problem of the project.
3. A single, concrete next action.

Fail if the response contains no brief text, if the brief lacks a foreign field or a project, if it offers only a list of generic ideas with no mechanism, or if it gives several competing next actions instead of one.
