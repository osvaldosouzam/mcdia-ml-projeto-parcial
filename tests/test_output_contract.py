from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_common.paths import EvaluationOnePaths  # noqa: E402


class OutputContractTest(unittest.TestCase):
    def test_evaluation_one_has_exactly_four_expected_outputs(self) -> None:
        paths = EvaluationOnePaths()
        self.assertEqual(
            {
                "lucimar_oliveira_do_nascimento.ipynb",
                "dicionario_lucimar_oliveira_do_nascimento.xlsx",
                "base_lucimar_oliveira_do_nascimento.zip",
                "relatorio_parcial_lucimar_oliveira_do_nascimento.docx",
            },
            {path.name for path in paths.required_outputs},
        )


if __name__ == "__main__":
    unittest.main()
