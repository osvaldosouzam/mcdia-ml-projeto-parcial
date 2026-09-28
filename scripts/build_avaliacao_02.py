from __future__ import annotations

import sys
from pathlib import Path

from build_common.paths import PROJECT_ROOT


REQUIRED_SOURCES = (
    PROJECT_ROOT / "notebooks/avaliacao_02/lucimar_nascimento_atividade_2.ipynb",
    PROJECT_ROOT / "sources/avaliacao_02/metodologia.md",
    PROJECT_ROOT / "sources/avaliacao_02/resultados.md",
    PROJECT_ROOT / "sources/avaliacao_02/discussao.md",
    PROJECT_ROOT / "sources/avaliacao_02/conclusao.md",
)


def missing_sources() -> list[Path]:
    return [path for path in REQUIRED_SOURCES if not path.is_file()]


def main() -> int:
    missing = missing_sources()
    if missing:
        print(
            "A infraestrutura da Avaliação 2 está preparada, mas o conteúdo ainda não foi implementado.",
            file=sys.stderr,
        )
        print("Fontes pendentes:", file=sys.stderr)
        for path in missing:
            print(f"- {path.relative_to(PROJECT_ROOT)}", file=sys.stderr)
        return 2
    print(
        "As fontes da Avaliação 2 foram encontradas, mas a geração final será implementada na issue correspondente.",
        file=sys.stderr,
    )
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
