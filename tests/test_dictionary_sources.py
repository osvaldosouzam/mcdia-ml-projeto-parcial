from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_common.dictionary import DictionarySourceError, read_dictionary_source  # noqa: E402


class DictionarySourcesTest(unittest.TestCase):
    def test_expected_source_counts(self) -> None:
        raw = read_dictionary_source(ROOT / "sources/dicionario/base_bruta.csv")
        derived = read_dictionary_source(ROOT / "sources/dicionario/variaveis_derivadas.csv")
        self.assertEqual(25, len(raw))
        self.assertEqual(19, len(derived))

    def test_duplicate_variable_is_rejected(self) -> None:
        temporary = ROOT / "target/test_duplicate_dictionary.csv"
        temporary.parent.mkdir(parents=True, exist_ok=True)
        source = (ROOT / "sources/dicionario/base_bruta.csv").read_text(encoding="utf-8")
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
