# Security

Public repo. Skills run locally (no data leaves the PC); repo maintenance
checks are described in `docs/INSTALL.md` and `docs/FAQ.md`.

## Never commit

- Tokens/keys: `AKIA...`, `ghp_...`, `github_pat_...`, `xai-...`, `sk-...`, assigned passwords
- PII: emails, real names, private IPs, `C:\Users\<name>`, `/home/<name>` paths
- Files >1MB or binaries without reason

## Dependencies

Zero runtime dependencies: all repo scripts use the Python standard library
only (CI advisory steps may pip-install pinned tools into throwaway runners).
No `requirements.txt` to audit because there is nothing to install.

## Local checks

```bash
python scripts/validate.py
python scripts/security-check.py
```

## Reporting

Use GitHub's **private vulnerability reporting** (Security tab →
Report a vulnerability) so details stay private until fixed.
Never open a public issue with secret content (file + line only, no values).
Never post credentials, tokens, or personal data — not even redacted samples.
