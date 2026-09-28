#!/usr/bin/env python3
"""Universal installer: copy skills/<name>/ to per-agent destinations.

Usage:
  python scripts/install.py --all
  python scripts/install.py --all --agent claude
  python scripts/install.py --skill invoice-it --agent codex
  python scripts/install.py --skill invoice-it --all --dest ./tmp-test
  python scripts/install.py --all --source vendors --dry-run
  python scripts/install.py --skill invoice-it --agent claude --force

Existing installs are never overwritten unless --force is given.
"""
import argparse
import shutil
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SKILLS = REPO / "skills"
VENDORS = REPO / "vendors"

AGENTS = {
    "claude": [Path.home() / ".claude" / "skills"],
    "codex": [REPO / ".agents" / "skills", Path.home() / ".agents" / "skills"],
    "grok": [Path.home() / ".grok" / "skills"],
    "cursor": [REPO / ".cursor" / "skills"],
    "copilot": [REPO / ".github" / "skills"],
    "copilot-cli": [Path.home() / ".copilot" / "skills"],
    "gemini": [REPO / ".gemini" / "skills"],
    "opencode": [REPO / ".opencode" / "skills", Path.home() / ".config" / "opencode" / "skills"],
    "windsurf": [REPO / ".windsurf" / "skills"],
}

def vendor_roots():
    if not VENDORS.exists():
        return []
    return sorted([p for p in VENDORS.iterdir() if p.is_dir() and p.name != "third-party"])

def available_skills(source):
    found = {}
    if source in ("ours", "all"):
        for p in SKILLS.iterdir():
            if (p / "SKILL.md").exists():
                found.setdefault(p.name, p)
    if source in ("vendors", "all"):
        for root in vendor_roots():
            for p in root.iterdir():
                if (p / "SKILL.md").exists():
                    found.setdefault(p.name, p)
    return found

def install_skill(src, dests, dry=False, force=False):
    if not (src / "SKILL.md").exists():
        print(f"SKIP {src}: missing SKILL.md in {src}")
        return False
    ok = True
    for d in dests:
        target = d / src.name
        print(f"  -> {target}")
        if not dry:
            target.parent.mkdir(parents=True, exist_ok=True)
            if target.exists() and not force:
                print(f"     exists, kept (use --force to replace)")
                continue
            if target.exists():
                shutil.rmtree(target)
            shutil.copytree(src, target)
    return ok

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--skill", default=None)
    ap.add_argument("--agent", default="all",
                    help="claude|codex|grok|cursor|copilot|copilot-cli|gemini|opencode|windsurf|all")
    ap.add_argument("--all", action="store_true",
                    help="install all skills")
    ap.add_argument("--user-only", action="store_true")
    ap.add_argument("--dest", default=None, help="custom destination (test)")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--source", default="ours", choices=["ours", "vendors", "all"],
                    help="ours only (default), vendors only, or all")
    ap.add_argument("--force", action="store_true",
                    help="replace already-installed skills (default: keep existing)")
    args = ap.parse_args()

    skills = available_skills(args.source)
    if not skills:
        print(f"No skills found (source={args.source})")
        return 1
    wanted = sorted(skills) if (args.all or not args.skill) else [args.skill]
    for s in wanted:
        if s not in skills:
            print(f"Unknown skill: {s} (available: {', '.join(sorted(skills))})")
            return 1

    agents = list(AGENTS) if args.agent == "all" else [args.agent]
    if any(a not in AGENTS for a in agents):
        print(f"Unknown agent. Choose from {list(AGENTS)} + all")
        return 1

    for skill in wanted:
        src = skills[skill]
        origin = "vendor" if "vendors" in src.parts else "ours"
        print(f"[install] {skill} ({origin})")
        for ag in agents:
            dests = [Path(args.dest) / ag] if args.dest else AGENTS[ag]
            if args.user_only:
                dests = [d for d in dests if str(d).startswith(str(Path.home()))]
            install_skill(src, dests, dry=args.dry_run, force=args.force)
    print("Done.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
