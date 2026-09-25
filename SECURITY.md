# Security

Local only for now. No data leaves the PC.

## Never commit

- Tokens/keys: `AKIA...`, `ghp_...`, `xai-...`, `sk-...`, assigned passwords
- PII: emails, real names, private IPs, `C:\Users\<name>`, `/home/<name>` paths
- Files >1MB or binaries without reason

## Local checks

```bash
python scripts/validate.py
python scripts/security-check.py
```

## Reporting

Repo still private/local: report verbally to the owner with file:suspicious line.
Once on public GitHub, open a `security` issue without including the secret.
