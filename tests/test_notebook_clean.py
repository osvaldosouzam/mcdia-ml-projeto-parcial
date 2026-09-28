from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_common.notebook import (  # noqa: E402
    NotebookSourceError,
    prepare_notebook,
    validate_clean_notebook,
)


class NotebookCleanTest(unittest.TestCase):
    def test_project_notebook_is_clean_and_maps_consolidated_schema(self) -> None:
        source = ROOT / "notebooks/avaliacao_01/lucimar_oliveira_do_nascimento.ipynb"
        validate_clean_notebook(source)
        notebook = json.loads(source.read_text(encoding="utf-8"))
        content = "\n".join(
            "".join(cell.get("source", [])) for cell in notebook["cells"]
        )
        for expected in (
            "'companhia_icao': 'sg_empresa_icao'",
            "'origem_icao': 'sg_icao_origem'",
            "'destino_icao': 'sg_icao_destino'",
            "base_lucimar_oliveira_do_nascimento.zip",
            "codigo_faixa_atraso",
        ):
            self.assertIn(expected, content)
        self.assertNotIn("copy=False", content)

    def test_project_notebook_is_split_into_small_didactic_units(self) -> None:
        source = ROOT / "notebooks/avaliacao_01/lucimar_oliveira_do_nascimento.ipynb"
        notebook = json.loads(source.read_text(encoding="utf-8"))
        code_cells = [cell for cell in notebook["cells"] if cell["cell_type"] == "code"]
        markdown_cells = [cell for cell in notebook["cells"] if cell["cell_type"] == "markdown"]
        content = "\n".join("".join(cell.get("source", [])) for cell in notebook["cells"])

        self.assertGreaterEqual(len(markdown_cells), len(code_cells))
        self.assertLessEqual(
            max(len("".join(cell["source"]).splitlines()) for cell in code_cells),
            45,
        )
        self.assertNotIn("CÉLULA ", content.upper())
        self.assertNotRegex(content, r"={8,}")
        self.assertNotIn("warnings.filterwarnings", content)
        self.assertNotIn("except Exception", content)

    def test_prepare_removes_outputs_and_execution_counts(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "source.ipynb"
            output = Path(directory) / "output.ipynb"
            notebook = {
                "cells": [
                    {
                        "cell_type": "code",
                        "execution_count": 3,
                        "metadata": {},
                        "outputs": [{"output_type": "stream", "name": "stdout", "text": ["ok\n"]}],
                        "source": ["print('ok')"],
                    }
                ],
                "metadata": {},
                "nbformat": 4,
                "nbformat_minor": 5,
            }
            source.write_text(json.dumps(notebook), encoding="utf-8")
            prepare_notebook(source, output)
            validate_clean_notebook(output)
            cleaned = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual([], cleaned["cells"][0]["outputs"])
            self.assertIsNone(cleaned["cells"][0]["execution_count"])

    def test_local_absolute_path_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "source.ipynb"
            output = Path(directory) / "output.ipynb"
            notebook = {
                "cells": [
                    {
                        "cell_type": "code",
                        "execution_count": None,
                        "metadata": {},
                        "outputs": [],
                        "source": ["path = '/home/usuario/dados.csv'"],
                    }
                ],
                "metadata": {},
                "nbformat": 4,
                "nbformat_minor": 5,
            }
            source.write_text(json.dumps(notebook), encoding="utf-8")
            with self.assertRaisesRegex(NotebookSourceError, "caminho local absoluto"):
                prepare_notebook(source, output)
            self.assertFalse(output.exists())


if __name__ == "__main__":
    unittest.main()
