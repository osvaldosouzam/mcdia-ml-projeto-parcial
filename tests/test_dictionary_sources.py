from __future__ import annotations

import sys
import tempfile
import unittest
import zipfile
import csv
import io
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_common.dictionary import DictionarySourceError, read_dictionary_source  # noqa: E402


class DictionarySourcesTest(unittest.TestCase):
    def test_expected_source_counts(self) -> None:
        base = read_dictionary_source(ROOT / "sources/dicionario/base_consolidada.csv")
        analytical = read_dictionary_source(ROOT / "sources/dicionario/variaveis_analiticas.csv")
        self.assertEqual(25, len(base))
        self.assertEqual(20, len(analytical))
        self.assertIn("codigo_faixa_atraso", {row["Variável"] for row in analytical})

    def test_base_dictionary_matches_the_csv_header(self) -> None:
        dictionary = read_dictionary_source(ROOT / "sources/dicionario/base_consolidada.csv")
        dictionary_names = [row["Variável"] for row in dictionary]
        archive_path = ROOT / "data/raw/base_lucimar_nascimento_v2.zip"
        with zipfile.ZipFile(archive_path) as archive:
            csv_names = [name for name in archive.namelist() if name.lower().endswith(".csv")]
            self.assertEqual(["base_lucimar_nascimento_v2.csv"], csv_names)
            with archive.open(csv_names[0]) as raw:
                text = io.TextIOWrapper(raw, encoding="utf-8-sig", newline="")
                csv_header = next(csv.reader(text))
        self.assertEqual(csv_header, dictionary_names)

    def test_duplicate_variable_is_rejected(self) -> None:
        temporary = ROOT / "target/test_duplicate_dictionary.csv"
        temporary.parent.mkdir(parents=True, exist_ok=True)
        source = (ROOT / "sources/dicionario/base_consolidada.csv").read_text(encoding="utf-8")
        lines = source.splitlines()
        temporary.write_text("\n".join([*lines, lines[1]]) + "\n", encoding="utf-8")
        try:
            with self.assertRaises(DictionarySourceError):
                read_dictionary_source(temporary)
        finally:
            temporary.unlink(missing_ok=True)

    def test_invalid_header_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "invalid.csv"
            source.write_text("Variavel,Descricao\ncoluna,Texto\n", encoding="utf-8")
            with self.assertRaisesRegex(DictionarySourceError, "Cabeçalho inválido"):
                read_dictionary_source(source)


if __name__ == "__main__":
    unittest.main()
