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

    mut = run("mutuo-tassi", "mutuo.py",
              {"capitale": 150000, "anni": 25, "taeg-a": 4.0,
               "tan-b": 3.5, "shock": 2.0})
    hold("mutuo: totale_a == rata_a*n",
         abs(mut["totale_a"] - mut["rata_a"] * 300) < 0.05, str(mut))
    hold("mutuo: shock peggiora la rata",
         mut["rata_b_shock"] > mut["rata_b"] > 0, str(mut))

    ced = run("cedolare-secca", "cedolare.py",
              {"canone": 24000, "cedolare": 21, "marginale": 43})
    hold("cedolare: costi == canone*aliquote",
         abs(ced["costo_cedolare"] - 24000 * 0.21) < TOL
         and abs(ced["costo_irpef_stimato"] - 24000 * 0.43) < TOL, str(ced))

    bus = run("busta-paga-leggi", "payslip_check.py",
              {"lordo": 1950, "inps": 180, "irpef": 120,
               "detrazioni": 30, "netto": 1620})
    hold("busta: gap == ricalcolato-netto",
         abs(bus["gap"] - (bus["netto_ricalcolato"] - 1620)) < TOL, str(bus))

    tfr = run("tfr-fondo", "rivalutazione.py",
              {"accantonato": 20000, "inflazione": 4.0, "year": 2026})
    hold("tfr: rivalutazione == accantonato*tasso/100",
         abs(tfr["rivalutazione"] - 20000 * tfr["tasso_pct"] / 100) < TOL,
         str(tfr))

    print(f"invariants: {19 - len(fails)}/19 hold")
    return 2 if fails else 0


if __name__ == "__main__":
    raise SystemExit(main())
