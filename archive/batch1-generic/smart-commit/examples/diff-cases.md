# smart-commit cases

## 1. Small diff → ideal commit

```diff
+def slugify(t):
+    return t.lower().replace(" ", "-")
```

Proposal:
```text
feat(utils): add slugify for skill names
```
Alternatives:
```text
feat(utils): add slug helper for names
chore(utils): add slugify function
```

## 2. Large diff (>200 lines) → summarize then commit

`git diff --stat`:
```text
 scripts/install.py | 120 ++++++++
 skills/x/SKILL.md  |  90 +++++
```

Behavior: summarize per file first (install: new destinations; skill x: new instructions),
then ONE proposal:
```text
feat(installer): add cursor and gemini destinations
```

## 3. Diff with secret → block

```diff
+API_KEY = "xai-abc123..."
```

Behavior: no proposal. Reply:
```text
BLOCKED: possible secret in <file>:<line>. Remove it, use env var, then resubmit diff.
Command: python skills/smart-commit/scripts/check-diff.py
```
