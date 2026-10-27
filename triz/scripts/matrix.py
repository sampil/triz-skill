#!/usr/bin/env python3
"""Look up the classical TRIZ contradiction matrix (Altshuller, 39 x 39).

Usage:
  matrix.py 9 14                          one cell: improving 9, worsening 14
  matrix.py --improve 9 39 --worsen 14 36 several pairs, principles ranked by frequency
  matrix.py --find latency                search parameters by keyword (names and glosses)
  matrix.py --params                      list all 39 parameters
  matrix.py --principle 35 10             names of principles
  matrix.py --top [N]                     principles that appear most often in the matrix
  add --json to any command for machine-readable output
"""
import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = json.loads((HERE / "matrix.json").read_text(encoding="utf-8"))
PARAMS = {int(k): v for k, v in DATA["parameters"].items()}
PRINCIPLES = {int(k): v for k, v in DATA["principles"].items()}
MATRIX = {tuple(map(int, k.split(","))): v for k, v in DATA["matrix"].items()}


def glosses():
    """Parameter glosses from references/parameters.md, if present (for --find)."""
    path = HERE.parent / "references" / "parameters.md"
    out = {}
    if not path.exists():
        return out
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"\|\s*(\d+)\s*\|(.+)\|\s*$", line)
        if m:
            cols = [c.strip() for c in m.group(2).split("|")]
            out[int(m.group(1))] = " | ".join(cols[1:])
    return out


def check_param(n):
    if n not in PARAMS:
        sys.exit(f"Parameter {n} is out of range: use 1..39 (see --params).")


def fmt_principles(nums):
    return ", ".join(f"{n} {PRINCIPLES[n]}" for n in nums)


def cell(i, j):
    check_param(i)
    check_param(j)
    return MATRIX.get((i, j), [])


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pair", nargs="*", type=int, help="improving worsening")
    ap.add_argument("--improve", nargs="+", type=int)
    ap.add_argument("--worsen", nargs="+", type=int)
    ap.add_argument("--find")
    ap.add_argument("--params", action="store_true")
    ap.add_argument("--principle", nargs="+", type=int)
    ap.add_argument("--top", nargs="?", const=10, type=int)
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    if a.params or a.find:
        g = glosses()
        q = (a.find or "").lower()
        rows = [(n, PARAMS[n], g.get(n, "")) for n in sorted(PARAMS)
                if not q or q in PARAMS[n].lower() or q in g.get(n, "").lower()]
        if a.json:
            print(json.dumps([{"id": n, "name": p, "gloss": s} for n, p, s in rows], ensure_ascii=False, indent=1))
        elif not rows:
            print(f"No parameter matches '{a.find}'. Try a broader word or see --params.")
        else:
            for n, p, s in rows:
                print(f"{n:>2}  {p}" + (f"\n    {s}" if s and a.find else ""))
        return

    if a.principle:
        bad = [n for n in a.principle if n not in PRINCIPLES]
        if bad:
            sys.exit(f"Principles are numbered 1..40; got {bad}.")
        if a.json:
            print(json.dumps({n: PRINCIPLES[n] for n in a.principle}, ensure_ascii=False))
        else:
            for n in a.principle:
                print(f"{n:>2}  {PRINCIPLES[n]}")
        return

    if a.top:
        c = Counter(p for v in MATRIX.values() for p in v)
        top = c.most_common(a.top)
        if a.json:
            print(json.dumps([{"principle": n, "name": PRINCIPLES[n], "count": k} for n, k in top], ensure_ascii=False))
        else:
            for n, k in top:
                print(f"{n:>2}  {PRINCIPLES[n]:<28} {k} cells")
        return

    if a.pair:
        if len(a.pair) != 2:
            sys.exit("Give exactly two numbers: improving worsening.")
        improve, worsen = [a.pair[0]], [a.pair[1]]
    elif a.improve and a.worsen:
        improve, worsen = a.improve, a.worsen
    else:
        ap.print_help()
        return

    results, tally = [], Counter()
    for i in improve:
        for j in worsen:
            if i == j:
                continue
            v = cell(i, j)
            results.append({"improving": [i, PARAMS[i]], "worsening": [j, PARAMS[j]], "principles": v})
            for rank, p in enumerate(v):
                tally[p] += 1
    ranked = sorted(tally, key=lambda p: (-tally[p], p))

    if a.json:
        print(json.dumps({"cells": results,
                          "ranked": [{"principle": p, "name": PRINCIPLES[p], "count": tally[p]} for p in ranked]},
                         ensure_ascii=False, indent=1))
        return

    if not results:
        sys.exit("Improving and worsening parameters must differ.")
    for r in results:
        (i, pi), (j, pj), v = r["improving"], r["worsening"], r["principles"]
        print(f"Improve {i} {pi}  vs  worsen {j} {pj}")
        print("  " + (fmt_principles(v) if v else "(empty cell: no classical recommendation; "
                                                 "go to the physical contradiction and separation, or try --top)"))
    if len(results) > 1 and ranked:
        print("\nRanked across all pairs:")
        for p in ranked:
            print(f"  {p:>2} {PRINCIPLES[p]:<28} x{tally[p]}")


if __name__ == "__main__":
    main()
