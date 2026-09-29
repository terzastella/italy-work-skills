# Italian Work Skills Hub 🇮🇹

![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Spec: agentskills.io](https://img.shields.io/badge/Spec-agentskills.io-blue.svg)
![Gates: CI](https://img.shields.io/badge/Gates-validate%20%7C%20security%20%7C%20evals%20%7C%20freshness-green.svg)

> 🇮🇹 Italiano? Leggi [`README-IT.md`](README-IT.md).

**254 English agent skills for Italian work** — e-invoices with VAT, formal `Lei` emails,
flat-rate tax math, Europass CVs, public grants — plus 24 pinned third-party skills.
Installable on Claude, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode
and Windsurf with one command. Spec: [Agent Skills open standard](https://agentskills.io).

New here? Start with [`docs/USER-GUIDE.md`](docs/USER-GUIDE.md) · Installing: [`docs/INSTALL.md`](docs/INSTALL.md) · Questions: [`docs/FAQ.md`](docs/FAQ.md).

```bash
git clone https://github.com/terzastella/italy-work-skills.git
cd italy-work-skills
python scripts/install.py --all                          # original skills (default)
python scripts/install.py --skill invoice-it --agent claude
```

## Why Italy

Global skill repos focus on coding and marketing. This hub focuses on Italian work:
e-invoicing via SdI, PEC certified mail, the forfettario scheme, tax deadlines,
Europass, public grants. Every skill here speaks those cases, cites official
sources (AdE, INPS, EUR-Lex) and carries a "verify with a professional" disclaimer
where it matters. See [`docs/METHODOLOGY.md`](docs/METHODOLOGY.md) for the philosophy.

## Why this repo is different

1. **Real installable skills** in `skills/` (universal `SKILL.md` format)
2. **Universal installer** — 1 command for 9 agents
3. **Depth**: `SKILL.md` + `references/` + `examples/` + neutral `scripts/` with fixtures
4. **Executable where safe**: 30 stdlib calculators (tax totals, instalments, accruals,
   budgets) — rates and tables are dated inputs, never bundled truth
5. **Honest boundaries**: 36 sensitive skills are info-only + professional referral
   (audited in `docs/AUDITS.md`); delicate topics never ship code
6. **Verified locally**: `validate.py` + `security-check.py` + deterministic
   `eval-golden.py` (all calculation checks green) + index coherence checks in CI

## Destinations

| Agent | Destination |
|-------|-------------|
| Claude Code | `~/.claude/skills/` or `.claude/skills/` (+ `.claude-plugin/plugin.json`) |
| Codex | `.agents/skills/` |
| Grok | `~/.grok/skills/` (also reads `.claude/`, `.agents/skills/`) |
| Cursor | `.cursor/skills/` |
| Copilot | `.github/skills/` |
| Copilot CLI | `~/.copilot/skills/` |
| Gemini | `.gemini/skills/` |
| OpenCode | `.opencode/skills/` |
| Windsurf | `.windsurf/skills/` (invoke with `@name`) |

`skills/*/SKILL.md` also works with `gh skill install`.

## Skill catalog (MIT, English)

254 skills in 16 themes — full catalog in [`docs/CATALOG.md`](docs/CATALOG.md)
(generated from `catalog/skills.json`, do not edit by hand):

- [Fisco e tasse](docs/CATALOG.md#fisco-e-tasse) (35) · [Lavoro](docs/CATALOG.md#lavoro) (46) · [Casa](docs/CATALOG.md#casa) (26)
- [PA e documenti](docs/CATALOG.md#pa-e-documenti) (19) · [Impresa](docs/CATALOG.md#impresa) (22) · [Salute](docs/CATALOG.md#salute) (20)
- [Soldi e banche](docs/CATALOG.md#soldi-e-banche) (17) · [Trasporti e viaggi](docs/CATALOG.md#trasporti-e-viaggi) (14) · [Famiglia](docs/CATALOG.md#famiglia) (14)
- [Scuola e giovani](docs/CATALOG.md#scuola-e-giovani) (10) · [Tutele e consumi](docs/CATALOG.md#tutele-e-consumi) (7) · [Giustizia](docs/CATALOG.md#giustizia) (6)
- [Successioni e donazioni](docs/CATALOG.md#successioni-e-donazioni) (8) · [Pensioni](docs/CATALOG.md#pensioni) (4) · [Scrittura e contenuti](docs/CATALOG.md#scrittura-e-contenuti) (4) · [Tooling](docs/CATALOG.md#tooling) (2)

### Featured

| Skill | Why |
|-------|-----|
| [invoice-it](skills/invoice-it/SKILL.md) | Italian invoices with verified VAT math (+ script) |
| [regime-forfettario](skills/regime-forfettario/SKILL.md) | 85k/100k gates + tax math (+ script) |
| [fattura-elettronica-it](skills/fattura-elettronica-it/SKILL.md) | SdI e-invoices without rejections |
| [imu-calcolo](skills/imu-calcolo/SKILL.md) | Property tax base/rate math (+ script + tables) |
| [irpef-scaglioni](skills/irpef-scaglioni/SKILL.md) | Bracket slices, marginal vs average (+ script) |
| [naspi-guida](skills/naspi-guida/SKILL.md) | Benefit gates without myths |
| [isee-guida](skills/isee-guida/SKILL.md) | DSU without the classic mistakes |
| [bandi-pmi](skills/bandi-pmi/SKILL.md) | Honest go/no-go on grants |
| [hello-agent](skills/hello-agent/SKILL.md) | 10-second smoke test |

Install: `python scripts/install.py --skill <name> --all` (full table in `docs/CATALOG.md`).

## Third-party skills (pinned copies in `vendors/`, opt-in)

24 verbatim byte-identical copies pinned in `vendors/upstreams.lock.json`:

* **Anthropic** (10, Apache-2.0) · **Matt Pocock** (6, MIT) · **Superpowers** (8, MIT)

```bash
python scripts/install.py --all --source vendors         # originals + third-party
python scripts/install.py --skill tdd --source vendors   # one third-party skill
```

Deliberately excluded (`docx/pdf/pptx/xlsx`: source-available, link-only) and
no-copy guides (Codex/Grok have no public repos). Licenses: `vendors/README.md`,
`docs/THIRD-PARTY-NOTICES.md`.

## Repo layout

```
ai-skills/
  README.md (this file) + README-IT.md + LICENSE + llms.txt
  skills/                    # SOURCE OF TRUTH: 254 originals (MIT)
  archive/                   # frozen pre-restart generics (not installed)
  vendors/                   # 24 pinned third-party (never hand-edit)
  templates/skill-starter/   # new-skill template
  catalog/                   # skills.json (278 entries) + manifests + _registry.md
  docs/                      # USER-GUIDE, INSTALL, FAQ, GLOSSARY, CATALOG, METHODOLOGY, ...
  scripts/                   # install + validate + security + catalog + evals + versioning
```

Rule: **edit only in `skills/`**, the rest is generated/copied.

## Create a new skill

```bash
cp -r templates/skill-starter skills/my-skill
# edit, then:
python scripts/validate.py --skill my-skill
python scripts/security-check.py
python scripts/eval-golden.py  # if you touched a skill with scripts/
```

Full guide: `docs/CREATE-SKILL.md`. For Italy skills: official sources + professional disclaimer.

## Licenses

* `skills/*`, `templates/*`, `scripts/*`, docs: **MIT** (see `LICENSE`).
* Anthropic `docx/pdf/pptx/xlsx` are **source-available, not open-source** — linked, never copied.
* Tax/law skills are informative drafts, not professional advice.

## Roadmap

Status: **v1.16 — 254 originals + 24 pinned third-party = 278 entries** (history in `CHANGELOG.md`).
`main` may contain unreleased changes; use a tagged release for reproducible installs.

- [x] 254 skills complete and deepened, 30 calculators verified (63/63 golden + 15/15 oracles + 19/19 invariants green)
- [x] Sensitive topics audited: information + professional referral, never verdicts
- [x] First real-agent runs logged (`docs/TEST-PLAN-LOCAL.md`)
- [ ] Real-agent tests on Claude/Codex/Grok (`docs/TEST-PLAN.md` ready, badges to follow)
- [x] Public repo
- [ ] skills.sh/marketplace submit (then maintenance only)
