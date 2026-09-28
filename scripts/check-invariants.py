#!/usr/bin/env python3
"""Structural invariant checks for neutral calculators.

Golden fixtures catch regressions; hand oracles catch wrong formulas shipped
with wrong expectations. This layer catches INTERNAL incoherence: outputs
that contradict each other or their own inputs, on fixed canonical cases.
Deterministic, no LLM, no network. Exit 2 on violation, 0 when all hold.

Usage:
  python scripts/check-invariants.py
"""
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
TOL = 0.02


def _load_golden():
    spec = importlib.util.spec_from_file_location(
        "eval_golden", REPO / "scripts" / "eval-golden.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.argv


argv = _load_golden()
fails = []


def run(skill, script, inp):
    skill_dir = REPO / "skills" / skill
    r = subprocess.run(argv(skill_dir, script, inp), capture_output=True,
                       text=True, timeout=60, cwd=REPO)
    if r.returncode != 0:
        raise RuntimeError(f"{skill}: exit {r.returncode}: {r.stderr.strip()[:150]}")
    return json.loads(r.stdout)


def hold(name, cond, detail=""):
    if cond:
        print(f"[ok] {name}")
    else:
        print(f"[FAIL] {name} {detail}")
        fails.append(name)


def main():
    imu = run("imu-calcolo", "imu.py",
              {"rendita": 850, "moltiplicatore": 160, "aliquota-per-mille": 10.6,
               "detrazione": 0, "mesi": 12, "year": 2026})
    hold("imu: acconto+saldo == imposta",
         abs(imu["acconto_giugno"] + imu["saldo_dicembre"] - imu["imposta_dovuta"]) < TOL,
         str(imu))
    hold("imu: base == rendita*1.05*moltiplicatore",
         abs(imu["base_imponibile"] - 850 * 1.05 * 160) < TOL, str(imu))
    hold("imu: imposta == base*aliquota/1000",
         abs(imu["imposta_dovuta"] - imu["base_imponibile"] * 10.6 / 1000) < TOL,
         str(imu))

    irpef = run("irpef-scaglioni", "irpef.py",
                {"reddito": 35000, "scaglioni": "examples/scaglioni-2025.json",
                 "year": 2025})
    hold("irpef: media == imposta/reddito*100",
         abs(irpef["aliquota_media_pct"] - irpef["imposta"] / 35000 * 100) < 0.05,
         str(irpef))
    hold("irpef: marginale in {23,25,43}",
         irpef["aliquota_marginale_pct"] in (23.0, 25.0, 43.0), str(irpef))

    inv = run("invoice-it", "totals.py", "examples/items-610.json")
    hold("invoice: totale == imponibile + sum(iva)",
         abs(inv["totale"] - inv["imponibile"] - sum(inv["iva_per_aliquota"].values())) < TOL,
         str(inv))

    forf = run("regime-forfettario", "forfettario.py",
               {"fatturato": 50000, "coeff": 0.78, "contributi": 5000,
                "aliquota": 5, "year": 2026})
    hold("forfettario: reddito == fatturato*coeff",
         abs(forf["reddito"] - 50000 * 0.78) < TOL, str(forf))
    hold("forfettario: base == reddito-contributi",
         abs(forf["base_imponibile"] - (forf["reddito"] - 5000)) < TOL, str(forf))
    hold("forfettario: imposta == base*5%",
         abs(forf["imposta_5pct"] - forf["base_imponibile"] * 0.05) < TOL,
         str(forf))

    acc = run("acconti-calcolo", "acconti.py",
              {"imposta": 10000, "split": "100", "year": 2026})
    hold("acconti: sum(rate) == base",
         abs(sum(acc["rate"]) - acc["base"]) < TOL, str(acc))

    print(f"invariants: {10 - len(fails)}/10 hold")
    return 2 if fails else 0


if __name__ == "__main__":
    raise SystemExit(main())
