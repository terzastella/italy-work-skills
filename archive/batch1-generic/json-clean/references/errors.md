# Common JSON errors → mechanical fix

| Error | Signal | Fix |
|-------|--------|-----|
| Trailing comma | `},]` / `,}` | remove comma |
| Single quotes | `'key'` | → double |
| Comments | `//` or `/*` | remove (it is JSONC, declare it) |
| BOM | weird chars at start | save UTF-8 without BOM |
| Unclosed quote | parser line N | close, re-verify |
| Duplicate key | 2× same key | ask which to keep |

Mechanical only. Dubious values/structure → flag, do not invent.
Validate with `python -m json.tool file.json` after each fix.
