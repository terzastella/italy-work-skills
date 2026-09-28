#!/usr/bin/env python3
"""Enforce last-verified freshness on SKILL.md + references/ (254/254).

Usage:
  python scripts/check-freshness.py           # report only, exit 0
  python scripts/check-freshness.py --check   # exit 2 if anything is stale/missing (CI-blocking)
  python scripts/check-freshness.py --stamp <skill>...  # stamp + version bump

See docs/FRESHNESS.md. STAMP dates always come from today (never hardcoded).
"""
import datetime as dt
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
PAT = re.compile(r"^last-verified:\s*(\d{4})-(\d{2})-(\d{2})", re.M)
SEM_PAT = re.compile(r"^## Sources \(verified (\d{4})-(\d{2})-(\d{2})\)", re.M)
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
CASA = set()  # filled below from theme batches; kept for history
# Full coverage: every skill with references/ or SKILL.md is checked.
# Theme sets above document the rollout order; enforcement is universal.
ALL_SKILLS = None


def rolled():
    global ALL_SKILLS
    if ALL_SKILLS is None:
        ALL_SKILLS = {p.name for p in (REPO / "skills").iterdir()
                      if p.is_dir() and (p / "SKILL.md").is_file()}
    return ALL_SKILLS


def today_stamp():
    return dt.date.today().isoformat()


STAMP = None  # computed per-run, never hardcoded (see stamp())
SKILL_STAMP = None
META_PAT = re.compile(r'metadata: \{([^}]*)\}', re.S)
SKILL_PAT = re.compile(r'last_verified: "(\d{4})-(\d{2})-(\d{2})"')


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


def ref_date(text):
    """(date, kind) from a references file. Semantic `## Sources` headers
    count exactly like `last-verified:` lines — one date per file, no duals."""
    m = PAT.search(text)
    if m:
        return (m.group(1), m.group(2), m.group(3)), "stamped"
    m = SEM_PAT.search(text)
    if m:
        return (m.group(1), m.group(2), m.group(3)), "semantic"
    return None, None


def stamp_skill_meta(skill_dir):
    """Insert or renew last_verified in SKILL.md metadata + bump version."""
    p = skill_dir / "SKILL.md"
    txt = p.read_text(encoding="utf-8")
    m = SKILL_PAT.search(txt)
    if m:
        txt = txt[:m.start()] + SKILL_STAMP + txt[m.end():]
    else:
        mm = META_PAT.search(txt)
        if not mm:
            print(f"[STAMP-SKIP] {skill_dir.name}: no metadata map found")
            return False
        inner = mm.group(1).rstrip()
        sep = "" if inner.endswith(",") or not inner else ", "
        txt = txt[:mm.start()] + "metadata: {" + inner + sep + SKILL_STAMP + "}" + txt[mm.end():]
    vm = re.search(r'version: "0\.(\d+)"', txt)
    if not vm:
        print(f"[STAMP-SKIP] {skill_dir.name}: no 0.x version found")
        return False
    txt = txt[:vm.start(1)] + str(int(vm.group(1)) + 1) + txt[vm.end(1):]
    p.write_text(txt, encoding="utf-8")
    return True


def stamp(skills):
    for name in skills:
        d = REPO / "skills" / name
        refs = sorted((d / "references").glob("*.md")) if (d / "references").is_dir() else []
        n_refs = 0
        for ref in refs:
            text = ref.read_text(encoding="utf-8")
            if SEM_PAT.search(text):
                continue  # semantic file: single date lives in its header
            lines = text.splitlines()
            idx = next((i for i, l in enumerate(lines[:4])
                        if l.startswith("last-verified:")), None)
            if idx is None:
                ref.write_text("\n".join([lines[0], "", STAMP] + lines[1:]) + "\n",
                               encoding="utf-8")
            else:
                lines[idx] = STAMP  # renew existing date
                ref.write_text("\n".join(lines) + "\n", encoding="utf-8")
            n_refs += 1
        meta = stamp_skill_meta(d)
        if n_refs or meta:
            print(f"[STAMPED] {name} ({n_refs} refs, skill-meta={meta})")
        elif refs:
            print(f"[STAMP-SKIP] {name}: already stamped")


def main():
    if "--stamp" in sys.argv:
        global STAMP, SKILL_STAMP
        today = dt.date.today().isoformat()
        STAMP = f"last-verified: {today}"
        SKILL_STAMP = f'last_verified: "{today}"'
        stamp([a for a in sys.argv[2:] if not a.startswith("--")])
        return 0
    check = "--check" in sys.argv
    today = dt.date.today()
    missing, stale = [], []
    for ref in sorted((REPO / "skills").glob("*/references/*.md")):
        skill = ref.parts[-3]
        got, kind = ref_date(ref.read_text(encoding="utf-8"))
        if not got:
            if skill in rolled():
                missing.append(f"{skill}/{ref.name}")
            continue
        try:
            seen = dt.date(int(got[0]), int(got[1]), int(got[2]))
        except ValueError:
            missing.append(f"{skill}/{ref.name} (bad date)")
            continue
        if (today - seen).days > STALE_DAYS:
            stale.append(f"{skill}/{ref.name} ({seen.isoformat()}, {kind})")
    for m in missing:
        print(f"[MISSING] {m}")
    for s in stale:
        print(f"[STALE] {s}")
    for name in sorted(rolled()):
        p = REPO / "skills" / name / "SKILL.md"
        if not p.is_file():
            continue
        m = SKILL_PAT.search(p.read_text(encoding="utf-8"))
        if not m:
            missing.append(f"{name}/SKILL.md (no last_verified)")
            print(f"[MISSING] {name}/SKILL.md (no last_verified)")
            continue
        try:
            seen = dt.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
        except ValueError:
            missing.append(f"{name}/SKILL.md (bad date)")
            print(f"[MISSING] {name}/SKILL.md (bad date)")
            continue
        if (today - seen).days > STALE_DAYS:
            stale.append(f"{name}/SKILL.md ({m.group(0)})")
            print(f"[STALE] {name}/SKILL.md ({m.group(0)})")
    pilot_refs = sum(1 for _ in (REPO / "skills").glob("*/references/*.md"))
    print(f"freshness: {len(missing)} missing, {len(stale)} stale "
          f"({len(rolled())} skills, {pilot_refs} refs)")
    if check and (missing or stale):
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
