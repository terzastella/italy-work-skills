# Pull request

## What

- [ ] New skill(s):
- [ ] Fix / docs / toolchain:

## Checklist (must all be green)

- [ ] `python scripts/validate.py` — zero FAIL
- [ ] `python scripts/security-check.py` — clean
- [ ] JSON indexes parse (`catalog/skills.json`, `.claude-plugin/plugin.json`)
- [ ] `python scripts/install.py --all --dest ./tmp-test --dry-run` — ok
- [ ] `python scripts/build-catalog.py --check` — clean, `docs/CATALOG.md` regenerated if needed
- [ ] `python scripts/eval-golden.py` — green (if touching a skill with `scripts/`)

## Indexes updated (when adding a skill)

- [ ] `catalog/skills.json` + `.claude-plugin/plugin.json` (version bump)
- [ ] `llms.txt` + `docs/COMPATIBILITY.md`
- [ ] `catalog/_registry.md` (one name once) + `docs/BATCHES.md` + `CHANGELOG.md`

## Notes for reviewers

Skill content in English; fiscal figures carry their year; examples use marked
fake data. Delicate skills: info-only + professional referral, no verdicts.
`vendors/` and `archive/` are never touched by content PRs.
