#!/usr/bin/env python3
"""Write README.md from projects.json. Edit projects.json, then run: python3 build.py"""
import json, pathlib

HERE = pathlib.Path(__file__).resolve().parent
projects = json.loads((HERE / "projects.json").read_text())

lines = [
    "# Best of Hermes",
    "",
    "A hand-picked list of projects for [Hermes Agent](https://github.com/NousResearch/hermes-agent), from builders",
    "who make the community better: they try each other's work, give feedback and help out.",
    "",
    "Every project here is open source. Open one, read what it does, try what fits how you work.",
    "",
    f"**{len(projects)} projects from {len({p['builder'] for p in projects})} builders.**",
    "",
    "## Builders",
    "",
]
builders = []
for p in projects:
    if p["builder"] not in builders:
        builders.append(p["builder"])
for b in builders:
    gh = next(p["github"] for p in projects if p["builder"] == b)
    n = sum(p["builder"] == b for p in projects)
    lines.append(f"- [{b}](#{b.lower().replace(' ', '-')}) · [@{gh}](https://github.com/{gh}) · {n} project{'s' if n != 1 else ''}")
for b in builders:
    gh = next(p["github"] for p in projects if p["builder"] == b)
    lines += ["", f"## {b}", "", f"[@{gh}](https://github.com/{gh})", "", "| Project | What it does | Language |", "|---|---|---|"]
    for p in (p for p in projects if p["builder"] == b):
        desc = (p["description"] or "").replace("|", "\\|")
        lines.append(f"| [{p['repo'].split('/')[1]}](https://github.com/{p['repo']}) | {desc} | {p['language'] or ''} |")
lines += [
    "",
    "## Suggest a project",
    "",
    "Open an issue with the repo link and a line on why it belongs here.",
    "",
]
(HERE / "README.md").write_text("\n".join(lines))
print(f"README.md: {len(projects)} projects")
