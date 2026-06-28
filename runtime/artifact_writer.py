

import json
from datetime import datetime
from pathlib import Path
from typing import Any


ARTIFACT_DIR = Path(__file__).resolve().parent / "artifacts"


def ensure_artifact_dir() -> Path:
    """Ensure the runtime artifacts directory exists."""
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    return ARTIFACT_DIR


def write_artifact(name: str, data: Any) -> Path:
    """
    Write a runtime artifact as JSON.

    Args:
        name: Artifact filename without extension, or with .json.
        data: JSON-serializable runtime output.

    Returns:
        Path to the written artifact file.
    """
    artifact_dir = ensure_artifact_dir()
    filename = name if name.endswith(".json") else f"{name}.json"
    output_path = artifact_dir / filename

    payload = {
        "artifact_name": filename,
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "artifact_status": "provisional",
        "data": data,
    }

    with output_path.open("w", encoding="utf-8") as file:
        json.dump(payload, file, ensure_ascii=False, indent=2)

    print(f"Artifact Written: {output_path}")
    return output_path


def write_runtime_artifacts(**artifacts: Any) -> dict[str, str]:
    """
    Write multiple named runtime artifacts.

    Example:
        write_runtime_artifacts(
            operational_intent=operational_intent,
            scenario_interpretation=interpretation,
        )
    """
    written_paths: dict[str, str] = {}

    for name, data in artifacts.items():
        if data is None:
            continue
        path = write_artifact(name, data)
        written_paths[name] = str(path)

    return written_paths