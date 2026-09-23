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
| [partita-iva-apri](skills/partita-iva-apri/SKILL.md) | Aprire partita IVA: regime e passi | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill partita-iva-apri --all` |
| [ateco-scelta](skills/ateco-scelta/SKILL.md) | Codice ATECO giusto e perché | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill ateco-scelta --all` |
| [acconti-calcolo](skills/acconti-calcolo/SKILL.md) | Acconti con metodo storico | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill acconti-calcolo --all` |
| [ritenuta-acconto](skills/ritenuta-acconto/SKILL.md) | Ritenute: chi trattiene e chi no | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill ritenuta-acconto --all` |
| [operazioni-estero](skills/operazioni-estero/SKILL.md) | Estero IVA e Intrastat base | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill operazioni-estero --all` |
| [fattura-pa](skills/fattura-pa/SKILL.md) | Fatture PA con CIG/CUP | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill fattura-pa --all` |
| [imu-calcolo](skills/imu-calcolo/SKILL.md) | IMU con base e aliquota | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill imu-calcolo --all` |
| [cu-730-guida](skills/cu-730-guida/SKILL.md) | CU e 730 per dipendenti e freelance | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill cu-730-guida --all` |
| [busta-paga-leggi](skills/busta-paga-leggi/SKILL.md) | Buste paga riga per riga | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill busta-paga-leggi --all` |
| [naspi-guida](skills/naspi-guida/SKILL.md) | NASpI: requisiti e calcolo | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill naspi-guida --all` |
| [isee-guida](skills/isee-guida/SKILL.md) | ISEE con DSU senza errori | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill isee-guida --all` |
| [bollette-energia](skills/bollette-energia/SKILL.md) | Bollette luce/gas e confronti | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill bollette-energia --all` |
| [bonus-casa](skills/bonus-casa/SKILL.md) | Bonus casa con carte in regola | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill bonus-casa --all` |
| [sanita-digitale](skills/sanita-digitale/SKILL.md) | FSE, IO, CUP e tessera | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill sanita-digitale --all` |
| [affitto-check](skills/affitto-check/SKILL.md) | Contratti affitto con red flag | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill affitto-check --all` |
| [pagopa-guida](skills/pagopa-guida/SKILL.md) | pagoPA con ricevute che provano | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill pagopa-guida --all` |
| [garanzie-consumo](skills/garanzie-consumo/SKILL.md) | Garanzia 2 anni e oneri | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill garanzie-consumo --all` |
| [recesso-acquisti](skills/recesso-acquisti/SKILL.md) | Recesso 14 giorni e eccezioni | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill recesso-acquisti --all` |
| [isa-check](skills/isa-check/SKILL.md) | Punteggi ISA letti bene | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill isa-check --all` |
| [tirocinio-guida](skills/tirocinio-guida/SKILL.md) | Stage con diritti e indennità | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill tirocinio-guida --all` |
| [nota-credito](skills/nota-credito/SKILL.md) | Note di credito via SdI | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill nota-credito --all` |
| [contributi-inps](skills/contributi-inps/SKILL.md) | Contributi per gestione e minimali | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill contributi-inps --all` |
| [agevolazioni-assunzioni](skills/agevolazioni-assunzioni/SKILL.md) | Sgravi assunzioni con requisiti | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill agevolazioni-assunzioni --all` |
| [ditta-vs-srl](skills/ditta-vs-srl/SKILL.md) | Forme giuridiche a confronto | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill ditta-vs-srl --all` |
| [camera-commercio](skills/camera-commercio/SKILL.md) | Pratiche registro imprese | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill camera-commercio --all` |
| [durc](skills/durc/SKILL.md) | DURC: validità e controlli | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill durc --all` |
| [maternita-congedi](skills/maternita-congedi/SKILL.md) | Maternità e parentali INPS | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill maternita-congedi --all` |
| [malattia-certificato](skills/malattia-certificato/SKILL.md) | Malattia e reperibilità | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill malattia-certificato --all` |
| [apprendistato](skills/apprendistato/SKILL.md) | Apprendistato con tutele | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill apprendistato --all` |
| [contratto-tipi](skills/contratto-tipi/SKILL.md) | Tipi di contratto a confronto | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill contratto-tipi --all` |
| [condominio-spese](skills/condominio-spese/SKILL.md) | Spese condominiali e millesimi | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill condominio-spese --all` |
| [mutuo-tassi](skills/mutuo-tassi/SKILL.md) | Mutui con TAN/TAEG veri | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill mutuo-tassi --all` |
| [compravendita-casa](skills/compravendita-casa/SKILL.md) | Comprare casa senza disastri | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill compravendita-casa --all` |
| [auto-bollo](skills/auto-bollo/SKILL.md) | Bollo auto regionale | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill auto-bollo --all` |
| [assegno-unico](skills/assegno-unico/SKILL.md) | Assegno unico con fasce ISEE | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill assegno-unico --all` |
| [anagrafe-certificati](skills/anagrafe-certificati/SKILL.md) | Certificati ANPR online | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill anagrafe-certificati --all` |
| [passaporto-procedura](skills/passaporto-procedura/SKILL.md) | Passaporto senza doppi viaggi | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill passaporto-procedura --all` |
| [voli-ritardi](skills/voli-ritardi/SKILL.md) | EU261 con fasce e lettere | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill voli-ritardi --all` |
| [banche-reclami](skills/banche-reclami/SKILL.md) | Reclami banca + ABF | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill banche-reclami --all` |
| [vacanze-pacchetto](skills/vacanze-pacchetto/SKILL.md) | Pacchetti viaggio protetti | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill vacanze-pacchetto --all` |
| [tari-tassa](skills/tari-tassa/SKILL.md) | TARI con base e riduzioni | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill tari-tassa --all` |
| [canone-rai](skills/canone-rai/SKILL.md) | Canone TV con esenzioni | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill canone-rai --all` |
| [successioni-info](skills/successioni-info/SKILL.md) | Successioni con franchigie | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill successioni-info --all` |
| [donazioni-info](skills/donazioni-info/SKILL.md) | Donazioni con atto notarile | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill donazioni-info --all` |
| [patente-punti](skills/patente-punti/SKILL.md) | Punti patente e recuperi | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill patente-punti --all` |
| [periodo-prova](skills/periodo-prova/SKILL.md) | Periodi di prova e uscite | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill periodo-prova --all` |
| [licenziamento-info](skills/licenziamento-info/SKILL.md) | Licenziamenti e termini | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill licenziamento-info --all` |
| [smart-working](skills/smart-working/SKILL.md) | Lavoro agile con accordo | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill smart-working --all` |
| [part-time](skills/part-time/SKILL.md) | Part-time e conversioni | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill part-time --all` |
| [utenze-voltura](skills/utenze-voltura/SKILL.md) | Volture e subentri | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill utenze-voltura --all` |
| [affitto-breve](skills/affitto-breve/SKILL.md) | Affitti brevi e CIN | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill affitto-breve --all` |
| [compravendita-auto](skills/compravendita-auto/SKILL.md) | Auto usate senza sorprese | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill compravendita-auto --all` |
| [scuola-iscrizioni](skills/scuola-iscrizioni/SKILL.md) | Iscrizioni scolastiche | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill scuola-iscrizioni --all` |
| [universita-tasse](skills/universita-tasse/SKILL.md) | Tasse universitarie e aiuti | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill universita-tasse --all` |
| [medico-base](skills/medico-base/SKILL.md) | Medico di base e cambi | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill medico-base --all` |
| [ticket-esenzioni](skills/ticket-esenzioni/SKILL.md) | Esenzioni ticket sanitarie | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill ticket-esenzioni --all` |
| [invalidita-104](skills/invalidita-104/SKILL.md) | Invalidità e 104 con patronato | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill invalidita-104 --all` |
| [residenza-cambio](skills/residenza-cambio/SKILL.md) | Cambi residenza e effetti | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill residenza-cambio --all` |
| [carta-identita-cie](skills/carta-identita-cie/SKILL.md) | CIE senza doppi viaggi | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill carta-identita-cie --all` |
| [permesso-soggiorno](skills/permesso-soggiorno/SKILL.md) | Permessi con kit e rinnovi | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill permesso-soggiorno --all` |

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
  skills/                    # SOURCE OF TRUTH: 87 skill (9 + batch 1-IT 18 + batch 2-IT 20 + batch 3-IT 20 + batch 4-IT 20)
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
    batch2-IT fisco2: partita-iva-apri/ ateco-scelta/ acconti-calcolo/
      ritenuta-acconto/ operazioni-estero/ fattura-pa/ imu-calcolo/ cu-730-guida/
    batch2-IT lavoro2/casa: busta-paga-leggi/ naspi-guida/ isee-guida/
      bollette-energia/ bonus-casa/ sanita-digitale/ affitto-check/
    batch2-IT PA/tutele: pagopa-guida/ garanzie-consumo/ recesso-acquisti/
      isa-check/ tirocinio-guida/
    batch3-IT fisco/impresa: nota-credito/ contributi-inps/ agevolazioni-assunzioni/
      ditta-vs-srl/ camera-commercio/ durc/
    batch3-IT lavoro: maternita-congedi/ malattia-certificato/
      apprendistato/ contratto-tipi/
    batch3-IT casa: condominio-spese/ mutuo-tassi/ compravendita-casa/
      auto-bollo/ assegno-unico/
    batch3-IT PA/tutele: anagrafe-certificati/ passaporto-procedura/
      voli-ritardi/ banche-reclami/ vacanze-pacchetto/
    batch4-IT fisco/famiglia: tari-tassa/ canone-rai/ successioni-info/ donazioni-info/
    batch4-IT lavoro/casa: periodo-prova/ licenziamento-info/ smart-working/
      part-time/ utenze-voltura/ affitto-breve/ compravendita-auto/
    batch4-IT scuola/salute: scuola-iscrizioni/ universita-tasse/ medico-base/
      ticket-esenzioni/ invalidita-104/
    batch4-IT PA/documenti: residenza-cambio/ carta-identita-cie/
      patente-punti/ permesso-soggiorno/
    (ognuna: SKILL.md + references/ + examples/)
  archive/                   # skill generiche pre-restart (non installate)
    batch1-generic/ (17) + batch2-seo/ (18)
  templates/skill-starter/   # modello per nuove skill
  catalog/                   # skills.json + vendors-manifest.json + _registry.md
  .agents/skills/README.md   # standard Codex/Cursor/Copilot
  .claude/README.md          # adapter Claude Code (+ .claude-plugin/plugin.json)
  .grok/README.md            # adapter Grok Code
  .github/skills/README.md   # adapter Copilot + Copilot CLI
  .opencode/skills/README.md # adapter OpenCode
  .windsurf/skills/README.md # adapter Windsurf (invocazione @nome)
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

## Roadmap (repo GitHub privata, sviluppo per batch)

- [x] Restart Italia 1.0 (9 skill + archivio 35 generiche)
- [x] Batch 1-IT (18 skill: fisco, formali, lavoro, bandi/PA) → totale 27
- [x] Batch 2-IT (20 skill: fisco 2, lavoro 2, casa, PA, tutele) → totale 47
- [x] 9 agenti (claude, codex, grok, cursor, copilot, copilot-cli, gemini, opencode, windsurf)
- [x] CI gates su repo privata (validate + security + install dry-run)
- [x] Batch 3-IT (20 skill: fisco/impresa, lavoro, casa, PA/tutele) → totale 67
- [x] Batch 4-IT (20 skill: fisco/famiglia, lavoro, casa/auto, scuola/salute, PA) → totale 87
- [ ] Rinviati da valutare: contratto-base-check, ferie-permessi
- [ ] Test reali sugli agenti e badge in `docs/COMPATIBILITY.md`
- [ ] Batch 4-IT da pianificare (vedi `catalog/_registry.md`)
- [ ] Rinviato (serve repo pubblica): submit a skills.sh / agentskills.io
