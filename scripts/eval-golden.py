#!/usr/bin/env python3
"""Deterministic eval for Golden-1 neutral scripts (fiducia phase).

Runs every script against its committed fixtures in examples/fixtures/
and compares the declared expected outputs. No LLM, no network.
Exit 2 on any mismatch, 0 when all green. CI runs this.

Usage:
  python scripts/eval-golden.py
"""
import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
TOL = 0.011


def argv(skill_dir, script, inp):
    exe = str(skill_dir / "scripts" / script)
    a = [sys.executable, exe]
    rel = lambda p: str(skill_dir / p)
    if script == "imu.py":
        a += ["--rendita", str(inp["rendita"]), "--moltiplicatore", str(inp["moltiplicatore"]),
              "--aliquota-per-mille", str(inp["aliquota-per-mille"]),
              "--detrazione", str(inp.get("detrazione", 0)), "--mesi", str(inp.get("mesi", 12)),
              "--year", str(inp["year"])]
    elif script == "irpef.py":
        a += ["--reddito", str(inp["reddito"]), "--scaglioni", rel(inp["scaglioni"]),
              "--year", str(inp["year"])]
    elif script == "acconti.py":
        a += ["--imposta", str(inp["imposta"]), "--split", str(inp["split"]),
              "--year", str(inp["year"])]
        if "previsione" in inp:
            a += ["--previsione", str(inp["previsione"])]
    elif script == "forfettario.py":
        if "fatturato" in inp:
            a += ["--fatturato", str(inp["fatturato"]), "--coeff", str(inp["coeff"]),
                  "--contributi", str(inp.get("contributi", 0)),
                  "--aliquota", str(inp.get("aliquota", 15)), "--year", str(inp["year"])]
        else:
            a += ["--soglia-check", str(inp["soglia-check"]), "--year", str(inp["year"])]
    elif script == "totals.py":
        a += ["--items", rel(inp)]  # fixture input is the items path itself
    elif script == "payslip_check.py":
        a += ["--lordo", str(inp["lordo"]), "--inps", str(inp["inps"]),
              "--irpef", str(inp["irpef"]), "--detrazioni", str(inp.get("detrazioni", 0)),
              "--netto", str(inp["netto"])]
    elif script == "ratei.py":
        a += ["--spettanza", str(inp["spettanza"]), "--mese", str(inp["mese"]),
              "--fruiti", str(inp.get("fruiti", 0))]
        if "part-time" in inp:
            a += ["--part-time", str(inp["part-time"])]
    elif script == "ritenuta.py":
        if "lordo" in inp:
            a += ["--lordo", str(inp["lordo"])]
        if "netto" in inp:
            a += ["--netto", str(inp["netto"])]
        a += ["--aliquota", str(inp.get("aliquota", 20))]
        if inp.get("forfettario"):
            a += ["--forfettario"]
    elif script == "rivalutazione.py":
        a += ["--accantonato", str(inp["accantonato"]), "--inflazione", str(inp["inflazione"]),
              "--year", str(inp["year"])]
    elif script == "cedolare.py":
        a += ["--canone", str(inp["canone"]), "--cedolare", str(inp.get("cedolare", 21)),
              "--marginale", str(inp["marginale"])]
    elif script == "tredicesima.py":
        a += ["--retribuzione", str(inp["retribuzione"]), "--mesi", str(inp["mesi"])]
        if "part-time" in inp:
            a += ["--part-time", str(inp["part-time"])]
    elif script == "riscatto.py":
        a += ["--anni", str(inp["anni"]), "--tariffa", str(inp["tariffa"]),
              "--year", str(inp["year"])]
    elif script == "ravvedimento.py":
        a += ["--imposta", str(inp["imposta"]), "--giorni", str(inp["giorni"]),
              "--sanzione-pct", str(inp["sanzione-pct"]), "--tasso-legale", str(inp["tasso-legale"]),
              "--year", str(inp["year"])]
    elif script == "compensa.py":
        a += ["--crediti", str(inp["crediti"]), "--debiti", str(inp["debiti"]),
              "--soglia-visto", str(inp["soglia-visto"]), "--year", str(inp["year"])]
    elif script == "detrai19.py":
        a += ["--spese", str(inp["spese"]), "--franchigia", str(inp["franchigia"]),
              "--year", str(inp["year"])]
    elif script == "pluscasa.py":
        a += ["--acquisto", str(inp["acquisto"]), "--vendita", str(inp["vendita"]),
              "--gain", str(inp["gain"]), "--sostitutiva", str(inp.get("sostitutiva", 26)),
              "--year", str(inp["year"])]
        if "marginale" in inp:
            a += ["--marginale", str(inp["marginale"])]
    elif script == "rateizza.py":
        a += ["--debito", str(inp["debito"]), "--n-rate", str(inp["n-rate"]),
              "--interesse", str(inp["interesse"]), "--year", str(inp["year"])]
    elif script == "straord.py":
        a += ["--ore", str(inp["ore"]), "--paga-oraria", str(inp["paga-oraria"]),
              "--maggiorazione", str(inp["maggiorazione"])]
    elif script == "occasionali.py":
        a += ["--lordo", str(inp["lordo"]), "--ritenuta", str(inp.get("ritenuta", 20)),
              "--franchigia-inps", str(inp["franchigia-inps"]), "--year", str(inp["year"])]
    elif script == "riparto.py":
        a += ["--totale", str(inp["totale"]), "--millesimi", str(inp["millesimi"]),
              "--addebitato", str(inp["addebitato"])]
    elif script == "mutuo.py":
        a += ["--capitale", str(inp["capitale"]), "--anni", str(inp["anni"]),
              "--taeg-a", str(inp["taeg-a"]), "--tan-b", str(inp["tan-b"]),
              "--shock", str(inp.get("shock", 2.0))]
    elif script == "deposito.py":
        a += ["--capitale", str(inp["capitale"]), "--lordo", str(inp["lordo"]),
              "--bollo", str(inp.get("bollo", 0)), "--year", str(inp["year"])]
    elif script == "revolving.py":
        a += ["--saldo", str(inp["saldo"]), "--taeg", str(inp["taeg"]),
              "--rata", str(inp["rata"])]
    elif script == "bpf.py":
        a += ["--capitale", str(inp["capitale"]), "--lordo", str(inp["lordo"]),
              "--bollo", str(inp.get("bollo", 0)), "--year", str(inp["year"])]
    elif script == "contributi.py":
        a += ["--reddito", str(inp["reddito"]), "--aliquota", str(inp["aliquota"]),
              "--split", str(inp.get("split", "40,40,20")), "--year", str(inp["year"])]
    elif script == "bollo.py":
        a += ["--importo", str(inp["importo"]), "--soglia", str(inp["soglia"]),
              "--bollo", str(inp.get("bollo", 2)), "--year", str(inp["year"])]
    elif script == "fondo.py":
        a += ["--spese", str(inp["spese"]), "--profilo", str(inp.get("profilo", "dipendente"))]
        if "surplus" in inp:
            a += ["--surplus", str(inp["surplus"])]
    elif script == "plusvalenza.py":
        a += ["--gain", str(inp["gain"]), "--minus", str(inp.get("minus", 0)),
              "--aliquota", str(inp["aliquota"]), "--year", str(inp["year"])]
    elif script == "fasce.py":
        a += ["--isee", str(inp["isee"]), "--minori", str(inp["minori"]),
              "--tabella", rel(inp["tabella"]), "--year", str(inp["year"])]
    elif script == "budget.py":
        # argparse: one --spese flag followed by all CAT:amount values
        a = [sys.executable, exe, "--month", str(inp["month"]),
             "--income", str(inp["income"]), "--out", "tmp-eval-budget"]
        if inp.get("spese"):
            a += ["--spese"] + list(inp["spese"])
    else:
        raise ValueError(f"unknown script {script}")
    return a + ["--json"]


def close_enough(got, want, path=""):
    if isinstance(want, dict):
        if not isinstance(got, dict):
            return [f"{path}: expected object, got {got!r}"]
        errs = []
        for k, v in want.items():
            if k not in got:
                errs.append(f"{path}.{k}: missing in output")
            else:
                errs.extend(close_enough(got[k], v, f"{path}.{k}"))
        return errs
    if isinstance(want, (int, float)) and isinstance(got, (int, float)):
        return [] if abs(got - want) < TOL else [f"{path}: got {got}, want {want}"]
    return [] if got == want else [f"{path}: got {got!r}, want {want!r}"]


def main():
    skills_root = REPO / "skills"
    total, failed = 0, 0
    for skill_dir in sorted(skills_root.iterdir()):
        scripts = skill_dir / "scripts"
        fixtures = skill_dir / "examples" / "fixtures"
        if not scripts.is_dir() or not fixtures.is_dir():
            continue
        py = sorted(scripts.glob("*.py"))
        fx = sorted(fixtures.glob("*.json"))
        if not py or not fx:
            continue
        script = py[0].name
        for f in fx:
            total += 1
            data = json.loads(f.read_text(encoding="utf-8"))
            try:
                r = subprocess.run(argv(skill_dir, script, data["input"]),
                                   capture_output=True, text=True, timeout=60, cwd=REPO)
            except Exception as e:  # noqa: BLE001
                print(f"[FAIL] {skill_dir.name}/{f.name}: runner error {e}")
                failed += 1
                continue
            if r.returncode != 0:
                print(f"[FAIL] {skill_dir.name}/{f.name}: exit {r.returncode}: {r.stderr.strip()[:200]}")
                failed += 1
                continue
            try:
                out = json.loads(r.stdout)
            except ValueError:
                print(f"[FAIL] {skill_dir.name}/{f.name}: not JSON output")
                failed += 1
                continue
            errs = close_enough(out, data["expected"])
            if errs:
                print(f"[FAIL] {skill_dir.name}/{f.name}:")
                for e in errs:
                    print(f"  - {e}")
                failed += 1
            else:
                print(f"[ok] {skill_dir.name}/{f.name}")
    print(f"eval: {total - failed}/{total} fixtures green")
    return 2 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
