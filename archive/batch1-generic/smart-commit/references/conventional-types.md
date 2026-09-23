# Conventional commit types — EN

Format: `<type>(<scope>): <description>` — max 72 chars, imperative, lowercase.

| Type | When | Example |
|------|------|---------|
| `feat` | new feature | `feat(auth): add refresh token rotation` |
| `feat` | new skill | `feat(skills): add csv-validator` |
| `fix` | bug | `fix(ui): fix table overflow on mobile` |
| `docs` | docs | `docs(readme): add compatibility matrix` |
| `refactor` | refactor, same behavior | `refactor(scripts): simplify install.py` |
| `test` | tests | `test(validate): add folder-name case` |
| `chore` | maintenance | `chore(deps): update vendors-manifest` |
| `build` | build | `build(installer): copy assets too` |
| `ci` | automation | `ci(validate): add PII check` |

Scope: one lowercase word (folder/module/function). If no scope fits, omit it:
`docs: fix README typos`.
