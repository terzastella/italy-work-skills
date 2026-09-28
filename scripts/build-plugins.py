#!/usr/bin/env python3
"""Generate per-harness plugin manifests from catalog/skills.json.

Source of truth stays catalog/skills.json. Never hand-edit the outputs:
  .codex-plugin/plugin.json, .cursor-plugin/plugin.json, gemini-extension.json
CI rebuilds and fails on diff (plugins-sync check).

Usage:
  python scripts/build-plugins.py
"""
import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
CATALOG = REPO / "catalog" / "skills.json"

HARNESSES = {
    ".codex-plugin/plugin.json": "codex",
    ".cursor-plugin/plugin.json": "cursor",
}


def main():
    data = json.loads(CATALOG.read_text(encoding="utf-8"))
    skills = data["skills"]
    ours = [f"skills/{s['name']}" for s in skills if "origin" not in s]
    vend = [f"vendors/{s['origin'].split('/', 1)[1]}/{s['name']}" for s in skills if "origin" in s]
    paths = ours + vend

    for rel, harness in HARNESSES.items():
        manifest = {
            "name": data["name"],
            "description": f"Italian Work Skills Hub for {harness} ({len(ours)} originals + {len(vend)} pinned third-party).",
            "version": data["version"],
            "author": {"name": "ai-skills-hub"},
            "license": "MIT",
            "skills": paths,
        }
        out = REPO / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"wrote {rel}: {len(paths)} skills, v{data['version']}")

    gemini = {
        "name": data["name"],
        "version": data["version"],
        "description": f"Italian Work Skills Hub for Gemini ({len(ours)} originals + {len(vend)} pinned third-party).",
        "author": "ai-skills-hub",
        "license": "MIT",
        "skills": paths,
    }
    (REPO / "gemini-extension.json").write_text(
        json.dumps(gemini, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote gemini-extension.json: {len(paths)} skills, v{data['version']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
