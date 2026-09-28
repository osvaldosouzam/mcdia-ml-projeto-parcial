from __future__ import annotations

from pathlib import Path

from .dictionary import read_dictionary_source, validate_dictionary
from .notebook import validate_clean_notebook
from .package import validate_data_zip, validate_required_outputs
from .paths import EvaluationOnePaths
from .report import validate_report


def validate_evaluation_one(paths: EvaluationOnePaths) -> dict[str, object]:
    base_rows = read_dictionary_source(paths.base_dictionary_source)
    analytical_rows = read_dictionary_source(paths.analytical_dictionary_source)
    validate_dictionary(paths.dictionary_output, len(base_rows))
    validate_report(paths.report_output)
    validate_clean_notebook(paths.notebook_output)
    csv_member = validate_data_zip(paths.data_output)
    validate_required_outputs(paths.required_outputs)
    return {
        "base_dictionary_variables": len(base_rows),
        "internal_analytical_variables": len(analytical_rows),
        "data_csv_member": csv_member,
        "outputs": [str(path) for path in paths.required_outputs],
    }
