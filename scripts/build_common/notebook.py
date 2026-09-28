from __future__ import annotations

import copy
import json
import re
from pathlib import Path


class NotebookSourceError(ValueError):
    """Indica que o notebook não pode ser preparado para entrega."""


LOCAL_PATH_PATTERNS = (
    re.compile(r"/home/[^/]+/"),
    re.compile(r"[A-Za-z]:\\Users\\[^\\]+\\"),
)


def _load_notebook(path: Path) -> dict:
    if not path.is_file():
        raise NotebookSourceError(f"Notebook não encontrado: {path}")
    try:
        notebook = json.loads(path.read_text(encoding="utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise NotebookSourceError(f"Notebook inválido: {path}: {error}") from error
    if not isinstance(notebook.get("cells"), list) or not notebook["cells"]:
        raise NotebookSourceError(f"Notebook sem células: {path}")
    return notebook


def prepare_notebook(source: Path, output: Path) -> Path:
    notebook = copy.deepcopy(_load_notebook(source))
    for cell in notebook["cells"]:
        if cell.get("cell_type") == "code":
            cell["outputs"] = []
            cell["execution_count"] = None
        source_text = "".join(cell.get("source", []))
        for pattern in LOCAL_PATH_PATTERNS:
            if pattern.search(source_text):
                raise NotebookSourceError(
                    f"Notebook contém caminho local absoluto incompatível com a entrega: {pattern.pattern}"
                )
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(notebook, ensure_ascii=False, indent=1) + "\n",
        encoding="utf-8",
    )
    return output


def validate_clean_notebook(path: Path) -> None:
    notebook = _load_notebook(path)
    for index, cell in enumerate(notebook["cells"]):
        if cell.get("cell_type") != "code":
            continue
        if cell.get("outputs"):
            raise NotebookSourceError(f"Célula {index} contém outputs persistidos")
        if cell.get("execution_count") is not None:
            raise NotebookSourceError(f"Célula {index} contém contagem de execução")
