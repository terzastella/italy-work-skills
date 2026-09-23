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
| Copilot | `.github/skills/` | — | CLI also reads `.claude/`, `.agents/skills/` |
| Copilot CLI | `.github/skills/` | `~/.copilot/skills/` | same spec, SDK `skillDirectories` |
| Gemini | `.gemini/skills/` | — |  |
| OpenCode | `.opencode/skills/` | `~/.config/opencode/skills/` | also reads `.claude/`, `.agents/skills/`; permissions in `opencode.json` |
| Windsurf | `.windsurf/skills/` | `~/.codeium/windsurf/skills/` | also reads `.agents/skills/`; invoke explicitly with `@skill-name` |

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
| partita-iva-apri | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| ateco-scelta | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| acconti-calcolo | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| ritenuta-acconto | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| operazioni-estero | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| fattura-pa | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| imu-calcolo | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| cu-730-guida | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| busta-paga-leggi | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| naspi-guida | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| isee-guida | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| bollette-energia | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| bonus-casa | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| sanita-digitale | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| affitto-check | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| pagopa-guida | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| garanzie-consumo | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| recesso-acquisti | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| isa-check | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| tirocinio-guida | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| nota-credito | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| contributi-inps | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| agevolazioni-assunzioni | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| ditta-vs-srl | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| camera-commercio | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| durc | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| maternita-congedi | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| malattia-certificato | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| apprendistato | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| contratto-tipi | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| condominio-spese | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| mutuo-tassi | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| compravendita-casa | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| auto-bollo | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| assegno-unico | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| anagrafe-certificati | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| passaporto-procedura | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| voli-ritardi | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| banche-reclami | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |
| vacanze-pacchetto | ⚠️ untested | ⚠️ untested | ⚠️ untested | — |

Archived generic skills (35 in `archive/`) are not tested or installed.

How to test (local only):
1. `python scripts/install.py --skill hello-agent --agent <agent>`
2. Ask the agent `hello skills` and check the reply table
3. Mark ✅ + date + agent version (e.g. `✅ 2026-09-23 claude-code 1.x`)
4. Repeat for `smart-commit` (sample diff) and `doc-polish-it` (sample file)
