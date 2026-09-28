#!/usr/bin/env python3
"""Advisory Agent Skills spec check via upstream skills-ref (demo-only tool).

Usage:
  python scripts/check-spec.py

Requires: pip install "git+https://github.com/agentskills/agentskills.git#subdirectory=skills-ref"
Without it the check SKIPS (exit 0) — our own scripts/validate.py stays
the binding gate. Exit 2 on spec divergences; CI runs this as
non-blocking (upstream marks skills-ref demonstration-only).

Known intentional divergences (see docs/METHODOLOGY.md):
  - flow-style `metadata: {author: ..., version: ...}` (strictyaml rejects flow)
  - extra top-level fields (argument-hint, user-invocable, ...)
"""
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]

try:
    from skills_ref import validate
except ImportError:
    print("check-spec: skills-ref not installed, SKIP (pip install from agentskills/agentskills#skills-ref)")
    sys.exit(0)


def main():
    bad, total = 0, 0
    for d in sorted((REPO / "skills").iterdir()):
        if not d.is_dir() or not (d / "SKILL.md").is_file():
            continue
        total += 1
        errs = validate(d)
        if errs:
            bad += 1
            print(f"[SPEC-DIVERGE] {d.name}:")
            for e in errs[:3]:
                print(f"  - {str(e)[:160]}")
    print(f"check-spec: {total - bad}/{total} skills pass upstream skills-ref")
    return 2 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
