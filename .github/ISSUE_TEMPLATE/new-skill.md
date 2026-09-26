---
name: New skill
about: Propose a new skill for skills/
title: "[skill] "
labels: new-skill
---

## Name (hyphen-case, == folder name)

## Trigger ("Use when...")

## What the skill does (2 lines, English)

## Delicate? (legal/health/family → info-only + referral, no verdicts)

## References structure planned

- `references/`:
- `examples/` (fake data marked):
- `scripts/` (neutral calculators only, stdlib):

## Checklist for the author (see docs/CREATE-SKILL.md)

- [ ] `python scripts/validate.py --skill <name>` green
- [ ] Indexes: `catalog/skills.json`, `llms.txt`, `.claude-plugin/plugin.json`, `docs/COMPATIBILITY.md`, `docs/CATALOG.md`
