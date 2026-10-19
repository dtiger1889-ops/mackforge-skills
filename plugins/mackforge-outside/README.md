# Mackforge Outside View

Before Claude commits to building something, `/outside` makes it look outside its own head first. It runs one short reconnaissance pass: a few web searches for tools, libraries and published skills that already solve the problem, a look at your other projects for the same problem shape, and a check of the one note that applies. Then it reports.

The report has a fixed order: a verdict on the current approach (survives, dies, or changes), up to five things that already exist with a source link for each, and exactly one next action. Adapting what exists is the default; building from scratch has to give a reason.

## Example

You ask Claude for a job scheduler that retries failed jobs with backoff. Without the command, it starts writing the retry loop straight away. Run `/outside` first and it searches for maintained job queues and retry libraries, checks whether one of your other projects already has a queue, and comes back with a verdict (for example "changes: use a library"), a short list of candidates with links, and one next action, such as adding the library and wiring one job to it. You still write code, just less of it.

## Use it when

- You are about to build a component that someone has probably built already.
- A plan feels like it came from inside one conversation.
- You want to know whether you are reinventing the wheel.

Type `/outside` or say "check prior art" or "has anyone already built this".

## What it does and does not do

- Runs web searches through Claude's own search tool. Sends nothing anywhere else and stores nothing.
- Reads your project files and notes only to orient; it does not change them.
- One pass, no sub-agents. "Nothing shipped does this" is a valid result.

## Install

In claude.ai: Customize, then Plugins, then browse the directory for **Mackforge Outside View**. In Claude Code: `/plugin marketplace add dtiger1889-ops/mackforge-skills`, then `/plugin install mackforge-outside@mackforge`.

## License

MIT. By Daniel Mack (dtiger1889-ops), [mackforge.dev](https://mackforge.dev). Part of the [mackforge-skills](https://github.com/dtiger1889-ops/mackforge-skills) collection.
