# commit-scope path → scope map

| Paths touched | Proposed scope |
|---------------|----------------|
| `skills/<name>/` | `<name>` |
| `scripts/` | `scripts` |
| `docs/` | `docs` |
| `catalog/` | `catalog` |
| `templates/` | `templates` |
| `.agents/`, `.claude/`, `.grok/`, `.github/` | `config` |
| root (`README`, `LICENSE`) | no scope (`docs:`/`chore:`) |

Compare with `git log --oneline -10`: if a similar scope was used, reuse it.
New module → new scope, flag it as new.
