# commit-scope cases

## Diff in one skill

`git diff --stat`: `skills/json-clean/SKILL.md | 40 ++++`.

Output: `Scope: json-clean (alternative: none, docs: message)`.
Consistency check: `git log --oneline -10` already shows `feat(csv-clean): ...` → reuse style.

## Mixed diff

Stat touches `skills/`, `scripts/`, `docs/` together.

Output: `No scope: 3 different areas. Suggestion: split into 3 commits
(skills, scripts, docs) or use a scopeless message.`
