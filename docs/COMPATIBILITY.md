# Multi-agent compatibility

One `SKILL.md` for all. Differences only in the loader, not the format.

| Field | Required | Claude | Codex | Grok | Notes |
|-------|----------|--------|-------|------|-------|
| `name` | yes | ✅ | ✅ | ✅ | hyphen-case, == folder name, max 64 |
| `description` | yes | ✅ | ✅ | ✅ | what + when, max 1024, English |
| `license` | no | ✅ | ✅ | ✅ | MIT for ours, see THIRD-PARTY for vendors |
| `compatibility` | no | ✅ | ✅ | ✅ (ignores `model`,`effort`) | max 500 chars |
| `metadata` | no | ✅ | ✅ | ✅ (string map) | `author, version, lang` |
| `allowed-tools` | no | ✅ | ⚠️ experimental | ignored | Claude Code only |
| `argument-hint` | no | ignored | ignored | ✅ slash autocomplete |  |
| `user-invocable` | no | n/a | n/a | ✅ default true | `false` hides slash |
| `disable-model-invocation` | no | n/a | `allow_implicit_invocation` in openai.yaml | ✅ |  |

## Paths per agent

| Agent | Repo | User | Extra |
|-------|------|------|-------|
| Claude Code | `.claude/skills/` | `~/.claude/skills/` | plugin `.claude-plugin/` |
| Codex | `$REPO/.agents/skills/` | `~/.agents/skills/` | `/etc/codex/skills`, `agents/openai.yaml` |
| Grok | `./.grok/skills/` | `~/.grok/skills/` | also reads `.claude/`, `.agents/skills/` |
| Cursor | `.cursor/skills/` | `~/.cursor/skills/` |  |
| Copilot | `.github/skills/` | — |  |
| Gemini | `.gemini/skills/` | — |  |

## Test status (update after real tests, 9 active skills)

| Skill | Claude | Codex | Grok | Last test |
|-------|--------|-------|------|-----------|
| hello-agent | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| skill-creator-it | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| invoice-it | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| email-formale-it | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| xlsx-budget-it | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| translate-it-en | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| press-release-it | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| doc-polish-it | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| case-study | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| fattura-elettronica-it | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| regime-forfettario | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| scadenze-fiscali | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| corrispettivi-it | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| pec-bozza | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| sollecito-pagamento | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| verbale-riunione-it | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| preventivo-it | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| nota-spese | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| cv-europass | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| lettera-presentazione | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| colloquio-prep-it | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| dimissioni-procedura | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| bandi-pmi | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| domanda-bando | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| spid-cie-guida | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| privacy-informativa | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| visura-leggimi | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |

Archived generic skills (35 in `archive/`) are not tested or installed.

How to test (local only):
1. `python scripts/install.py --skill hello-agent --agent <agent>`
2. Ask the agent `hello skills` and check the reply table
3. Mark ✅ + date + agent version (e.g. `✅ 2026-09-23 claude-code 1.x`)
4. Repeat for `smart-commit` (sample diff) and `doc-polish-it` (sample file)
