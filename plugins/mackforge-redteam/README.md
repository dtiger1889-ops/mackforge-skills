# Red Team

`/redteam` gives a plan, claim or answer one focused adversarial pass. It assumes the target is wrong and hunts for the fatal flaw, instead of agreeing with it. It is the cheap middle step between accepting Claude's first answer and running a full multi-agent review.

Every pass returns the same five parts:

1. The strongest case that it is wrong, with the mechanism of how it breaks.
2. The silent assumption it depends on.
3. The decoy: whether the obvious answer is a trap, and what the real one is.
4. The cheapest disproof: one command, file read or measurement that would settle it.
5. A verdict (survives, needs revision, abandon) and the single most important fix.

If the target genuinely holds up, it says so plainly rather than inventing a flaw.

## Use it when

Type `/redteam` or say "push back on this", "red-team this" or "stress-test this".

## What it does and does not do

- Reads the target, and the project's own state files when the target belongs to a project.
- Sends nothing anywhere and stores nothing. One pass, no sub-agents.

## Install

In claude.ai: Customize, then Plugins, then browse the directory for **Red Team**. In Claude Code: `/plugin marketplace add dtiger1889-ops/mackforge-skills`, then `/plugin install mackforge-redteam@mackforge`.

## License

MIT. By Daniel Mack (dtiger1889-ops), [mackforge.dev](https://mackforge.dev). Part of the [mackforge-skills](https://github.com/dtiger1889-ops/mackforge-skills) collection.
