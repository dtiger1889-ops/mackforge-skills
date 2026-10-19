---
max_turns: 6
allowed_tools: [Skill]
tags: [should-not-fire, plain-task]
---

Here is a Python function that is supposed to return the average of a list, but it crashes on an empty list. Fix it.

def average(values):
    return sum(values) / len(values)

Return 0.0 for an empty list.
