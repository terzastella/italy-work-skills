# Review severity scale

| Level | Meaning | Examples |
|-------|---------|----------|
| SEVERE | bug, flaw, crash, secret | SQL injection, hardcoded key, `except: pass` on critical |
| MEDIUM | likely error, poor handling | missing None check, no timeout, magic numbers |
| MINOR | style, nit | unclear name, long line, unused import |

Verdicts: BLOCKED (≥1 severe) · NEEDS WORK (≥1 medium) · ACCEPTABLE (minor/none only).
