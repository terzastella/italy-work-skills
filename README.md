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
| [colf-badanti](skills/colf-badanti/SKILL.md) | Colf e badanti con livelli | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill colf-badanti --all` |
| [collaborazioni-occasionali](skills/collaborazioni-occasionali/SKILL.md) | Occasionali con limiti | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill collaborazioni-occasionali --all` |
| [pensione-guida](skills/pensione-guida/SKILL.md) | Pensioni: percorsi e finestre | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill pensione-guida --all` |
| [riscatto-laurea](skills/riscatto-laurea/SKILL.md) | Riscatto laurea e convenienza | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill riscatto-laurea --all` |
| [tfr-fondo](skills/tfr-fondo/SKILL.md) | TFR in azienda o fondi | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill tfr-fondo --all` |
| [prima-casa-agevolazioni](skills/prima-casa-agevolazioni/SKILL.md) | Prima casa e residenza | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill prima-casa-agevolazioni --all` |
| [affitto-concordato](skills/affitto-concordato/SKILL.md) | Canone concordato e sconti | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill affitto-concordato --all` |
| [conto-corrente-costi](skills/conto-corrente-costi/SKILL.md) | Costi conto e ISC | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill conto-corrente-costi --all` |
| [rc-auto](skills/rc-auto/SKILL.md) | RC auto e sinistri | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill rc-auto --all` |
| [criptovalute-fisco](skills/criptovalute-fisco/SKILL.md) | Cripto e fisco senza miti | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill criptovalute-fisco --all` |
| [spese-mediche-detrazioni](skills/spese-mediche-detrazioni/SKILL.md) | Spese mediche al 19% | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill spese-mediche-detrazioni --all` |
| [unioni-convivenze](skills/unioni-convivenze/SKILL.md) | Unioni e convivenze | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill unioni-convivenze --all` |
| [asilo-nido-bonus](skills/asilo-nido-bonus/SKILL.md) | Bonus nido e fasce | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill asilo-nido-bonus --all` |
| [testamento-olografo](skills/testamento-olografo/SKILL.md) | Testamento con requisiti | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill testamento-olografo --all` |
| [aire-estero](skills/aire-estero/SKILL.md) | AIRE e voto estero | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill aire-estero --all` |
| [certificati-estero](skills/certificati-estero/SKILL.md) | Apostille e legalizzazioni | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill certificati-estero --all` |
| [telefonia-reclami](skills/telefonia-reclami/SKILL.md) | Reclami e conciliaweb | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill telefonia-reclami --all` |
| [energia-reclami](skills/energia-reclami/SKILL.md) | Reclami e sportello ARERA | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill energia-reclami --all` |
| [assicurazione-casa](skills/assicurazione-casa/SKILL.md) | Polizze casa e sinistri | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill assicurazione-casa --all` |
| [animali-viaggi](skills/animali-viaggi/SKILL.md) | Animali oltre confine | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill animali-viaggi --all` |
| [ravvedimento-operoso](skills/ravvedimento-operoso/SKILL.md) | Ravvedimento con fasce | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill ravvedimento-operoso --all` |
| [cartelle-ader](skills/cartelle-ader/SKILL.md) | Cartelle con 60 giorni | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill cartelle-ader --all` |
| [rateizzazione-debiti](skills/rateizzazione-debiti/SKILL.md) | Rateizzi senza perderli | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill rateizzazione-debiti --all` |
| [cedolare-secca](skills/cedolare-secca/SKILL.md) | Cedolare vs IRPEF | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill cedolare-secca --all` |
| [firma-digitale](skills/firma-digitale/SKILL.md) | Firme con tipi giusti | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill firma-digitale --all` |
| [cassa-integrazione](skills/cassa-integrazione/SKILL.md) | CIG e paga effetti | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill cassa-integrazione --all` |
| [welfare-aziendale](skills/welfare-aziendale/SKILL.md) | Fringe senza trappole | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill welfare-aziendale --all` |
| [ecommerce-adempimenti](skills/ecommerce-adempimenti/SKILL.md) | Vendere online in regola | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill ecommerce-adempimenti --all` |
| [sicurezza-lavoro](skills/sicurezza-lavoro/SKILL.md) | DVR e mappa doveri | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill sicurezza-lavoro --all` |
| [marchi-info](skills/marchi-info/SKILL.md) | Marchi e brevetti base | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill marchi-info --all` |
| [ape-certificazione](skills/ape-certificazione/SKILL.md) | APE e classi energetiche | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill ape-certificazione --all` |
| [edilizia-cila-scia](skills/edilizia-cila-scia/SKILL.md) | Permessi per lavori | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill edilizia-cila-scia --all` |
| [amministratore-condominio](skills/amministratore-condominio/SKILL.md) | Amministratori dentro/fuori | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill amministratore-condominio --all` |
| [domicilio-digitale-inad](skills/domicilio-digitale-inad/SKILL.md) | Domicilio INAD ed effetti | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill domicilio-digitale-inad --all` |
| [cassetto-fiscale](skills/cassetto-fiscale/SKILL.md) | Cassetto AdE e deleghe | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill cassetto-fiscale --all` |
| [elezioni-voto](skills/elezioni-voto/SKILL.md) | Votare senza sorprese | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill elezioni-voto --all` |
| [multe-ricorso](skills/multe-ricorso/SKILL.md) | Multe e ricorsi base | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill multe-ricorso --all` |
| [assicurazione-sanitaria](skills/assicurazione-sanitaria/SKILL.md) | Fondi sanitari e deducibilità | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill assicurazione-sanitaria --all` |
| [dis-coll](skills/dis-coll/SKILL.md) | DIS-COLL per collaboratori | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill dis-coll --all` |
| [pensione-reversibilita](skills/pensione-reversibilita/SKILL.md) | Reversibilità e limiti | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill pensione-reversibilita --all` |
| [accertamento-info](skills/accertamento-info/SKILL.md) | Accertamenti e adesione | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill accertamento-info --all` |
| [compensazioni-f24](skills/compensazioni-f24/SKILL.md) | Compensazioni con visti | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill compensazioni-f24 --all` |
| [rimborsi-fiscali](skills/rimborsi-fiscali/SKILL.md) | Rimborsi con tempi | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill rimborsi-fiscali --all` |
| [somministrazione](skills/somministrazione/SKILL.md) | Interinale e parità | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill somministrazione --all` |
| [lavoro-minorile](skills/lavoro-minorile/SKILL.md) | Minori al lavoro, tutele | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill lavoro-minorile --all` |
| [startup-innovativa](skills/startup-innovativa/SKILL.md) | Startup e registro | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill startup-innovativa --all` |
| [fallimento-crisi-info](skills/fallimento-crisi-info/SKILL.md) | Crisi con segnali | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill fallimento-crisi-info --all` |
| [franchising-info](skills/franchising-info/SKILL.md) | Affiliazioni e fee | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill franchising-info --all` |
| [usufrutto-nuda](skills/usufrutto-nuda/SKILL.md) | Usufrutto e nuda proprietà | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill usufrutto-nuda --all` |
| [spese-notarili](skills/spese-notarili/SKILL.md) | Preventivi notaio letti | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill spese-notarili --all` |
| [mantenimento-figli](skills/mantenimento-figli/SKILL.md) | Mantenimento senza cifre | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill mantenimento-figli --all` |
| [matrimonio-civile](skills/matrimonio-civile/SKILL.md) | Matrimoni e pubblicazioni | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill matrimonio-civile --all` |
| [cittadinanza](skills/cittadinanza/SKILL.md) | Cittadinanza e vie | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill cittadinanza --all` |
| [assistenza-anziani](skills/assistenza-anziani/SKILL.md) | Anziani e RSA | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill assistenza-anziani --all` |
| [bonus-cultura-18app](skills/bonus-cultura-18app/SKILL.md) | Bonus 18enni | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill bonus-cultura-18app --all` |
| [patronato-servizi](skills/patronato-servizi/SKILL.md) | Patronati gratis quando | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill patronato-servizi --all` |
| [concorsi-pubblici](skills/concorsi-pubblici/SKILL.md) | Concorsi e bandi | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill concorsi-pubblici --all` |
| [leasing-finanziamento](skills/leasing-finanziamento/SKILL.md) | Leasing o prestito | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill leasing-finanziamento --all` |
| [trasloco-diritti](skills/trasloco-diritti/SKILL.md) | Traslochi e danni | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill trasloco-diritti --all` |
| [riscaldamento-contabilizzazione](skills/riscaldamento-contabilizzazione/SKILL.md) | Riparti calore equi | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill riscaldamento-contabilizzazione --all` |
| [giudice-di-pace](skills/giudice-di-pace/SKILL.md) | Piccole cause e limiti | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill giudice-di-pace --all` |
| [conciliazione-paritetica](skills/conciliazione-paritetica/SKILL.md) | Conciliazioni con associazioni | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill conciliazione-paritetica --all` |
| [diffida-legale](skills/diffida-legale/SKILL.md) | Diffide senza minacce | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill diffida-legale --all` |
| [mediazione-civile](skills/mediazione-civile/SKILL.md) | Mediazioni obbligatorie | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill mediazione-civile --all` |
| [testamento-pubblico](skills/testamento-pubblico/SKILL.md) | Testamento dal notaio | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill testamento-pubblico --all` |
| [eredita-debiti](skills/eredita-debiti/SKILL.md) | Eredità con debiti | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill eredita-debiti --all` |
| [volture-catastali](skills/volture-catastali/SKILL.md) | Volture con tempi | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill volture-catastali --all` |
| [trasferta-estero](skills/trasferta-estero/SKILL.md) | Trasferte oltre confine | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill trasferta-estero --all` |
| [infortuni-lavoro](skills/infortuni-lavoro/SKILL.md) | Infortuni e INAIL | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill infortuni-lavoro --all` |
| [reperibilita-lavoro](skills/reperibilita-lavoro/SKILL.md) | Reperibilità e limiti | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill reperibilita-lavoro --all` |
| [revisione-auto](skills/revisione-auto/SKILL.md) | Revisioni in regola | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill revisione-auto --all` |
| [ztl-permessi](skills/ztl-permessi/SKILL.md) | ZTL e permessi | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill ztl-permessi --all` |
| [trasporto-disabili](skills/trasporto-disabili/SKILL.md) | Contrassegni e soste | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill trasporto-disabili --all` |
| [vaccini-obbligatori](skills/vaccini-obbligatori/SKILL.md) | Calendari vaccinali | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill vaccini-obbligatori --all` |
| [donazione-sangue](skills/donazione-sangue/SKILL.md) | Donare sangue e permessi | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill donazione-sangue --all` |
| [pronto-soccorso-ticket](skills/pronto-soccorso-ticket/SKILL.md) | Codici e ticket PS | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill pronto-soccorso-ticket --all` |
| [straordinari-info](skills/straordinari-info/SKILL.md) | Straordinari e banca ore | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill straordinari-info --all` |
| [conti-deposito](skills/conti-deposito/SKILL.md) | Depositi al netto | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill conti-deposito --all` |
| [fondo-emergenza](skills/fondo-emergenza/SKILL.md) | Fondi liquidi sicuri | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill fondo-emergenza --all` |
| [trasferte-lavoro](skills/trasferte-lavoro/SKILL.md) | Trasferte Italia e quote | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill trasferte-lavoro --all` |
| [irpef-scaglioni](skills/irpef-scaglioni/SKILL.md) | Scaglioni e medie vere | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill irpef-scaglioni --all` |
| [addizionali-regionali](skills/addizionali-regionali/SKILL.md) | Addizionali per residenza | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill addizionali-regionali --all` |
| [imposta-bollo](skills/imposta-bollo/SKILL.md) | Marche e virtuale | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill imposta-bollo --all` |
| [aspettativa-lavoro](skills/aspettativa-lavoro/SKILL.md) | Aspettative e buchi | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill aspettativa-lavoro --all` |
| [trasferimento-sede](skills/trasferimento-sede/SKILL.md) | Trasferimenti e rifiuti | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill trasferimento-sede --all` |
| [plusvalenza-casa](skills/plusvalenza-casa/SKILL.md) | Plusvalenze e 5 anni | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill plusvalenza-casa --all` |
| [case-popolari-erp](skills/case-popolari-erp/SKILL.md) | ERP e graduatorie | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill case-popolari-erp --all` |
| [agenti-rappresentanti](skills/agenti-rappresentanti/SKILL.md) | Enasarco e FIRR | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill agenti-rappresentanti --all` |
| [appalti-pubblici-info](skills/appalti-pubblici-info/SKILL.md) | Gare e MEPA | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill appalti-pubblici-info --all` |
| [congedo-matrimoniale](skills/congedo-matrimoniale/SKILL.md) | Congedi nozze | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill congedo-matrimoniale --all` |
| [mensa-scolastica](skills/mensa-scolastica/SKILL.md) | Mense e fasce ISEE | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill mensa-scolastica --all` |
| [impegnativa-visite](skills/impegnativa-visite/SKILL.md) | Classi e CUP | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill impegnativa-visite --all` |
| [donazione-organi](skills/donazione-organi/SKILL.md) | Volontà sobrie | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill donazione-organi --all` |
| [adozioni-info](skills/adozioni-info/SKILL.md) | Adozioni e tempi | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill adozioni-info --all` |
| [separazione-divorzio](skills/separazione-divorzio/SKILL.md) | Separazioni senza tattiche | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill separazione-divorzio --all` |
| [servizio-civile](skills/servizio-civile/SKILL.md) | Bandi e assegni | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill servizio-civile --all` |
| [tredicesima-info](skills/tredicesima-info/SKILL.md) | Tredicesime e ratei | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill tredicesima-info --all` |
| [buoni-fruttiferi](skills/buoni-fruttiferi/SKILL.md) | Buoni al netto | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill buoni-fruttiferi --all` |
| [treni-diritti](skills/treni-diritti/SKILL.md) | Ritardi e rimborsi | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill treni-diritti --all` |
| [noleggio-auto-diritti](skills/noleggio-auto-diritti/SKILL.md) | Noleggi e franchigie | ⚠️ | ⚠️ | ⚠️ | `python scripts/install.py --skill noleggio-auto-diritti --all` |

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
  skills/                    # SOURCE OF TRUTH: 187 skill (9 + batch 1-9 IT)
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
    batch5-IT lavoro/pensioni: colf-badanti/ collaborazioni-occasionali/
      pensione-guida/ riscatto-laurea/ tfr-fondo/
    batch5-IT casa/soldi: prima-casa-agevolazioni/ affitto-concordato/
      conto-corrente-costi/ rc-auto/ criptovalute-fisco/
    batch5-IT famiglia/estero: spese-mediche-detrazioni/ unioni-convivenze/
      asilo-nido-bonus/ testamento-olografo/ aire-estero/
    batch5-IT tutele: certificati-estero/ telefonia-reclami/ energia-reclami/
      assicurazione-casa/ animali-viaggi/
    batch6-IT fisco: ravvedimento-operoso/ cartelle-ader/ rateizzazione-debiti/
      cedolare-secca/ firma-digitale/
    batch6-IT lavoro/impresa: cassa-integrazione/ welfare-aziendale/
      ecommerce-adempimenti/ sicurezza-lavoro/ marchi-info/
    batch6-IT casa/digitali: ape-certificazione/ edilizia-cila-scia/
      amministratore-condominio/ domicilio-digitale-inad/ cassetto-fiscale/
    batch6-IT PA/salute: elezioni-voto/ multe-ricorso/ assicurazione-sanitaria/
      dis-coll/ pensione-reversibilita/
    batch7-IT fisco/lavoro: accertamento-info/ compensazioni-f24/ rimborsi-fiscali/
      somministrazione/ lavoro-minorile/
    batch7-IT impresa/casa: startup-innovativa/ fallimento-crisi-info/ franchising-info/
      usufrutto-nuda/ spese-notarili/
    batch7-IT famiglia/salute: mantenimento-figli/ matrimonio-civile/ cittadinanza/
      assistenza-anziani/ bonus-cultura-18app/
    batch7-IT PA/tutele: patronato-servizi/ concorsi-pubblici/ leasing-finanziamento/
      trasloco-diritti/ riscaldamento-contabilizzazione/
    batch8-IT giustizia/successioni: giudice-di-pace/ conciliazione-paritetica/
      diffida-legale/ mediazione-civile/ testamento-pubblico/
    batch8-IT eredità/lavoro: eredita-debiti/ volture-catastali/ trasferta-estero/
      infortuni-lavoro/ reperibilita-lavoro/
    batch8-IT trasporti/salute: revisione-auto/ ztl-permessi/ trasporto-disabili/
      vaccini-obbligatori/ donazione-sangue/
    batch8-IT soldi/lavoro: pronto-soccorso-ticket/ straordinari-info/ conti-deposito/
      fondo-emergenza/ trasferte-lavoro/
    batch9-IT fisco/lavoro: irpef-scaglioni/ addizionali-regionali/ imposta-bollo/
      aspettativa-lavoro/ trasferimento-sede/
    batch9-IT casa/impresa: plusvalenza-casa/ case-popolari-erp/ agenti-rappresentanti/
      appalti-pubblici-info/ congedo-matrimoniale/
    batch9-IT famiglia/salute: mensa-scolastica/ impegnativa-visite/ donazione-organi/
      adozioni-info/ separazione-divorzio/
    batch9-IT PA/soldi: servizio-civile/ tredicesima-info/ buoni-fruttiferi/
      treni-diritti/ noleggio-auto-diritti/
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
- [x] Batch 5-IT (20 skill: lavoro/pensioni, casa/soldi, famiglia/estero, tutele) → totale 107
- [x] Batch 6-IT (20 skill: fisco, lavoro/impresa, casa/digitali, PA/salute) → totale 127
- [x] Batch 7-IT (20 skill: fisco/lavoro, impresa/casa, famiglia/salute, PA/tutele) → totale 147
- [x] Batch 8-IT (20 skill: giustizia/successioni, eredità/lavoro, trasporti/salute, soldi/lavoro) → totale 167
- [x] Batch 9-IT (20 skill: fisco/lavoro, casa/impresa, famiglia/salute, PA/soldi) → totale 187
- [ ] Rinviati da valutare: contratto-base-check, ferie-permessi
- [ ] Test reali sugli agenti e badge in `docs/COMPATIBILITY.md`
- [ ] Batch 10-IT da pianificare (vedi `catalog/_registry.md`)
- [ ] Rinviato (serve repo pubblica): submit a skills.sh / agentskills.io
