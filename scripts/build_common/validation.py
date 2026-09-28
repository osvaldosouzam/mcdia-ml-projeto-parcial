from __future__ import annotations

from pathlib import Path

from .dictionary import read_dictionary_source, validate_dictionary
from .notebook import validate_clean_notebook
from .package import validate_data_zip, validate_required_outputs
from .paths import EvaluationOnePaths
from .report import validate_report


def validate_evaluation_one(paths: EvaluationOnePaths) -> dict[str, object]:
    raw_rows = read_dictionary_source(paths.raw_dictionary_source)
    derived_rows = read_dictionary_source(paths.derived_dictionary_source)
    validate_dictionary(paths.dictionary_output, (len(raw_rows), len(derived_rows)))
    validate_report(paths.report_output)
    validate_clean_notebook(paths.notebook_output)
    csv_member = validate_data_zip(paths.data_output)
    validate_required_outputs(paths.required_outputs)
    return {
        "raw_dictionary_variables": len(raw_rows),
        "derived_dictionary_variables": len(derived_rows),
        "data_csv_member": csv_member,
        "outputs": [str(path) for path in paths.required_outputs],
    }
