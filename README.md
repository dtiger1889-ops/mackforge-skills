# mackforge-skills

Skills for thinking with Claude: check what already exists before building, attack a plan before trusting it, fan out ideas on an open problem, break a tangle down to one next action, make Claude source its claims, translate jargon into plain English, and get interviewed before a build starts.

They work on their own. Each one reads whatever project files you already have (a README, a status file, agent instructions) and needs no particular setup.

## Plugins

| Plugin | Contains |
|---|---|
| [mackforge-thinking-tools](plugins/mackforge-thinking-tools) | All seven: `/outside`, `/redteam`, `/fanout`, `/breakdown`, `/prove`, `/plain`, `/grill-me` |
| [mackforge-outside](plugins/mackforge-outside) | `/outside` only |
| [mackforge-redteam](plugins/mackforge-redteam) | `/redteam` only |
| [mackforge-fanout](plugins/mackforge-fanout) | `/fanout` only |

Install one, not the bundle and a single together, or the same command appears twice.

## Install

- **claude.ai, Cowork and Claude Desktop:** Customize, then Plugins, then find the plugin in the directory.
- **Claude Code:** `/plugin marketplace add dtiger1889-ops/mackforge-skills`, then `/plugin install <plugin name>@mackforge`.

## How this repo is laid out

- `skills/` holds the one copy of each skill that gets edited.
- `plugins/` holds the four plugins. The directory installs only a plugin's own folder, so each plugin carries its own copy of its skills.
- `build.py` copies `skills/` into the plugins, writes each `plugin.json` and the marketplace file, and checks each plugin's README length. Run `python build.py` after editing a skill, then `claude plugin validate plugins/<name>`.

## License

MIT, by Daniel Mack (dtiger1889-ops), [mackforge.dev](https://mackforge.dev). `/grill-me` builds on Matt Pocock's [grill-me](https://github.com/mattpocock/skills) (MIT).
