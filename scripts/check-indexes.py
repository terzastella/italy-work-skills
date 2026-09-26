from pathlib import Path
import json
import re
import sys

REPO = Path(__file__).resolve().parents[1]
errors = []

skills = json.loads((REPO / "catalog" / "skills.json").read_text(encoding="utf-8"))
plugin = json.loads((REPO / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))

if skills.get("version") != plugin.get("version"):
    errors.append(f"version mismatch: skills.json {skills.get('version')} vs plugin.json {plugin.get('version')}")

ours = [s["name"] for s in skills["skills"] if "origin" not in s]
vend = [s["name"] for s in skills["skills"] if "origin" in s]
total = len(skills["skills"])
plugin_ours = [p.split("/", 1)[1] for p in plugin["skills"] if p.startswith("skills/")]
plugin_vend = [p.rsplit("/", 1)[1] for p in plugin["skills"] if p.startswith("vendors/")]

if set(ours) != set(plugin_ours):
    errors.append(f"ours set mismatch: only-skills.json={sorted(set(ours) - set(plugin_ours))} only-plugin={sorted(set(plugin_ours) - set(ours))}")
if set(vend) != set(plugin_vend):
    errors.append(f"vendors set mismatch: only-skills.json={sorted(set(vend) - set(plugin_vend))} only-plugin={sorted(set(plugin_vend) - set(ours))}")
if [s["name"] for s in skills["skills"]] != [p.rsplit("/", 1)[1] for p in plugin["skills"]]:
    errors.append("order mismatch: plugin skills order differs from skills.json order")

compat = (REPO / "docs" / "COMPATIBILITY.md").read_text(encoding="utf-8")
collapsed = re.search(
    rf"Full list: {len(ours)} ours \+ {len(vend)} vendors = {total} entries",
    compat)
if collapsed:
    print(f"compat: collapsed summary note ok ({len(ours)}+{len(vend)}={total})")
else:
    missing_compat = [n for n in ours if f"| {n} |" not in compat]
    if missing_compat:
        errors.append(f"COMPATIBILITY.md missing rows: {missing_compat}")

llms = (REPO / "llms.txt").read_text(encoding="utf-8")
registry = (REPO / "catalog" / "_registry.md").read_text(encoding="utf-8")
missing_llms = [n for n in ours if n not in llms]
missing_registry = [n for n in ours if n not in registry]
if missing_llms:
    errors.append(f"llms.txt missing names: {missing_llms}")
if missing_registry:
    errors.append(f"_registry.md missing names: {missing_registry}")

print(f"indexes: {total} entries ({len(ours)} ours + {len(vend)} vendors), versions {skills.get('version')}")
if errors:
    print("INDEX CHECK FAILED:")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)
print("INDEX CHECK OK")
