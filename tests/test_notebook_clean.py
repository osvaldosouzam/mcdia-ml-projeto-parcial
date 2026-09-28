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
