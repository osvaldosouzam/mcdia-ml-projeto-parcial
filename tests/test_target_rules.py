from __future__ import annotations

import ast
import json
import sys
import unittest
from pathlib import Path

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))


def load_classifier():
    path = ROOT / "notebooks/avaliacao_01/lucimar_oliveira_do_nascimento.ipynb"
    notebook = json.loads(path.read_text(encoding="utf-8"))
    source = "\n".join(
        "".join(cell.get("source", []))
        for cell in notebook["cells"]
        if cell["cell_type"] == "code"
    )
    tree = ast.parse(source)
    functions = [
        node for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == "classificar_faixas"
    ]
    if len(functions) != 1:
        raise AssertionError("O notebook deve definir classificar_faixas exatamente uma vez")
    module = ast.fix_missing_locations(ast.Module(body=functions, type_ignores=[]))
    namespace = {"np": np, "pd": pd}
    exec(compile(module, str(path), "exec"), namespace)
    return namespace["classificar_faixas"]


class TargetRulesTest(unittest.TestCase):
    def test_all_boundaries_and_missing_value(self) -> None:
        classifier = load_classifier()
        values = [
            -1, 0, np.nextafter(0.0, 1.0), np.nextafter(15.0, 0.0), 15,
            30, np.nextafter(30.0, np.inf), 45, np.nextafter(45.0, np.inf),
            60, np.nextafter(60.0, np.inf), np.nan,
        ]
        result = classifier(values)
        self.assertEqual([0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5], result.iloc[:-1].tolist())
        self.assertTrue(pd.isna(result.iloc[-1]))

    def test_binary_target_matches_multiclass_rule(self) -> None:
        classifier = load_classifier()
        values = pd.Series([-10, 0, 1, 14.99, 15, 30, 45, 60, 61])
        classes = classifier(values)
        binary_from_delay = values.ge(15).astype("Int64")
        binary_from_class = classes.ge(2).astype("Int64")
        pd.testing.assert_series_equal(binary_from_delay, binary_from_class)


if __name__ == "__main__":
    unittest.main()
