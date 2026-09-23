#!/usr/bin/env python3
"""Universal installer: copy skills/<name>/ to per-agent destinations.

Usage:
  python scripts/install.py --all
  python scripts/install.py --all --agent claude
  python scripts/install.py --skill smart-commit --agent codex
  python scripts/install.py --skill smart-commit --all --dest ./tmp-test
"""
import argparse
import shutil
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SKILLS = REPO / "skills"

AGENTS = {
    "claude": [Path.home() / ".claude" / "skills"],
    "codex": [REPO / ".agents" / "skills", Path.home() / ".agents" / "skills"],
    "grok": [Path.home() / ".grok" / "skills"],
    "cursor": [REPO / ".cursor" / "skills"],
    "copilot": [REPO / ".github" / "skills"],
    "gemini": [REPO / ".gemini" / "skills"],
}

def available_skills():
    return sorted([p.name for p in SKILLS.iterdir() if (p / "SKILL.md").exists()])

def install_skill(skill, dests, dry=False):
    src = SKILLS / skill
    if not (src / "SKILL.md").exists():
        print(f"SKIP {skill}: missing SKILL.md in {src}")
        return False
    ok = True
    for d in dests:
        target = d / skill
        print(f"  -> {target}")
        if not dry:
            target.parent.mkdir(parents=True, exist_ok=True)
            if target.exists():
                shutil.rmtree(target)
            shutil.copytree(src, target)
    return ok

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--skill", default=None)
    ap.add_argument("--agent", default="all",
                    help="claude|codex|grok|cursor|copilot|gemini|all")
    ap.add_argument("--all", action="store_true",
                    help="installa tutte le skill")
    ap.add_argument("--user-only", action="store_true")
    ap.add_argument("--dest", default=None, help="destinazione custom (test)")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    skills = available_skills()
    if not skills:
        print("No skills in skills/")
        return 1
    wanted = skills if (args.all or not args.skill) else [args.skill]
    for s in wanted:
        if s not in skills:
            print(f"Unknown skill: {s} (available: {', '.join(skills)})")
            return 1

    agents = list(AGENTS) if args.agent == "all" else [args.agent]
    if any(a not in AGENTS for a in agents):
        print(f"Unknown agent. Choose from {list(AGENTS)} + all")
        return 1

    for skill in wanted:
        print(f"[install] {skill}")
        for ag in agents:
            dests = [Path(args.dest) / ag] if args.dest else AGENTS[ag]
            if args.user_only:
                dests = [d for d in dests if str(d).startswith(str(Path.home()))]
            install_skill(skill, dests, dry=args.dry_run)
    print("Done.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
