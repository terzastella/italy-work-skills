#!/usr/bin/env python3
"""Behavior guards for Golden + delicate skills (superpowers-1 block).

Deterministic static checks, no LLM, no network. Exit 2 on any failure.
CI runs this alongside eval-golden.py.

- Golden (20): run protocol present (input.md + expect.md, non-trivial),
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
          "colf-badanti", "partita-iva-apri", "isee-guida", "hello-agent"]

YEAR_REQUIRED = set(GOLDEN) - {"hello-agent", "email-formale-it", "pec-bozza", "cv-europass"}
LINK_REQUIRED = set(GOLDEN) - {"hello-agent"}
GOODBAD_REQUIRED = set(GOLDEN) - {"hello-agent"}

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
    # --- Golden protocols + static guards ---
    for name in GOLDEN:
        proto = TESTS / name
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

    print(f"behavior: {'FAIL' if fails else 'OK'} ({len(GOLDEN)} golden, {len(DELICATE)} delicate)")
    return 2 if fails else 0


if __name__ == "__main__":
    raise SystemExit(main())
