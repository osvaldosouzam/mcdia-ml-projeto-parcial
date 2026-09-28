from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]


@dataclass(frozen=True)
class EvaluationOnePaths:
    root: Path = PROJECT_ROOT

    @property
    def base_dictionary_source(self) -> Path:
        return self.root / "sources/dicionario/base_consolidada.csv"

    @property
    def analytical_dictionary_source(self) -> Path:
        return self.root / "sources/dicionario/variaveis_analiticas.csv"

    @property
    def report_source(self) -> Path:
        return self.root / "sources/avaliacao_01/relatorio_parcial.md"

    @property
    def report_template(self) -> Path:
        return self.root / "templates/relatorio_institucional.docx"

    @property
    def notebook_source(self) -> Path:
        return self.root / "notebooks/avaliacao_01/lucimar_oliveira_do_nascimento.ipynb"

    @property
    def data_source(self) -> Path:
        return self.root / "data/raw/base_lucimar_nascimento_v2.zip"

    @property
    def output_dir(self) -> Path:
        return self.root / "target/avaliacao_01"

    @property
    def dictionary_output(self) -> Path:
        return self.output_dir / "dicionario_lucimar_oliveira_do_nascimento.xlsx"

    @property
    def report_output(self) -> Path:
        return self.output_dir / "relatorio_parcial_lucimar_oliveira_do_nascimento.docx"

    @property
    def notebook_output(self) -> Path:
        return self.output_dir / "lucimar_oliveira_do_nascimento.ipynb"

    @property
    def data_output(self) -> Path:
        return self.output_dir / "base_lucimar_oliveira_do_nascimento.zip"

    @property
    def required_outputs(self) -> tuple[Path, ...]:
        return (
            self.notebook_output,
            self.dictionary_output,
            self.data_output,
            self.report_output,
        )
