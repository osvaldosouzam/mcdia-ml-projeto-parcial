from __future__ import annotations

import argparse
import json
import sys

from build_common.paths import EvaluationOnePaths
from build_common.validation import validate_evaluation_one


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Valida os entregáveis gerados.")
    parser.add_argument("--avaliacao", choices=("1", "2"), required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.avaliacao == "2":
        print("A validação da Avaliação 2 será habilitada quando seus entregáveis forem implementados.")
        return 2
    try:
        result = validate_evaluation_one(EvaluationOnePaths())
    except Exception as error:
        print(f"ERRO: validação da Avaliação 1 falhou: {error}", file=sys.stderr)
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
