from __future__ import annotations

import json
import sys

from build_common.dictionary import build_dictionary
from build_common.notebook import prepare_notebook
from build_common.package import copy_data_zip, reset_output_dir
from build_common.paths import EvaluationOnePaths
from build_common.report import build_report
from build_common.validation import validate_evaluation_one


def build() -> dict[str, object]:
    paths = EvaluationOnePaths()
    reset_output_dir(paths.output_dir, paths.root / "target")
    build_dictionary(
        paths.base_dictionary_source,
        paths.dictionary_output,
    )
    build_report(
        paths.report_source,
        paths.report_template,
        paths.report_output,
        paths.root / "sources",
    )
    prepare_notebook(paths.notebook_source, paths.notebook_output)
    copy_data_zip(paths.data_source, paths.data_output)
    return validate_evaluation_one(paths)


def main() -> int:
    try:
        result = build()
    except Exception as error:
        print(f"ERRO: não foi possível gerar a Avaliação 1: {error}", file=sys.stderr)
        return 1
    print("Avaliação 1 gerada e validada com sucesso.")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
