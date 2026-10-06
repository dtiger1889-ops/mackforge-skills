"""Assemble the plugin folders from the shared skills/ sources.

The directory installs only a plugin's own folder, so each plugin needs its own copy of every
skill it lists and of the LICENSE. skills/ is the one place a skill is edited; this script copies
it into each plugin, writes each plugin.json and the marketplace file, and checks the result.

Run from the repository root:  python build.py
"""
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
VERSION = "1.0.0"  # raise with every release; the directory serves the newest version
AUTHOR = {"name": "Daniel Mack", "url": "https://mackforge.dev"}
REPO = "https://github.com/dtiger1889-ops/mackforge-skills"

PLUGINS = {
    "mackforge-outside": {
        "displayName": "Outside View",
        "description": "Before committing to an approach, one quick check of what already exists: shipped tools, your other projects, your notes. Verdict first, one next action last.",
        "skills": ["outside"],
        "keywords": ["prior-art", "research", "planning"],
    },
    "mackforge-redteam": {
        "displayName": "Red Team",
        "description": "One adversarial pass that assumes your plan or answer is wrong, finds the most likely fatal flaw, and names the cheapest check that settles it.",
        "skills": ["redteam"],
        "keywords": ["critique", "review", "decision-making"],
    },
    "mackforge-fanout": {
        "displayName": "Fanout",
        "description": "Five parallel thinking frames plus a critic on an open-ended problem: scored ideas, the traps each one carries, and the strongest direction.",
        "skills": ["fanout"],
        "keywords": ["ideation", "brainstorming", "design"],
    },
    "mackforge-thinking-tools": {
        "displayName": "Thinking Tools",
        "description": "Seven skills for thinking with Claude: check prior art, attack a plan, fan out ideas, break a problem down, prove claims, translate jargon, and interview before building.",
        "skills": ["outside", "redteam", "fanout", "breakdown", "prove", "plain", "grill-me"],
        "keywords": ["thinking", "planning", "critique", "research", "prompting"],
    },
}


def build():
    lic = ROOT / "LICENSE"
    for name, spec in PLUGINS.items():
        pdir = ROOT / "plugins" / name
        if not (pdir / "README.md").is_file():
            sys.exit(f"{name}: plugins/{name}/README.md is missing (write it by hand first)")
        sdir = pdir / "skills"
        if sdir.exists():
            shutil.rmtree(sdir)
        for skill in spec["skills"]:
            src = ROOT / "skills" / skill
            if not (src / "SKILL.md").is_file():
                sys.exit(f"{name}: skills/{skill}/SKILL.md is missing")
            shutil.copytree(src, sdir / skill)
        shutil.copyfile(lic, pdir / "LICENSE")
        manifest = {
            "name": name,
            "displayName": spec["displayName"],
            "version": VERSION,
            "description": spec["description"],
            "author": AUTHOR,
            "homepage": REPO,
            "repository": REPO,
            "license": "MIT",
            "keywords": spec["keywords"],
        }
        (pdir / ".claude-plugin").mkdir(exist_ok=True)
        (pdir / ".claude-plugin" / "plugin.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
        words = len((pdir / "README.md").read_text(encoding="utf-8").split())
        if words < 40:
            sys.exit(f"{name}: README has {words} words; the directory requires at least 40")
        print(f"built {name}: {', '.join(spec['skills'])}")

    marketplace = {
        "name": "mackforge",
        "description": "mackforge skills for thinking with Claude.",
        "owner": AUTHOR,
        "plugins": [
            {"name": n, "source": f"./plugins/{n}", "description": s["description"]}
            for n, s in PLUGINS.items()
        ],
    }
    (ROOT / ".claude-plugin").mkdir(exist_ok=True)
    (ROOT / ".claude-plugin" / "marketplace.json").write_text(json.dumps(marketplace, indent=2) + "\n", encoding="utf-8")
    print("wrote .claude-plugin/marketplace.json")


if __name__ == "__main__":
    build()
