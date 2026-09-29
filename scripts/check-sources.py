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
PILOT = PILOT | CASA | {"accertamento-info", "adozioni-info",
         "affido-familiare", "appalti-pubblici-info",
         "assicurazione-vita-info", "contratto-base-check", "contratto-tipi",
         "criptovalute-fisco", "fallimento-crisi-info", "franchising-info",
         "invalidita-104", "irap-info", "marchi-info", "maternita-congedi",
         "multe-ricorso", "pensione-reversibilita", "permesso-soggiorno",
         "pignoramento-conto", "unioni-convivenze", "vaccini-obbligatori",
         "whistleblowing-info"}
OFFICIAL = ("inps.it", "agenziaentrate.gov.it", "salute.gov.it",
            "interno.gov.it", "lavoro.gov.it", "giustizia.it",
            "normattiva.it", "gazzettaufficiale.it", "europa.eu",
            "senato.it", "camera.it", "istat.it", "inail.it",
            "arera.it", "enea.it", "mase.gov.it", "parlamento.it",
            "notariato.it", "bancaditalia.it", "ivass.it",
            "arera.it", "enea.it", "mase.gov.it", "parlamento.it",
            "anticorruzione.it", "poliziadistato.it", "uibm.mise.gov.it",
            "mise.gov.it")
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
    blocks, cur = [], None
    for ln in txt.splitlines():
        if ln.startswith("- source:"):
            cur = {"source": ln[len("- source:"):].strip(), "url": None, "claims": []}
            blocks.append(cur)
        elif ln.startswith("  url:") and cur is not None:
            cur["url"] = ln[len("  url:"):].strip()
        elif ln.startswith("    - ") and cur is not None:
            cur["claims"].append(ln[len("    - "):].strip())
    if not blocks:
        errs.append(f"{skill}: no source blocks (want '- source:' + url + claims)")
    for b in blocks:
        if not b["url"] or not URL.match(b["url"]):
            errs.append(f"{skill}: block without valid URL: {b['source'][:60]}")
            continue
        if not official_host(b["url"]):
            errs.append(f"{skill}: non-official host: {b['url'][:80]}")
        real = [c for c in b["claims"] if len(c) >= 15]
        if not real:
            errs.append(f"{skill}: no meaningful claims (>=15 chars): {b['source'][:60]}")
    stale = (dt.date.today() - seen).days > STALE_DAYS
    urls = [b["url"] for b in blocks if b["url"] and URL.match(b["url"])]
    return (seen, stale, urls), errs


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
