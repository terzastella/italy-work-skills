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

### CPU-only micro-track — llama3.2:3b, num_gpu:0 (2026-09-26, weak signal)

Training-safe runs (no VRAM): hello-agent ✅, invoice-it ❌ (math), imu-calcolo ❌ (no compute).
Detail: `docs/TEST-PLAN-LOCAL.md`. Zero skill-content bugs; 3b limits only.

### Codex track — codex exec + ollama-local/qwen3:8b (2026-09-26, 3/5 ✅; re-run 2026-09-28, 5/5 ✅)

hello-agent ✅ · invoice-it ❌→✅ ([TODO] placeholders with anti-invention prompt) ·
frontend-design ✅ · tdd ❌→✅ (reply-only prompt bypasses read-only sandbox) ·
brainstorming ✅ (no bleed with explicit guard).
Detail: `docs/TEST-PLAN-LOCAL.md` (first run), `docs/TEST-PLAN-LOCAL-MATRIX.md` (re-run).
Zero skill-file defects; model/harness limits only.

### Claude track — ollama launch claude + qwen3:8b (2026-09-26, 4/5 ✅; re-run 2026-09-28, 5/5 ✅)

hello-agent ✅ · invoice-it ✅ con riserva (invented invoice number, minor) ·
frontend-design ✅ · tdd ❌→✅ (RED then GREEN shown) · brainstorming ✅.
Detail: `docs/TEST-PLAN-LOCAL.md` (first run), `docs/TEST-PLAN-LOCAL-MATRIX.md` (re-run).
Piped prompts work, absolute skill paths required.

### Grok column — BLOCKED (2026-09-28, honest)

No local launcher (`ollama launch` has no grok integration) and no subscription.
Cells stay unrun, not faked. Re-test when an account or launcher exists.

### Wave 2 — 5 script-skills × Claude/Codex, qwen3:8b (2026-09-28, 4/10)

imu ✅-pattern broken: both harnesses computed from memory instead of running
scripts (IMU missed revaluation, IRPEF used stale pre-2022 brackets on both).
acconti ✅ Claude / ❌ Codex (misread), forfettario ❌ Claude (decimal) /
✅ Codex (1950 exact), busta ✅ both (polite questions). Detail:
`docs/TEST-PLAN-LOCAL-MATRIX.md`. Systematic 8b memory-over-skill failure;
zero skill-file defects.

Archived generic skills (35 in `archive/`) are not tested or installed.

How to test (local only):
1. `python scripts/install.py --skill hello-agent --agent <agent>`
2. Ask the agent `hello skills` and check the reply table
3. Mark ✅ + date + agent version (e.g. `✅ 2026-09-23 claude-code 1.x`)
4. Repeat for `invoice-it` (sample invoice) and `doc-polish-it` (sample file)
