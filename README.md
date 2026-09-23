# Italian Work Skills Hub 🇮🇹

![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Spec: agentskills.io](https://img.shields.io/badge/Spec-agentskills.io-blue.svg)
![Validate: local](https://img.shields.io/badge/Validate-local-yellow.svg)

Il primo hub sistematico di **Agent Skills per il lavoro italiano**: fatture con IVA, email formali, budget, comunicati, traduzioni IT-EN. Skill vere e installabili su Claude, Codex, Grok, Cursor, Copilot con un comando.

Solo locale per ora — pubblicazione su GitHub rinviata.

> Skill tutte in inglese (`-it` = dominio Italia o origine italiana).
> Solo questo README resta in italiano.
> Standard: [Agent Skills open standard](https://agentskills.io) (`SKILL.md` + frontmatter).

## Perché Italia

I grandi repo mondiali (superpowers, mattpocock, ECC) coprono coding e marketing USA. Nessuno copre il lavoro italiano: fattura elettronica e IVA, PEC, email con il `Lei`, forfettario, scadenze, Europass, bandi. Qui ogni skill parla di questi casi, con fonti ufficiali (AdE, INPS, EUR-Lex) e disclaimer "verifica col professionista" dove serve.

## Perché questo repo è diverso

1. **Skill vere e installabili** in `skills/` (formato `SKILL.md` universale)
2. **Installer universale** — 1 comando per Claude / Codex / Grok / Cursor / Copilot
3. **Profondità**: ogni skill ha `SKILL.md` + `references/` + `examples/`
4. **Separazione chiara**: `skills/*` = originali (MIT) vs `catalog/vendors-manifest.json` = solo link alle ufficiali
5. **Validazione locale** con `scripts/validate.py` + `scripts/security-check.py`
6. **Archivio**: le skill generiche pre-restart stanno in `archive/` (consultabili, non installate)

## Quickstart

```bash
git clone https://github.com/terzastella/AI-Skills.git
cd AI-Skills

# Installa tutto ovunque (default: .agents + .claude + .grok + .cursor + .github)
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
| Gemini | `.gemini/skills/` | stesso `SKILL.md` |

## Catalogo skill (MIT, in inglese)

| Skill | Descrizione | Claude | Codex | Grok | Install |
|-------|-------------|--------|-------|------|---------|
| [hello-agent](skills/hello-agent/SKILL.md) | Smoke test: verifica che l'agente veda le skill | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill hello-agent --all` |
| [skill-creator-it](skills/skill-creator-it/SKILL.md) | Crea nuove skill seguendo lo standard repo | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill skill-creator-it --all` |
| [invoice-it](skills/invoice-it/SKILL.md) | Fatture italiane con IVA e totali verificati | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill invoice-it --all` |
| [email-formale-it](skills/email-formale-it/SKILL.md) | Email di lavoro italiane corrette | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill email-formale-it --all` |
| [xlsx-budget-it](skills/xlsx-budget-it/SKILL.md) | Budget Excel con formule e riepilogo | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill xlsx-budget-it --all` |
| [translate-it-en](skills/translate-it-en/SKILL.md) | Traduzioni IT↔EN fedeli, codice intatto | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill translate-it-en --all` |
| [press-release-it](skills/press-release-it/SKILL.md) | Comunicati con lead 5W e contatti | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill press-release-it --all` |
| [doc-polish-it](skills/doc-polish-it/SKILL.md) | Migliora README/docs, tono sobrio | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill doc-polish-it --all` |
| [case-study](skills/case-study/SKILL.md) | Casi studio con numeri veri | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill case-study --all` |
| [fattura-elettronica-it](skills/fattura-elettronica-it/SKILL.md) | Fatture elettroniche via SdI | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill fattura-elettronica-it --all` |
| [regime-forfettario](skills/regime-forfettario/SKILL.md) | Forfettario: soglie 85k/100k e calcoli | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill regime-forfettario --all` |
| [scadenze-fiscali](skills/scadenze-fiscali/SKILL.md) | Scadenze e calendari versamenti | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill scadenze-fiscali --all` |
| [corrispettivi-it](skills/corrispettivi-it/SKILL.md) | Corrispettivi: RT vs software | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill corrispettivi-it --all` |
| [pec-bozza](skills/pec-bozza/SKILL.md) | Bozze PEC con valore legale | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill pec-bozza --all` |
| [sollecito-pagamento](skills/sollecito-pagamento/SKILL.md) | Solleciti a 3 livelli | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill sollecito-pagamento --all` |
| [verbale-riunione-it](skills/verbale-riunione-it/SKILL.md) | Verbali con decisioni e owner | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill verbale-riunione-it --all` |
| [preventivo-it](skills/preventivo-it/SKILL.md) | Preventivi con validità e termini | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill preventivo-it --all` |
| [nota-spese](skills/nota-spese/SKILL.md) | Note spese con giustificativi | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill nota-spese --all` |
| [cv-europass](skills/cv-europass/SKILL.md) | CV Europass misurati | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill cv-europass --all` |
| [lettera-presentazione](skills/lettera-presentazione/SKILL.md) | Cover letter sull'annuncio | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill lettera-presentazione --all` |
| [colloquio-prep-it](skills/colloquio-prep-it/SKILL.md) | Colloqui con metodo STAR | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill colloquio-prep-it --all` |
| [dimissioni-procedura](skills/dimissioni-procedura/SKILL.md) | Dimissioni online e preavviso | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill dimissioni-procedura --all` |
| [bandi-pmi](skills/bandi-pmi/SKILL.md) | Bandi letti con go/no-go | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill bandi-pmi --all` |
| [domanda-bando](skills/domanda-bando/SKILL.md) | Domande con checklist allegati | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill domanda-bando --all` |
| [spid-cie-guida](skills/spid-cie-guida/SKILL.md) | SPID/CIE senza toccare credenziali | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill spid-cie-guida --all` |
| [privacy-informativa](skills/privacy-informativa/SKILL.md) | Informative GDPR con template | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill privacy-informativa --all` |
| [visura-leggimi](skills/visura-leggimi/SKILL.md) | Visure camerali decodificate | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill visura-leggimi --all` |

Legenda: ✅ testata localmente · ⚠️ da verificare · ❌ non supportata

## Skill ufficiali (solo reference, non copiate)

Non duplichiamo codice altrui per licenza e manutenzione. Vedi `catalog/vendors-manifest.json`:

* **Anthropic `anthropics/skills`**: esempi Apache-2.0 + `docx/pdf/pptx/xlsx` (source-available, solo reference).
* **OpenAI Codex**: skills in `.agents/skills/` + `agents/openai.yaml`.
* **xAI Grok**: built-in Word/Presentations/Spreadsheets/PDFs/Skill Creator + docs `.grok/skills/`.

## Struttura repo

```
ai-skills/
  README.md + LICENSE + llms.txt  # root essenziale
  skills/                    # SOURCE OF TRUTH: 27 skill (9 + batch 1-IT da 18)
    tooling: hello-agent/ skill-creator-it/
    cuore: invoice-it/ email-formale-it/ xlsx-budget-it/
      translate-it-en/ press-release-it/ doc-polish-it/ case-study/
    batch1-IT fisco: fattura-elettronica-it/ regime-forfettario/
      scadenze-fiscali/ corrispettivi-it/
    batch1-IT formali: pec-bozza/ sollecito-pagamento/
      verbale-riunione-it/ preventivo-it/ nota-spese/
    batch1-IT lavoro: cv-europass/ lettera-presentazione/
      colloquio-prep-it/ dimissioni-procedura/
    batch1-IT bandi-PA: bandi-pmi/ domanda-bando/ spid-cie-guida/
      privacy-informativa/ visura-leggimi/
    (ognuna: SKILL.md + references/ + examples/)
  archive/                   # skill generiche pre-restart (non installate)
    batch1-generic/ (17) + batch2-seo/ (18)
  templates/skill-starter/   # modello per nuove skill
  catalog/                   # skills.json + vendors-manifest.json + _registry.md
  .agents/skills/README.md   # standard Codex/Cursor/Copilot
  .claude/README.md          # adapter Claude Code (+ .claude-plugin/plugin.json)
  .grok/README.md            # adapter Grok
  .github/skills/README.md   # adapter Copilot
  docs/                      # COMPATIBILITY, CREATE-SKILL, CHATGPT-MIGRATION, THIRD-PARTY, BATCHES
  scripts/install.py + validate.py + security-check.py
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

## Roadmap (solo locale, pubblicazione rinviata)

- [x] Restart Italia 1.0 (9 skill + archivio 35 generiche)
- [x] Batch 1-IT (18 skill: fisco, formali, lavoro, bandi/PA) → totale 27
- [ ] Rinviati da valutare: contratto-base-check, ferie-permessi
- [ ] Test reali su Claude/Codex/Grok e badge in `docs/COMPATIBILITY.md`
- [ ] Batch 2-IT da pianificare (vedi `catalog/_registry.md`)
- [ ] Rinviato (serve GitHub pubblico): CI su PR, submit a skills.sh / agentskills.io
