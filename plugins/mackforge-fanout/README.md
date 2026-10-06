# Fanout

`/fanout` attacks an open-ended problem from five different angles at once, then has a critic sort the results. It is for questions with many valid answers: a design, an API shape, a name, a strategy, a set of hypotheses.

Five sub-agents each take one vantage (systems, adversarial, first principles, operator, outsider) and produce several ideas with the traps each one carries. A sixth agent scores them, groups the ones that converged, lists every distinct trap, and deepens the top three with the riskiest assumption behind each and the cheapest way to test it. You see the top three, the trap list and a short synthesis.

## Use it when

- The problem is open-ended and the decision matters.
- Not for debugging or anything with one checkable answer; the skill checks this first and tells you when a single answer is the better tool.

Type `/fanout` or say "fanout this" or "give me frames on X".

## Cost

It runs six agents, so it uses roughly seven times the tokens of a normal answer. It never runs automatically. In Claude Code and Cowork it runs the five frames in parallel; where sub-agents are not available it runs them one after another in the same conversation.

## What it does and does not do

- Sends nothing outside Claude and stores nothing unless you ask it to save the synthesis.

## Install

In claude.ai: Customize, then Plugins, then browse the directory for **Fanout**. In Claude Code: `/plugin marketplace add dtiger1889-ops/mackforge-skills`, then `/plugin install mackforge-fanout@mackforge`.

## License

MIT. By Daniel Mack (dtiger1889-ops), [mackforge.dev](https://mackforge.dev). Part of the [mackforge-skills](https://github.com/dtiger1889-ops/mackforge-skills) collection.
