#!/usr/bin/env python3
"""Semantic source check for rolled-out skills (see docs/FRESHNESS.md).

Each PILOT skill must carry references/fonti-verificate.md with a
`## Sources (verified YYYY-MM-DD)` block. Every bullet needs:
  - an https:// URL on an official domain (allow-list below),
  - a `claims:` list mapping the source to the rules that depend on it.

This proves WHICH claims depend on WHICH source — a timestamp alone cannot.
Link liveness is advisory only: `check-sources.py --check-links` (network).

Usage:
  python scripts/check-sources.py           # report only, exit 0
  python scripts/check-sources.py --check   # exit 2 on schema/date failures
  python scripts/check-sources.py --check-links  # HEAD each URL, advisory
"""
import datetime as dt
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

REPO = Path(__file__).resolve().parents[1]
STALE_DAYS = 365
PILOT = {"pensione-guida", "successioni-info", "salute-mentale-info",
         "cittadinanza", "separazione-divorzio", "licenziamento-info"}
CASA = {"affitto-breve", "affitto-check", "affitto-concordato",
        "amministratore-condominio", "ape-certificazione",
        "assemblea-condominiale", "assicurazione-casa", "banche-reclami",
        "bollette-energia", "bonus-casa", "comodato-uso",
        "compravendita-casa", "condominio-spese", "diffida-legale",
        "donazioni-info", "edilizia-cila-scia", "eredita-debiti",
        "lavori-straordinari", "mantenimento-figli", "mediazione-civile",
        "morosita-condominiale", "multe-ricorso", "mutuo-tassi",
        "percorso-casa-compravendita", "percorso-lutto",
        "prima-casa-agevolazioni", "spese-notarili",
        "testamento-biologico-dat", "testamento-olografo",
        "testamento-pubblico", "usufrutto-nuda", "utenze-voltura",
        "visura-leggimi", "volture-catastali"}
PILOT = PILOT | CASA
OFFICIAL = ("inps.it", "agenziaentrate.gov.it", "salute.gov.it",
            "interno.gov.it", "lavoro.gov.it", "giustizia.it",
            "normattiva.it", "gazzettaufficiale.it", "europa.eu",
            "senato.it", "camera.it", "istat.it", "inail.it",
            "arera.it", "enea.it", "mase.gov.it", "parlamento.it",
            "notariato.it", "bancaditalia.it", "ivass.it")
HEAD = re.compile(r"^## Sources \(verified (\d{4})-(\d{2})-(\d{2})\)", re.M)
URL = re.compile(r"https://[^\s)>\"]+")


def official_host(url):
    """True only for the domain itself or its subdomains. Substring tricks
    (evil-inps.it, inps.it.evil.com, ?x=inps.it) fail: only the parsed
    hostname counts."""
    try:
        host = urlparse(url).hostname or ""
    except ValueError:
        return False
    host = host.lower()
    return any(host == d or host.endswith("." + d) for d in OFFICIAL)


def parse(skill):
    p = REPO / "skills" / skill / "references" / "fonti-verificate.md"
    if not p.is_file():
        return None, [f"{skill}: missing references/fonti-verificate.md"]
    txt = p.read_text(encoding="utf-8")
    errs = []
    m = HEAD.search(txt)
    if not m:
        return None, [f"{skill}: missing '## Sources (verified YYYY-MM-DD)' header"]
    try:
        seen = dt.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    except ValueError:
        return None, [f"{skill}: bad verified date"]
    bullets = [ln for ln in txt.splitlines() if ln.startswith("- ")]
    if not bullets:
        errs.append(f"{skill}: no source bullets")
    for b in bullets:
        urls = URL.findall(b)
        if not urls:
            errs.append(f"{skill}: bullet without URL: {b[:80]}")
            continue
        if not official_host(urls[0]):
            errs.append(f"{skill}: non-official host: {urls[0][:80]}")
        if "claims:" not in b:
            errs.append(f"{skill}: bullet without claims: {b[:80]}")
    stale = (dt.date.today() - seen).days > STALE_DAYS
    return (seen, stale, [URL.findall(b)[0] for b in bullets if URL.findall(b)]), errs


def main():
    args = sys.argv[1:]
    if "--check-links" in args:
        import urllib.request
        bad = 0
        for skill in sorted(PILOT):
            info, _ = parse(skill)
            if not info:
                continue
            for u in info[2]:
                code, how = None, "HEAD"
                try:
                    req = urllib.request.Request(u, method="HEAD",
                                                 headers={"User-Agent": "italy-work-skills-linkcheck"})
                    code = urllib.request.urlopen(req, timeout=20).status
                except Exception:  # noqa: BLE001 - HEAD often blocked; try GET
                    try:
                        req = urllib.request.Request(u, method="GET",
                                                     headers={"User-Agent": "Mozilla/5.0"})
                        with urllib.request.urlopen(req, timeout=20) as r:
                            r.read(4096)
                            code = r.status
                            how = "GET"
                    except Exception as e2:  # noqa: BLE001
                        print(f"[DEAD] {skill}: {u[:90]} ({type(e2).__name__})")
                        bad += 1
                        continue
                print(f"[{'ok' if code < 400 else 'DEAD'}] {skill}: {u[:90]} -> {code} ({how})")
                bad += code >= 400
        print(f"links: {bad} dead/unreachable (advisory)")
        return 0
    check = "--check" in args
    missing, stale = [], []
    for skill in sorted(PILOT):
        info, errs = parse(skill)
        for e in errs:
            print(f"[MISSING] {e}")
            missing.append(e)
        if info and info[1]:
            print(f"[STALE] {skill}: sources verified {info[0]}")
            stale.append(skill)
    print(f"sources: {len(PILOT) - len(missing)} /{len(PILOT)} pilot skills schema-ok, "
          f"{len(stale)} stale")
    if check and (missing or stale):
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
