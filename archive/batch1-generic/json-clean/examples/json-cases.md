# json-clean cases

## Trailing commas + comments

Input (`conf.json`):
```text
{
  // local config
  "name": "hub",
  "ports": [8080, 8081,],
}
```

Report:
```text
File: conf.json | Errors: 2 | Status: VALID
Fixes: line 2 comment removed (was JSONC); line 4 trailing comma removed
Doubts: none | Output: conf.clean.json
```

## Duplicate key (blocked)

Output: `Lines 8 and 15: duplicate "timeout" key (30 vs 60). Which to keep?`
No automatic fix on values.
