from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_common.report import ReportSourceError, expand_markdown  # noqa: E402


class ReportSourcesTest(unittest.TestCase):
    def test_partial_report_resolves_all_sections(self) -> None:
        markdown = expand_markdown(
            ROOT / "sources/avaliacao_01/relatorio_parcial.md",
            ROOT / "sources",
        )
        for section in (
            "## 1. Introdução",
            "## 2. Objetivos",
            "## 3. Referencial Teórico",
            "## 4. Referências",
        ):
            self.assertIn(section, markdown)
        self.assertNotIn("{{ include", markdown)

    def test_missing_include_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            sources = Path(directory) / "sources"
            sources.mkdir()
            report = sources / "report.md"
            report.write_text("{{ include ausente.md }}\n", encoding="utf-8")
            with self.assertRaisesRegex(ReportSourceError, "não encontrada"):
                expand_markdown(report, sources)


if __name__ == "__main__":
    unittest.main()
