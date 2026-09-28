#!/usr/bin/env python3
"""Report references/ files missing last-verified or older than 12 months.

Usage:
  python scripts/check-freshness.py           # report only, exit 0
  python scripts/check-freshness.py --stamp <skill>...  # stamp + version bump

Advisory only (see docs/FRESHNESS.md). Rolled out: pilot trio + tax cluster;
full rollout is theme by theme.
"""
import datetime as dt
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
PAT = re.compile(r"^last-verified:\s*(\d{4})-(\d{2})-(\d{2})", re.M)
STALE_DAYS = 365
PILOT = {"invoice-it", "imu-calcolo", "regime-forfettario"}
TAX = {"accertamento-info", "acconti-calcolo", "addizionali-regionali",
       "ateco-scelta", "canone-rai", "cartelle-ader", "cedolare-secca",
       "compensazioni-f24", "contributi-inps", "corrispettivi-it",
       "criptovalute-fisco", "cu-730-guida", "dichiarazione-integrativa",
       "fattura-elettronica-it", "fattura-pa", "fattura-proforma",
       "imposta-bollo", "irap-info", "irpef-scaglioni", "isa-check",
       "ivafe-ivie", "nota-credito", "operazioni-estero", "partita-iva-apri",
       "plusvalenza-casa", "plusvalenza-finanziaria", "rateizzazione-debiti",
       "ravvedimento-operoso", "rimborsi-fiscali", "ritenuta-acconto",
       "scadenze-fiscali", "tari-tassa"}
ROLLED = PILOT | TAX
LAVORO = {"apprendistato", "aspettativa-lavoro", "assemblea-sindacale",
          "buoni-pasto", "busta-paga-leggi", "cassa-integrazione",
          "colf-badanti", "collaborazioni-occasionali", "colloquio-prep-it",
          "congedo-matrimoniale", "contratto-base-check", "contratto-tipi",
          "cv-europass", "dimissioni-procedura", "dis-coll",
          "distacco-lavoratore", "ferie-permessi", "festivi-lavorati",
          "infortuni-lavoro", "lavoro-minorile", "lavoro-notturno",
          "lavoro-spettacolo", "licenziamento-info", "malattia-certificato",
          "maternita-congedi", "naspi-guida", "orario-riposi", "part-time",
          "percorso-assunzione-domestica", "percorso-busta-controllo",
          "periodo-prova", "permessi-studio-150", "reperibilita-lavoro",
          "rsu-rls", "sciopero-diritti", "smart-working", "somministrazione",
          "stagionali-turismo", "straordinari-info", "tirocinio-guida",
          "trasferimento-sede", "trasferta-estero", "trasferte-lavoro",
          "tredicesima-info", "videosorveglianza-lavoro", "welfare-aziendale"}
SALUTE = {"assicurazione-sanitaria", "assistenza-anziani", "cure-termali",
          "donazione-organi", "donazione-sangue", "esami-intramoenia",
          "farmaci-equivalenti", "farmaci-estero", "guardia-medica-turisti",
          "impegnativa-visite", "invalidita-104", "medico-base",
          "pronto-soccorso-ticket", "ricetta-elettronica",
          "salute-mentale-info", "sanita-digitale", "screening-prevenzione",
          "spese-mediche-detrazioni", "ticket-esenzioni", "vaccini-obbligatori"}
ROLLED = PILOT | TAX | LAVORO | SALUTE
STAMP = "last-verified: 2026-09-28"


def bump_version(skill_dir):
    p = skill_dir / "SKILL.md"
    txt = p.read_text(encoding="utf-8")
    m = re.search(r'version: "0\.(\d+)"', txt)
    if not m:
        print(f"[STAMP-SKIP] {skill_dir.name}: no 0.x version found")
        return False
    txt = txt[:m.start(1)] + str(int(m.group(1)) + 1) + txt[m.end(1):]
    p.write_text(txt, encoding="utf-8")
    return True


def stamp(skills):
    for name in skills:
        d = REPO / "skills" / name
        refs = sorted((d / "references").glob("*.md")) if (d / "references").is_dir() else []
        if not refs:
            print(f"[STAMP-SKIP] {name}: no references/")
            continue
        for ref in refs:
            lines = ref.read_text(encoding="utf-8").splitlines()
            if any(l.startswith("last-verified:") for l in lines[:4]):
                continue
            ref.write_text("\n".join([lines[0], "", STAMP] + lines[1:]) + "\n", encoding="utf-8")
        bump_version(d)
        print(f"[STAMPED] {name} ({len(refs)} refs)")


def main():
    if "--stamp" in sys.argv:
        stamp([a for a in sys.argv[2:] if not a.startswith("--")])
        return 0
    check = "--check" in sys.argv
    today = dt.date.today()
    missing, stale = [], []
    for ref in sorted((REPO / "skills").glob("*/references/*.md")):
        skill = ref.parts[-3]
        m = PAT.search(ref.read_text(encoding="utf-8"))
        if not m:
            if skill in ROLLED:
                missing.append(f"{skill}/{ref.name}")
            continue
        try:
            seen = dt.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
        except ValueError:
            missing.append(f"{skill}/{ref.name} (bad date)")
            continue
        if (today - seen).days > STALE_DAYS:
            stale.append(f"{skill}/{ref.name} ({m.group(0).split(': ', 1)[1]})")
    for m in missing:
        print(f"[MISSING] {m}")
    for s in stale:
        print(f"[STALE] {s}")
    pilot_refs = sum(1 for _ in (REPO / "skills").glob("*/references/*.md")
                     if _.parts[-3] in ROLLED)
    print(f"freshness: {len(missing)} missing, {len(stale)} stale "
          f"(rolled out: {len(ROLLED)} skills, {pilot_refs} refs)")
    if check and (missing or stale):
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
