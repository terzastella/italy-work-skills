# Italian Work Skills Hub 🇮🇹

> 🇬🇧 English showcase: [`README.md`](README.md). Questa pagina resta il punto
> d'ingresso italiano.

![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Spec: agentskills.io](https://img.shields.io/badge/Spec-agentskills.io-blue.svg)
![Validate: local](https://img.shields.io/badge/Validate-local-yellow.svg)

Il primo hub sistematico di **Agent Skills per il lavoro italiano**: fatture con IVA, email formali, budget, comunicati, traduzioni IT-EN. Skill vere e installabili su Claude, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode e Windsurf con un comando.

Repo pubblica, sviluppo per branch e tag. Dettaglio avanzamento in `CHANGELOG.md`.

> Skill tutte in inglese (`-it` = dominio Italia o origine italiana).
> Solo questa pagina (`README-IT.md`) resta in italiano.
> Standard: [Agent Skills open standard](https://agentskills.io) (`SKILL.md` + frontmatter).

## Perché Italia

I grandi repo mondiali (superpowers, mattpocock, ECC) coprono coding e marketing USA. Nessuno copre il lavoro italiano: fattura elettronica e IVA, PEC, email con il `Lei`, forfettario, scadenze, Europass, bandi. Qui ogni skill parla di questi casi, con fonti ufficiali (AdE, INPS, EUR-Lex) e disclaimer "verifica col professionista" dove serve.

## Perché questo repo è diverso

1. **Skill vere e installabili** in `skills/` (formato `SKILL.md` universale)
2. **Installer universale** — 1 comando per 9 agenti (Claude, Codex, Grok, Cursor, Copilot, Copilot CLI, Gemini, OpenCode, Windsurf)
3. **Profondità**: ogni skill ha `SKILL.md` + `references/` + `examples/`
4. **Separazione chiara**: `skills/*` = originali (MIT) vs `catalog/vendors-manifest.json` = solo link alle ufficiali
5. **Validazione locale** con `scripts/validate.py` + `scripts/security-check.py`
6. **Archivio**: le skill generiche pre-restart stanno in `archive/` (consultabili, non installate)

## Quickstart

```bash
git clone https://github.com/terzastella/italy-work-skills.git
cd italy-work-skills

# Installa tutto ovunque (9 agenti: claude, codex, grok, cursor, copilot, copilot-cli, gemini, opencode, windsurf)
python scripts/install.py --all

# Oppure solo una skill su un agente
python scripts/install.py --skill invoice-it --agent claude
python scripts/install.py --skill invoice-it --agent codex
python scripts/install.py --skill invoice-it --agent grok

# Verifica che tutto rispetti la spec agentskills.io
python scripts/validate.py
python scripts/security-check.py
```

Destinazioni:

| Agente | Destinazione | Note |
|--------|--------------|------|
| Claude Code | `~/.claude/skills/` o `.claude/skills/` | + plugin via `.claude-plugin/plugin.json` |
| Codex (ChatGPT dev) | `.agents/skills/` | standard Codex, vedi `.agents/skills/README.md` |
| ChatGPT (app) | via Plugin / Codex | Custom GPT in dismissione sett-dic 2026, vedi `docs/CHATGPT-MIGRATION.md` |
| Grok | `~/.grok/skills/` | compatibile anche con `.claude/` e `.agents/` |
| Cursor | `.cursor/skills/` | stesso `SKILL.md` |
| Copilot | `.github/skills/` | stesso `SKILL.md` |
| Copilot CLI | `~/.copilot/skills/` | personale, legge anche `.github/` e `.agents/` |
| Gemini | `.gemini/skills/` | stesso `SKILL.md` |
| OpenCode | `.opencode/skills/` | legge anche `.claude/` e `.agents/` |
| Windsurf | `.windsurf/skills/` | invoca esplicito con `@nome-skill` |

> Formato `skills/*/SKILL.md` compatibile anche con `gh skill install`.

## Catalogo skill (MIT, in inglese)

254 skill organizzate in 16 temi — catalogo completo in [`docs/CATALOG.md`](docs/CATALOG.md)
(generato da `catalog/skills.json`, non modificare a mano):

- [Fisco e tasse](docs/CATALOG.md#fisco-e-tasse) (35) · [Lavoro](docs/CATALOG.md#lavoro) (46) · [Casa](docs/CATALOG.md#casa) (26)
- [PA e documenti](docs/CATALOG.md#pa-e-documenti) (19) · [Impresa](docs/CATALOG.md#impresa) (22) · [Salute](docs/CATALOG.md#salute) (20)
- [Soldi e banche](docs/CATALOG.md#soldi-e-banche) (17) · [Trasporti e viaggi](docs/CATALOG.md#trasporti-e-viaggi) (14) · [Famiglia](docs/CATALOG.md#famiglia) (14)
- [Scuola e giovani](docs/CATALOG.md#scuola-e-giovani) (10) · [Tutele e consumi](docs/CATALOG.md#tutele-e-consumi) (7) · [Giustizia](docs/CATALOG.md#giustizia) (6)
- [Successioni e donazioni](docs/CATALOG.md#successioni-e-donazioni) (8) · [Pensioni](docs/CATALOG.md#pensioni) (4) · [Scrittura e contenuti](docs/CATALOG.md#scrittura-e-contenuti) (4) · [Tooling](docs/CATALOG.md#tooling) (2)

### In evidenza

| Skill | Perché |
|-------|--------|
| [invoice-it](skills/invoice-it/SKILL.md) | Fatture italiane con IVA verificata |
| [regime-forfettario](skills/regime-forfettario/SKILL.md) | Soglie 85k/100k e calcoli |
| [fattura-elettronica-it](skills/fattura-elettronica-it/SKILL.md) | XML via SdI senza scarti |
| [email-formale-it](skills/email-formale-it/SKILL.md) | Il `Lei` fatto bene |
| [pec-bozza](skills/pec-bozza/SKILL.md) | Valore legale preservato |
| [naspi-guida](skills/naspi-guida/SKILL.md) | Requisiti senza miti |
| [isee-guida](skills/isee-guida/SKILL.md) | DSU senza errori |
| [bandi-pmi](skills/bandi-pmi/SKILL.md) | Go/no-go onesto |
| [hello-agent](skills/hello-agent/SKILL.md) | Smoke test 10 secondi |

Installazione: `python scripts/install.py --skill <nome> --all` (tabella completa in `docs/CATALOG.md`).


## Skill di terzi (copie pinnate in `vendors/`, opt-in)

24 skill originali altrui, file byte-identici pinnati ai commit in `vendors/upstreams.lock.json`:

* **Anthropic** (10, Apache-2.0): `frontend-design`, `skill-creator`, `mcp-builder`, `webapp-testing`, `claude-api`, `brand-guidelines`, `doc-coauthoring`, `internal-comms`, `canvas-design`, `theme-factory`
* **Matt Pocock** (6, MIT): `tdd`, `diagnosing-bugs`, `code-review`, `research`, `to-spec`, `prototype`
* **Superpowers** (8, MIT): `brainstorming`, `writing-plans`, `executing-plans`, `systematic-debugging`, `test-driven-development`, `using-git-worktrees`, `requesting-code-review`, `verification-before-completion`

```bash
python scripts/install.py --all                          # solo nostre (default)
python scripts/install.py --all --source vendors         # nostre + terze
python scripts/install.py --skill tdd --source vendors   # una skill terza
```

Escluse apposta (`docx/pdf/pptx/xlsx` Anthropic: source-available, solo link) e senza repo da copiare (Codex/Grok: restano guide). Dettagli e licenze: `vendors/README.md`, `docs/THIRD-PARTY-NOTICES.md`.

## Skill ufficiali (solo reference, non copiate)

Non duplichiamo codice altrui per licenza e manutenzione. Vedi `catalog/vendors-manifest.json`:

* **Anthropic `anthropics/skills`**: esempi Apache-2.0 + `docx/pdf/pptx/xlsx` (source-available, solo reference).
* **OpenAI Codex**: skills in `.agents/skills/` + frontmatter `disable-model-invocation` (vedi `.agents/skills/README.md`).
* **xAI Grok**: built-in Word/Presentations/Spreadsheets/PDFs/Skill Creator + docs `.grok/skills/`.

## Struttura repo

```
ai-skills/
  README.md + LICENSE + llms.txt  # root essenziale
  skills/                    # SOURCE OF TRUTH: 254 skill originali
    tooling + cuore (9) + skill per temi fiscali/lavoro/casa/salute/scuola/PA
    + 5 percorsi guidati multi-tappa (vedi sotto)
    (ognuna: SKILL.md + references/ + examples/ — catalogo per temi in docs/CATALOG.md)
    percorsi guidati: percorso-apri-partita-iva/ percorso-assunzione-domestica/
      percorso-casa-compravendita/ percorso-lutto/ percorso-busta-controllo/
  archive/                   # skill generiche pre-restart (non installate)
    batch1-generic/ (17) + batch2-seo/ (18)
  vendors/                   # 24 skill terze pinnate (mai modificare a mano)
    anthropics-skills/ (10) + mattpocock-skills/ (6) + superpowers/ (8)
    + upstreams.lock.json + third-party/ + README.md
  templates/skill-starter/   # modello per nuove skill
  catalog/                   # skills.json (278 entries) + vendors-manifest.json + _registry.md
  .agents/skills/README.md   # standard Codex/Cursor/Copilot
  .claude/README.md          # adapter Claude Code (+ .claude-plugin/plugin.json)
  .grok/README.md            # adapter Grok Code
  .github/skills/README.md   # adapter Copilot + Copilot CLI
  .opencode/skills/README.md # adapter OpenCode
  .windsurf/skills/README.md # adapter Windsurf (invocazione @nome)
  docs/                      # USER-GUIDE, INSTALL, FAQ, GLOSSARY, CATALOG, METHODOLOGY...
  scripts/install.py + validate.py + security-check.py + build-catalog.py + sync-vendors.py
```

Regola: **modifica solo in `skills/`**, il resto è generato/copiato da `install.py`.

## Creare una nuova skill

```bash
cp -r templates/skill-starter skills/mia-skill
# edita skills/mia-skill/SKILL.md (name == nome cartella, description con cosa+quando)
python scripts/validate.py --skill mia-skill
```

Guida completa: `docs/CREATE-SKILL.md`. Per skill Italia: aggiungi fonti ufficiali + disclaimer professionista.

## Licenze

* `skills/*`, `templates/*`, `scripts/*`, docs: **MIT** (vedi `LICENSE`).
* Skill ufficiali linkate in `catalog/vendors-manifest.json`: restano dei rispettivi proprietari. In particolare `docx/pdf/pptx/xlsx` di Anthropic sono **source-available, non open-source** — non copiarle, linkale (vedi `docs/THIRD-PARTY-NOTICES.md`).
* Le skill fisco/legge sono bozze informative, non consulenza professionale.

## Roadmap

Stato: **v1.16 — 254 skill nostre + 24 terze pinnate = 278 entries** (storia in `CHANGELOG.md`).

- [x] 254 skill complete e approfondite, 30 calcoli verificati (63/63 controlli verdi)
- [x] Temi sensibili blindati: solo informazioni + rinvio al professionista, mai verdetti
- [x] Primi test reali registrati (`docs/TEST-PLAN-LOCAL.md`)
- [ ] Test reali sugli agenti e badge in `docs/COMPATIBILITY.md`
- [ ] Rinviato (serve repo pubblica): submit a skills.sh / agentskills.io
