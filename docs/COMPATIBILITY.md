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
| `disable-model-invocation` | no | n/a | `allow_implicit_invocation` (Codex config, see `.agents/skills/README.md`) | ✅ |  |

## Paths per agent

| Agent | Repo | User | Extra |
|-------|------|------|-------|
| Claude Code | `.claude/skills/` | `~/.claude/skills/` | plugin `.claude-plugin/` |
| Codex | `$REPO/.agents/skills/` | `~/.agents/skills/` | `/etc/codex/skills`, frontmatter `disable-model-invocation` |
| Grok | `./.grok/skills/` | `~/.grok/skills/` | also reads `.claude/`, `.agents/skills/` |
| Cursor | `.cursor/skills/` | `~/.cursor/skills/` |  |
| Copilot | `.github/skills/` | — | CLI also reads `.claude/`, `.agents/skills/` |
| Copilot CLI | `.github/skills/` | `~/.copilot/skills/` | same spec, SDK `skillDirectories` |
| Gemini | `.gemini/skills/` | — |  |
| OpenCode | `.opencode/skills/` | `~/.config/opencode/skills/` | also reads `.claude/`, `.agents/skills/`; permissions in `opencode.json` |
| Windsurf | `.windsurf/skills/` | `~/.codeium/windsurf/skills/` | also reads `.agents/skills/`; invoke explicitly with `@skill-name` |

## Test status — all untested (278 entries, real agent tests deferred)

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

Full list: 254 ours + 24 vendors = 278 entries in `catalog/skills.json` (per-theme catalog in `docs/CATALOG.md`). All rows are untested until real install tests on Claude/Codex/Grok are recorded with date + agent version.
Only Claude/Codex/Grok columns are tracked; all 9 agents are supported by `scripts/install.py`.

## Local track — OpenCode + Ollama qwen3:8b (2026-09-26, 7/9 ✅)

Separate from the official matrix above. Full log: `docs/TEST-PLAN-LOCAL.md`.
Explicit invocation; model ollama 0.32.13 `qwen3:8b` (qwen3.6 too slow on this hardware).

| Skill | Result | Notes |
|---|---|---|
| hello-agent | ✅ | table + path correct; implicit trigger missed, agent self-ID wrong (model limits) |
| invoice-it | ✅ | fixture read, €610 exact, missing-data honesty |
| frontend-design (vendor) | ✅ | brand-aware draft |
| tdd (vendor) | ✅ | test + minimal impl |
| brainstorming (vendor) | ❌ | no questions first, hallucinated skill names (model limit) |
| imu-calcolo | ✅ | script run, 142.800/1.513,68 exact, rate assumption declared |
| irpef-scaglioni | ✅ | dated table, slices + 8190 exact |
| acconti-calcolo | ✅ | threshold + split stated (minor: split presented as rule) |

Archived generic skills (35 in `archive/`) are not tested or installed.

How to test (local only):
1. `python scripts/install.py --skill hello-agent --agent <agent>`
2. Ask the agent `hello skills` and check the reply table
3. Mark ✅ + date + agent version (e.g. `✅ 2026-09-23 claude-code 1.x`)
4. Repeat for `invoice-it` (sample invoice) and `doc-polish-it` (sample file)
