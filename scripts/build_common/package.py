from __future__ import annotations

import shutil
import zipfile
from pathlib import Path


class PackageError(ValueError):
    """Indica que a base ou o pacote final é inválido."""


def reset_output_dir(output_dir: Path, target_root: Path) -> None:
    resolved_output = output_dir.resolve()
    resolved_target = target_root.resolve()
    if resolved_target not in resolved_output.parents:
        raise PackageError(f"Recusa em limpar diretório fora de target/: {resolved_output}")
    if resolved_output.exists():
        shutil.rmtree(resolved_output)
    resolved_output.mkdir(parents=True, exist_ok=True)


def validate_data_zip(path: Path) -> str:
    if not path.is_file() or path.stat().st_size == 0:
        raise PackageError(f"Base compactada ausente ou vazia: {path}")
    try:
        with zipfile.ZipFile(path) as archive:
            files = [item for item in archive.infolist() if not item.is_dir()]
            csv_files = [item for item in files if item.filename.lower().endswith(".csv")]
            if len(files) != 1 or len(csv_files) != 1:
                raise PackageError(
                    f"O ZIP deve conter exatamente um CSV. Conteúdo: {[item.filename for item in files]}"
                )
            if csv_files[0].file_size == 0:
                raise PackageError("O CSV contido no ZIP está vazio")
            return csv_files[0].filename
    except zipfile.BadZipFile as error:
        raise PackageError(f"Arquivo ZIP inválido: {path}") from error


def copy_data_zip(source: Path, output: Path) -> Path:
    validate_data_zip(source)
    output.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, output)
    return output


def validate_required_outputs(paths: tuple[Path, ...]) -> None:
    missing = [str(path) for path in paths if not path.is_file() or path.stat().st_size == 0]
    if missing:
        raise PackageError(f"Outputs ausentes ou vazios: {missing}")
