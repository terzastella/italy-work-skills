#!/usr/bin/env python3
"""Installer attack simulation: symlinked skills must be rejected.

Creates a fake evil skill (dir symlink + inner-file symlink) in the system
temp dir, asserts install.py refuses both, cleans up. Needs symlink rights
(Linux/macOS CI, Windows admin/dev-mode). Exit 2 on failure, 0 when blocked.

Usage:
  python scripts/check-installer.py
"""
import importlib.util
import os
import shutil
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]


def load_installer():
    spec = importlib.util.spec_from_file_location(
        "ins", REPO / "scripts" / "install.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    try:
        tmp = Path(tempfile.mkdtemp(prefix="evilskill-"))
        outside = tmp / "outside"
        outside.mkdir()
        (outside / "SKILL.md").write_text("stolen")
        evil = tmp / "evilskill"
        evil.symlink_to(outside, target_is_directory=True)
        inner = tmp / "innerskill"
        inner.mkdir()
        (inner / "SKILL.md").write_text("x")
        (inner / "leak.md").symlink_to(outside / "SKILL.md")
    except OSError as e:
        print(f"installer-attack-test: SKIP (no symlink rights: {e})")
        return 0
    try:
        ins = load_installer()
        assert evil.is_symlink(), "test setup failed"
        assert ins.has_symlink(evil), "dir-symlink not detected"
        assert ins.install_skill(evil, [tmp / "dest"], dry=True) is False
        assert ins.has_symlink(inner), "inner symlink not detected"
        assert ins.install_skill(inner, [tmp / "dest"], dry=True) is False
        print("installer-attack-test: symlink attacks blocked")
        return 0
    except AssertionError as e:
        print(f"[FAIL] installer-attack-test: {e}")
        return 2
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    raise SystemExit(main())
