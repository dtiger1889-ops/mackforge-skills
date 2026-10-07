# Mackforge Think Twice

Seven skills for thinking with Claude instead of just accepting its first answer. Each one is a slash command you call when you want it; none of them run on their own.

| Command | What it does |
|---|---|
| `/outside` | Checks what already exists (tools, your other projects, your notes) before you build. Verdict first, one next action last. |
| `/redteam` | Assumes a plan or answer is wrong and finds the most likely fatal flaw, plus the cheapest check that settles it. |
| `/fanout` | Five thinking frames and a critic on an open-ended problem. Uses about seven times the tokens of a normal answer. |
| `/breakdown` | Turns one tangled problem into the smallest next action, the one blocking decision, and a collapsed plan. |
| `/prove` | Makes Claude back up the claims in its last answer with sources, and retract what it cannot source. |
| `/plain` | Re-explains a dense, jargon-heavy answer in plain English, looking up every code instead of guessing. |
| `/grill-me` | Interviews you in short rounds before building something new, then writes down a build spec. |

The same `outside`, `redteam` and `fanout` skills are also listed on their own, if you only want one.

## What they do and do not do

- They read your project files to orient and use Claude's own web search where a step calls for it. They send nothing anywhere else.
- They store nothing unless you ask: `/grill-me` writes its build spec into your project, and `/fanout` offers to save its synthesis.
- `/fanout` starts sub-agents in Claude Code and Cowork and runs its frames in sequence where sub-agents are not available.

## Install

In claude.ai: Customize, then Plugins, then browse the directory for **Mackforge Think Twice**. In Claude Code: `/plugin marketplace add dtiger1889-ops/mackforge-skills`, then `/plugin install mackforge-thinking-tools@mackforge`.

## Credit and license

`/grill-me` builds on Matt Pocock's [grill-me](https://github.com/mattpocock/skills) (MIT). MIT. By Daniel Mack (dtiger1889-ops), [mackforge.dev](https://mackforge.dev). Source: [mackforge-skills](https://github.com/dtiger1889-ops/mackforge-skills).
