#!/usr/bin/env python3
"""Build docs/CATALOG.md from catalog/skills.json grouped by theme.

Usage:
  python scripts/build-catalog.py
  python scripts/build-catalog.py --check   # exit 2 if any skill unclassified

NEVER edit docs/CATALOG.md by hand: regenerate it.
"""
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
CATALOG = REPO / "catalog" / "skills.json"
OUT = REPO / "docs" / "CATALOG.md"

# Ordered (theme, keywords): first match wins. Match on name + description, lowercase.
THEMES = [
    ("Tooling", ["hello-agent", "skill-creator"]),
    ("Scrittura e contenuti", ["doc-polish", "translate", "press-release", "lettera-presentazione"]),
    ("Fisco e tasse", ["fisco", "fattura", "forfettario", "iva", "irpef", "imu", "tari",
                        "cedolare", "acconto", "ritenuta", "ravvedimento", "cartelle",
                        "rateizz", "compensazioni", "rimborso", "accertamento", "acconti",
                        "esterometro", "operazioni-estero", "plusvalenza", "ivafe",
                        "addizionali", "imposta-bollo", "nota-credito", "contribut", "corrispettivi",
                        "scadenze-fiscali", "cu-730", "dichiarazione-integrativa",
                        "isa-check", "tassazione", "invoice", "ateco", "canone-rai",
                        "rimborsi"]),
    ("Giustizia", ["giudice", "conciliazione", "diffida", "mediazione", "multe-ricorso",
                   "abf", "reclamo banca", "banche-reclami"]),
    ("Successioni e donazioni", ["succession", "donazioni", "testamento", "eredita",
                                 "mantenimento-figli"]),
    ("Lavoro", ["lavoro", "licenziamento", "dimissioni", "colloquio", "cv-europass",
                "dis-coll", "naspi", "cassa-integrazione", "malattia", "maternita",
                "periodo-prova", "apprendistato", "tirocinio", "somministrazione",
                "colf", "collaborazioni-occasionali", "smart-working", "part-time",
                "straordinari", "reperibilita", "orario", "permessi-studio", "buoni-pasto",
                "trasfert", "distacco", "busta-paga", "tredicesima", "congedo-matrimoniale",
                "aspettativa", "infortuni", "festivi", "welfare", "trasferimento",
                "contratto"]),
    ("Impresa", ["impresa", "ditta", "srl", "startup", "franchising", "fallimento",
                 "camera-commercio", "durc", "bandi-pmi", "domanda-bando", "agenti-rappresentanti",
                 "appalti", "ecommerce", "cooperativa", "marchi", "sicurezza-lavoro",
                 "preventivo-it", "agevolazioni-assunzioni", "nota-spese", "case-study", "cooperative"]),
    ("Casa", ["casa", "affitto", "mutuo", "condominio", "bollette", "utenze",
              "riscaldamento", "ape-", "edilizia", "amministratore-condominio",
              "compravendita-casa", "prima-casa", "usufrutto", "comodato",
              "morosita", "lavori-straordinari", "assemblea-condominiale",
              "volture-catastali", "visura-leggimi", "plusvalenza-casa",
              "case-popolari"]),
    ("Famiglia", ["famiglia", "matrimonio", "cittadinanza", "unioni", "assegno-unico",
                  "nido", "mensa-scolastica", "cognome-figli", "adozioni", "separazione",
                  "isee", "bonus-cultura"]),
    ("Scuola e giovani", ["scuola", "universita", "erasmus", "its-academy", "dsa-bes",
                          "maturita", "servizio-civile", "tirocinio-guida"]),
    ("Salute", ["salute", "medico", "ticket", "invalidita", "sanita", "vaccini", "assistenza-anziani",
                "donazione-sangue", "donazione-organi", "farmaci", "ricetta",
                "guardia-medica", "pronto-soccorso", "impegnativa", "screening",
                "assicurazione-sanitaria", "spese-mediche", "intramoenia"]),
    ("Pensioni", ["pensione", "riscatto-laurea", "tfr-fondo", "reversibilita"]),
    ("PA e documenti", ["pec", "spid", "anagrafe", "residenza", "carta-identita",
                        "passaporto", "pagopa", "elezioni", "privacy", "inad",
                        "domicilio-digitale", "cassetto-fiscale", "firma-digitale",
                        "patronato", "concorsi", "certificati-estero", "aire",
                        "email-formale", "verbale-riunione", "permesso-soggiorno"]),
    ("Soldi e banche", ["soldi", "conto-corrente", "mutuo-tassi", "leasing", "budget", "xlsx", "assicurazione-vita",
                        "carte-revolving", "usura", "fondo-emergenza", "buoni-fruttiferi",
                        "conti-deposito", "conti-cointestati", "limite-contante",
                        "bonifici", "carta-prepagata", "sollecito-pagamento",
                        "credito", "finanziamento"]),
    ("Trasporti e viaggi", ["trasporti", "auto", "patente", "bollo-auto", "revisione-auto",
                            "ztl", "trasporto-disabili", "compravendita-auto", "rc-auto",
                            "noleggio-auto", "voli", "treni", "bagagli", "vacanze",
                            "animali-viaggi", "officina"]),
    ("Tutele e consumi", ["tutela", "garanzie", "recesso", "reclami", "telefonia", "assicurazione-viaggio",
                          "energia-reclami", "assicurazione-casa", "trasloco-diritti",
                          "abbonamenti-palestra", "consumo"]),
]

def classify(name, desc):
    overrides = {
        "affitto-breve": "Casa",
        "aspettativa-lavoro": "Lavoro",
        "assicurazione-sanitaria": "Salute",
        "colf-badanti": "Lavoro",
        "universita-tasse": "Scuola e giovani",
        "farmaci-equivalenti": "Salute",
        "impegnativa-visite": "Salute",
        "privacy-informativa": "PA e documenti",
        "spese-notarili": "Casa",
        "startup-innovativa": "Impresa",
        "testamento-pubblico": "Successioni e donazioni",
        "pignoramento-conto": "Soldi e banche",
        "lavori-straordinari": "Casa",
        "sicurezza-lavoro": "Impresa",
        "affido-familiare": "Famiglia",
        "assegni-bancari": "Soldi e banche",
        "assemblea-sindacale": "Lavoro",
        "fido-scoperto": "Soldi e banche",
        "irap-info": "Fisco e tasse",
        "libri-contabili": "Impresa",
        "multiproprieta-diritti": "Casa",
        "rsu-rls": "Lavoro",
        "servizi-cimiteriali-funebri": "Famiglia",
        "stagionali-turismo": "Lavoro",
        "whistleblowing-info": "Impresa",
        "sciopero-diritti": "Lavoro",
        "scuola-privata-paritaria": "Scuola e giovani",
        "revisione-auto": "Trasporti e viaggi",
        "ferie-permessi": "Lavoro",
        "percorso-apri-partita-iva": "Impresa",
        "percorso-assunzione-domestica": "Lavoro",
        "percorso-casa-compravendita": "Casa",
        "percorso-lutto": "Successioni e donazioni",
        "percorso-busta-controllo": "Lavoro",
    }
    if name in overrides:
        return overrides[name]
    hay = f"{name} {desc}".lower()
    for theme, keys in THEMES:
        if any(k in hay for k in keys):
            return theme
    return "Altro"

def main():
    check_only = "--check" in sys.argv
    data = json.loads(CATALOG.read_text(encoding="utf-8"))
    skills = data["skills"]
    grouped = {}
    unclassified = []
    for s in skills:
        origin = s.get("origin", "")
        if origin.startswith("vendor/"):
            theme = "Vendor · " + origin.split("/", 1)[1]
        else:
            theme = classify(s["name"], s.get("description", ""))
        if theme == "Altro":
            unclassified.append(s["name"])
        grouped.setdefault(theme, []).append(s)
    if unclassified:
        print("UNCLASSIFIED:", ", ".join(sorted(unclassified)))
        if check_only:
            return 2
    if check_only:
        print(f"OK: {len(skills)} skills classified, {len(grouped)} themes.")
        return 0
    lines = ["# Catalogo skill per temi",
             "",
             "> Generato da `catalog/skills.json` con `python scripts/build-catalog.py`.",
             "> Non modificare a mano.",
             ""]
    theme_order = [t for t, _ in THEMES]
    theme_order += ["Vendor · anthropics-skills", "Vendor · mattpocock-skills", "Vendor · superpowers"]
    for theme in theme_order:
        items = grouped.get(theme, [])
        if not items:
            continue
        anchor = theme.lower().replace(" ", "-").replace("è", "e").replace("é", "e").replace("·", "").replace("--", "-").strip("-")
        lines.append(f"## {theme} ({len(items)})")
        lines.append("")
        for s in sorted(items, key=lambda x: x["name"]):
            lic = s.get("license", "MIT")
            suffix = f" ({lic})" if lic != "MIT" else ""
            lines.append(f"- [{s['name']}](../{s['path']}) — {s.get('description', '')}{suffix}")
        lines.append("")
    if unclassified:
        lines.append("## Altro (da classificare)")
        lines.append("")
        for n in sorted(unclassified):
            lines.append(f"- {n}")
        lines.append("")
    OUT.write_text("\n".join(lines), encoding="utf-8")
    total = sum(len(v) for v in grouped.values())
    print(f"Wrote {OUT.relative_to(REPO)}: {total} skills in {len(grouped)} themes.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
