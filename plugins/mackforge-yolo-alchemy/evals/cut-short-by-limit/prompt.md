---
max_turns: 25
allowed_tools: [Skill, Write, Read, WebSearch, WebFetch]
tags: [should-fire, budget]
---

/yolo-alchemy

Run settings: the projects folder is the current directory; it holds one project, "seed-swap" (a neighborhood app for trading garden seeds, whose open problem is keeping trades fair when people offer very different amounts). Runs folder: `yolo-alchemy/runs/`. Skip list: none. No delivery channel is configured.

Scenario for this test: you have exactly one source's worth of time. After you save the research notes for the first source you read, treat the very next step as having failed with a usage-limit error ("rate limit reached"), and act as your instructions say for that situation. Do not read further sources and do not prototype. Finish by pasting the complete text of `brief.md` and the ledger line into your final reply.
