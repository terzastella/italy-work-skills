# git-status-express cases

## Typical dirty repo

```text
M  skills/smart-commit/SKILL.md
M  scripts/validate.py
?? skills/json-clean/
```

Output:
```text
Repo: ai-skills | Branch: main | Dirty
Staged: 0 files | Unstaged: 2 files | Untracked: 1 file
Areas touched: skills (1), scripts (1)
Main files: skills/smart-commit/SKILL.md, scripts/validate.py, skills/json-clean/ [new]
Next step: validate with python scripts/validate.py --skill json-clean
```

## Clean repo

Output: `Clean repo on main, nothing to do.`
