# Mackforge Yolo Alchemy

Usage you haven't spent when your weekly limit resets is gone. `/yolo-alchemy` turns it into research. Run on the evening before the reset, it picks one of your projects, researches one unrelated field (biology, logistics, urban planning and so on), and pairs that field's mechanisms with the project's open problems. If the best pairing can be sketched in under an hour, it builds a throwaway prototype. In the morning you have a short brief, the research notes with their sources, and one line in a running ledger.

## Use it when

- You regularly end the week with usage left over.
- You want a fresh angle on a project you've been stuck inside.

## Set it up

1. Install the plugin (below).
2. Create a scheduled task that runs on the evening before your weekly reset, started in the folder that holds your projects, with the prompt `/yolo-alchemy`. Claude Desktop's scheduled tasks work, as does any scheduler that can run `claude -p "/yolo-alchemy"` in that folder.
3. Optional: in the task's prompt or your instructions file, name a runs folder, a stop time (when the brief must be done) and any projects to skip.

You can also type `/yolo-alchemy` yourself any time you want a run.

## What it does and does not do

- Writes only inside its own runs folder (`yolo-alchemy/runs/` by default). It never writes in the project it studies, and never commits, branches or pushes.
- Searches the web through Claude's own search tool. Sends nothing anywhere else, except a short notification when your session has a messaging or notification tool.
- Does not read your account's usage. The schedule is what keeps it to leftover usage, and it stops early and writes the brief on any rate-limit error.
- If you reply "do it" in the run's session, it switches to normal work inside that project.

## Install

In claude.ai: Customize, then Plugins, then browse the directory for **Mackforge Yolo Alchemy**. In Claude Code: `/plugin marketplace add dtiger1889-ops/mackforge-skills`, then `/plugin install mackforge-yolo-alchemy@mackforge`.

## License

MIT. By Daniel Mack (dtiger1889-ops), [mackforge.dev](https://mackforge.dev). Part of the [mackforge-skills](https://github.com/dtiger1889-ops/mackforge-skills) collection; the standalone version lives at [yolo-alchemy](https://github.com/dtiger1889-ops/yolo-alchemy).
