"""Checks for the contradiction matrix data. Run: python -m unittest discover -s tests"""
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / "triz" / "scripts" / "matrix.json").read_text(encoding="utf-8"))
M = DATA["matrix"]

# Cells cross-checked against the matrix published at triz40.com
KNOWN = {
    "1,3": [15, 8, 29, 34], "1,9": [2, 8, 15, 38], "1,38": [26, 35, 18, 19], "2,4": [10, 1, 29, 35],
    "4,33": [2, 25], "4,34": [3], "7,5": [1, 7, 4, 17], "8,25": [35, 16, 32, 18], "9,10": [13, 28, 15, 19],
    "10,1": [8, 1, 37, 18], "11,7": [6, 35, 10], "11,21": [10, 35, 14], "12,29": [32, 30, 40],
    "13,22": [14, 2, 39, 6], "14,1": [1, 8, 40, 15], "14,15": [27, 3, 26], "14,31": [15, 35, 22, 2],
    "18,24": [1, 6], "19,9": [8, 35], "22,13": [14, 2, 39, 6], "27,1": [3, 8, 10, 40],
    "27,36": [13, 35, 1], "28,5": [26, 28, 32, 3], "30,26": [35, 33, 29, 31], "32,18": [28, 24, 27, 1],
    "34,3": [1, 28, 10, 25], "38,7": [35, 13, 16], "39,1": [35, 26, 24, 37],
}


class MatrixData(unittest.TestCase):
    def test_shape(self):
        self.assertEqual(len(DATA["parameters"]), 39)
        self.assertEqual(len(DATA["principles"]), 40)
        self.assertGreater(len(M), 1200)

    def test_cells_valid(self):
        for k, v in M.items():
            i, j = map(int, k.split(","))
            self.assertTrue(1 <= i <= 39 and 1 <= j <= 39 and i != j, k)
            self.assertTrue(1 <= len(v) <= 4, k)
            self.assertEqual(len(set(v)), len(v), k)
            self.assertTrue(all(1 <= p <= 40 for p in v), k)

    def test_known_cells(self):
        for k, v in KNOWN.items():
            self.assertEqual(M.get(k), v, k)

    def test_empty_cells(self):
        for k in ["1,2", "1,4", "2,1", "4,38"]:
            self.assertNotIn(k, M)


class Script(unittest.TestCase):
    def run_script(self, *args):
        return subprocess.run([sys.executable, str(ROOT / "triz" / "scripts" / "matrix.py"), *args],
                              capture_output=True, text=True)

    def test_lookup(self):
        out = self.run_script("14", "1")
        self.assertEqual(out.returncode, 0)
        self.assertIn("40 Composite materials", out.stdout)

    def test_json(self):
        out = json.loads(self.run_script("--json", "--improve", "9", "39", "--worsen", "27").stdout)
        self.assertEqual(len(out["cells"]), 2)

    def test_find(self):
        self.assertIn("Speed", self.run_script("--find", "latency").stdout)

    def test_bad_input(self):
        self.assertNotEqual(self.run_script("40", "1").returncode, 0)


if __name__ == "__main__":
    unittest.main()
