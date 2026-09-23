# release-notes cases

## Release with breaking change

Input: CHANGELOG 1.0.0 entry + diff with renamed `config.yaml`.

Output:
```markdown
# 1.0.0 — New universal installer

In short: 1-command install, 20 new skills, renamed config.

## New
- `install.py --all` installer for 6 agents
- 20 verified English skills

## Breaking
- `config.yaml` → `settings.yaml`. Migration: `mv config.yaml settings.yaml`.

## Upgrade
`python scripts/install.py --all`
```

## Empty release (advised against)

Output: `Only 2 minor fixes since v0.2: accumulate before releasing.`
