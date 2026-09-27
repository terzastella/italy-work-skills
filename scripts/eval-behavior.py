#!/usr/bin/env python3
"""Behavior guards for Golden + delicate skills (superpowers-1 block).

Deterministic static checks, no LLM, no network. Exit 2 on any failure.
CI runs this alongside eval-golden.py.

- Golden (136: run protocol present (input.md + expect.md, non-trivial),
  >=1 out-link in SKILL.md, Good+Bad examples, year markers where required.
- Delicate (36, mirror of docs/AUDITS.md): no scripts/ dir, referral marker
  present, banned verdict patterns (tests/patterns-ban.txt) never affirmative.

Usage:
  python scripts/eval-behavior.py
"""
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SKILLS = REPO / "skills"
TESTS = REPO / "tests" / "golden"

GOLDEN = ["imu-calcolo", "irpef-scaglioni", "acconti-calcolo", "regime-forfettario",
          "invoice-it", "busta-paga-leggi", "ferie-permessi", "tfr-fondo",
          "assegno-unico", "xlsx-budget-it", "scadenze-fiscali", "naspi-guida",
          "email-formale-it", "pec-bozza", "cv-europass", "bandi-pmi",
          "colf-badanti", "partita-iva-apri", "isee-guida", "hello-agent",
          "fattura-elettronica-it", "ritenuta-acconto", "cedolare-secca",
          "tredicesima-info", "riscatto-laurea", "contratto-tipi",
          "periodo-prova", "dimissioni-procedura", "malattia-certificato",
          "apprendistato", "conto-corrente-costi", "tari-tassa",
          "bollette-energia", "spid-cie-guida", "domanda-bando",
          "maternita-congedi", "pensione-guida", "successioni-info",
          "donazioni-info", "testamento-olografo",
          "ravvedimento-operoso", "compensazioni-f24", "spese-mediche-detrazioni",
          "plusvalenza-casa", "rateizzazione-debiti", "dichiarazione-integrativa",
          "straordinari-info", "collaborazioni-occasionali", "orario-riposi",
          "congedo-matrimoniale", "condominio-spese", "mutuo-tassi",
          "conti-deposito", "carte-revolving", "buoni-fruttiferi",
          "riscaldamento-contabilizzazione", "voli-ritardi",
          "conciliazione-paritetica", "affitto-concordato", "universita-tasse",
          "contributi-inps", "imposta-bollo", "rimborsi-fiscali", "ivafe-ivie",
          "addizionali-regionali", "cassa-integrazione", "lavoro-notturno",
          "festivi-lavorati", "somministrazione", "usura-tassi",
          "prima-casa-agevolazioni", "spese-notarili", "usufrutto-nuda",
          "affitto-breve", "utenze-voltura", "asilo-nido-bonus",
          "scuola-iscrizioni", "ticket-esenzioni", "passaporto-procedura",
          "residenza-cambio",
          "nota-credito", "nota-spese", "fattura-pa", "camera-commercio",
          "startup-innovativa", "tirocinio-guida", "agenti-rappresentanti",
          "buoni-pasto", "distacco-lavoratore", "fido-scoperto",
          "assegni-bancari", "bonifici-istantanei", "banche-reclami",
          "morosita-condominiale", "assemblea-condominiale",
          "anagrafe-certificati", "carta-identita-cie", "garanzie-consumo",
          "recesso-acquisti", "treni-diritti",
          "ditta-vs-srl", "ecommerce-adempimenti", "ateco-scelta", "dis-coll",
          "agevolazioni-assunzioni", "lavori-straordinari", "sicurezza-lavoro",
          "preventivo-it", "sollecito-pagamento", "case-study",
          "trasloco-diritti",
          "bonus-casa", "canone-rai", "auto-bollo", "rc-auto",
          "compravendita-auto", "patente-punti", "revisione-auto",
          "ztl-permessi", "trasporto-disabili", "energia-reclami",
          "telefonia-reclami", "vacanze-pacchetto", "bagagli-smarriti",
          "erasmus-info", "universita-fuorisede", "dsa-bes-scuola",
          "sanita-digitale", "medico-base", "guardia-medica-turisti",
          "mensa-scolastica",
          "abbonamenti-palestra", "cognome-figli", "colloquio-prep-it",
          "doc-polish-it", "lettera-presentazione", "matrimonio-civile",
          "matrimonio-estero", "patronato-servizi", "press-release-it",
          "privacy-informativa", "pronto-soccorso-ticket", "ricetta-elettronica",
          "screening-prevenzione", "servizi-cimiteriali-funebri",
          "servizio-civile", "skill-creator-it", "translate-it-en",
          "universita-estero-laurea", "verbale-riunione-it",
          "accertamento-info", "adozioni-info", "affido-familiare",
          "appalti-pubblici-info", "assicurazione-vita-info", "cittadinanza",
          "contratto-base-check", "cooperative-info", "criptovalute-fisco",
          "eredita-debiti", "fallimento-crisi-info", "franchising-info",
          "giudice-di-pace", "invalidita-104", "irap-info",
          "licenziamento-info", "mantenimento-figli", "marchi-info",
          "mediazione-civile", "multe-ricorso", "pensione-reversibilita",
          "permesso-soggiorno", "pignoramento-conto", "salute-mentale-info",
          "separazione-divorzio", "testamento-biologico-dat",
          "testamento-pubblico", "unioni-convivenze", "vaccini-obbligatori",
          "whistleblowing-info",
          "fondo-emergenza", "plusvalenza-finanziaria", "leasing-finanziamento",
          "affitto-check", "compravendita-casa", "fattura-proforma",
          "libri-contabili", "isa-check", "part-time", "permessi-studio-150",
          "lavoro-spettacolo", "trasferte-lavoro", "reperibilita-lavoro",
          "sciopero-diritti", "assemblea-sindacale", "rsu-rls",
          "videosorveglianza-lavoro", "stagionali-turismo", "smart-working",
          "aspettativa-lavoro",
          "amministratore-condominio", "volture-catastali",
          "trasferimento-sede", "trasferta-estero", "infortuni-lavoro",
          "concorsi-pubblici", "welfare-aziendale", "multiproprieta-diritti",
          "officina-diritti", "noleggio-auto-diritti", "carta-prepagata",
          "conti-cointestati", "bonus-cultura-18app", "scuola-privata-paritaria",
          "animali-viaggi", "aire-estero", "certificati-estero",
          "elezioni-voto", "assistenza-anziani", "cure-termali",
          "ape-certificazione", "assicurazione-casa", "assicurazione-sanitaria",
          "assicurazione-viaggio", "case-popolari-erp", "comodato-uso",
          "diffida-legale", "domicilio-digitale-inad", "donazione-organi",
          "donazione-sangue", "edilizia-cila-scia", "esami-intramoenia",
          "farmaci-equivalenti", "farmaci-estero", "firma-digitale",
          "impegnativa-visite", "its-academy", "lavoro-minorile",
          "maturita-esame", "pagopa-guida"]

PERCORSI = ["percorso-apri-partita-iva", "percorso-assunzione-domestica",
            "percorso-casa-compravendita", "percorso-lutto",
            "percorso-busta-controllo"]

GUIDED = GOLDEN + PERCORSI

YEAR_REQUIRED = set(GUIDED) - {"hello-agent", "email-formale-it", "pec-bozza", "cv-europass"}
LINK_REQUIRED = set(GUIDED) - {"hello-agent"}
GOODBAD_REQUIRED = set(GUIDED) - {"hello-agent"}

DELICATE = ["accertamento-info", "adozioni-info", "affido-familiare",
            "appalti-pubblici-info", "assicurazione-vita-info", "cittadinanza",
            "contratto-base-check", "contratto-tipi", "cooperative-info",
            "criptovalute-fisco", "donazioni-info", "eredita-debiti",
            "fallimento-crisi-info", "franchising-info", "giudice-di-pace",
            "invalidita-104", "irap-info", "licenziamento-info",
            "mantenimento-figli", "marchi-info", "maternita-congedi",
            "mediazione-civile", "multe-ricorso", "pensione-guida",
            "pensione-reversibilita", "permesso-soggiorno", "pignoramento-conto",
            "salute-mentale-info", "separazione-divorzio", "successioni-info",
            "testamento-biologico-dat", "testamento-olografo", "testamento-pubblico",
            "unioni-convivenze", "vaccini-obbligatori", "whistleblowing-info"]

REFERRAL = re.compile(r"rinvio|referral|patronato|notai|commercialista|avvocato|lawyer|accountant|notary|118|caf\b|medico|doctor|tribunal|inps", re.I)
YEAR = re.compile(r"20\d\d|year-stated|YEAR")
OUTLINK = re.compile(r"see `", re.I)

fails = []


def fail(msg):
    fails.append(msg)
    print(f"[FAIL] {msg}")


def read_skill(name):
    d = SKILLS / name
    texts = [(d / "SKILL.md").read_text(encoding="utf-8")]
    if (d / "references").is_dir():
        texts += [p.read_text(encoding="utf-8") for p in sorted((d / "references").glob("*")) if p.is_file()]
    return d, "\n".join(texts)


def main():
    # --- Golden + percorsi protocols + static guards ---
    for name in GUIDED:
        proto = (TESTS / name) if name in GOLDEN else (REPO / "tests" / "percorsi" / name)
        for f, minimum in (("input.md", 2), ("expect.md", 3)):
            p = proto / f
            if not p.exists():
                fail(f"{name}: missing tests/golden/{name}/{f}")
            elif len([ln for ln in p.read_text(encoding="utf-8").splitlines() if ln.strip()]) < minimum:
                fail(f"{name}: tests/golden/{name}/{f} too thin")
        d, text = read_skill(name)
        if name in LINK_REQUIRED and not OUTLINK.search((d / "SKILL.md").read_text(encoding="utf-8")):
            fail(f"{name}: SKILL.md has no out-link (see `...`)")
        if name in GOODBAD_REQUIRED:
            ex = ""
            if (d / "examples").is_dir():
                ex = "\n".join(p.read_text(encoding="utf-8") for p in (d / "examples").glob("*-cases.md"))
            if "## Good" not in ex or "## Bad" not in ex:
                fail(f"{name}: examples lack Good/Bad cases")
        if name in YEAR_REQUIRED and not YEAR.search(text):
            fail(f"{name}: no year marker (YYYY or year-stated) in SKILL.md+references")

    # --- Delicate guards ---
    for name in DELICATE:
        d, text = read_skill(name)
        if (d / "scripts").is_dir():
            fail(f"{name}: delicate skill must NEVER ship scripts/")
        if not REFERRAL.search(text):
            fail(f"{name}: no referral marker (patronato/notary/lawyer/118/...)")

    # --- Banned verdict patterns (affirmative use only) ---
    ban_text = (REPO / "tests" / "patterns-ban.txt").read_text(encoding="utf-8")
    patterns = [ln.strip() for ln in ban_text.splitlines()
                if ln.strip() and not ln.strip().startswith("#")
                and not ln.strip().startswith("Patterns:")
                and not ln.strip().startswith("Allow-list")]
    neg = re.compile(r"never|no |non |mai |rifiut|refus|not an|not a", re.I)
    for name in DELICATE:
        d, text = read_skill(name)
        for pat in patterns:
            for m in re.finditer(pat, text, re.I | re.S):
                line = text[max(0, m.start() - 120):m.end() + 120].splitlines()
                ctx = " ".join(line)
                if not neg.search(ctx):
                    fail(f"{name}: banned pattern affirmative: {pat!r} (...)")

    print(f"behavior: {'FAIL' if fails else 'OK'} ({len(GUIDED)} guided, {len(DELICATE)} delicate)")
    return 2 if fails else 0


if __name__ == "__main__":
    raise SystemExit(main())
