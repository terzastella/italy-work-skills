# refactor-plan cases

## Duplication across 2 scripts

Input: `install.py` and `deploy.py` with the same 30-line config reader.

Output:
```text
Goal: a single config reader
Guard: both scripts run with sample config
Step 1: extract config.py with load() | Verify: diff output before/after
Step 2: use load() in install.py | Verify: test install --dry-run
Step 3: use load() in deploy.py | Verify: test deploy --dry-run
Risks: different paths → mitigation: base_dir parameter
```

## No tests

Output: mandatory step 0 `add 1 test on install --dry-run output` before touching code.
