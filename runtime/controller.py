from pathlib import Path
from package_reader import load_character_package
from recognition_resolution import build_structural_observation
from reconstruction_brief import (
    build_reconstruction_brief,
    format_reconstruction_brief,
)

from distortion_brief import (
    build_distortion_brief,
    format_distortion_brief,
)

from loader import (
    bootstrap,
    list_characters,
)


# Helper functions for printing markdown files
RUNTIME_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = RUNTIME_DIR.parent


def _print_markdown_files_full_text(section_title, folder_name):
    folder_path = PROJECT_ROOT / folder_name

    print()
    print(f"=== {section_title} ===")

    if not folder_path.exists():
        print(f"Missing folder: {folder_name}")
        return

    markdown_files = sorted(folder_path.glob("*.md"))

    if not markdown_files:
        print(f"No markdown files found in: {folder_name}")
        return

    for markdown_file in markdown_files:
        print()
        print(f"--- {markdown_file.name} ---")
        print()

        try:
            content = markdown_file.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            content = markdown_file.read_text(encoding="utf-8-sig")

        print(content)


def print_llm_distortion_information_sources():
    _print_markdown_files_full_text("T1 Definition Full Text", "T1_Definition")
    _print_markdown_files_full_text("T2 Runtime Full Text", "T2_Runtime")


def show_menu():
    print("Exrela Runtime Controller")
    print()
    print("Select Operation:")
    print("1. LLM Distortion")
    print("2. Reconstruction")
    return input("> ").strip().translate(str.maketrans("１２", "12"))


def run_llm_distortion():
    print("LLM Distortion Mode")
    print()
    print("Loading Exrela Runtime Information Sources...")

    bootstrap_status = bootstrap()

    print_llm_distortion_information_sources()

    brief = build_distortion_brief(bootstrap_status)

    print()
    print(format_distortion_brief(brief))

    return brief


def run_reconstruction():
    print("Reconstruction Mode")

    bootstrap()

    chars = list_characters()

    if not chars:
        print("No recognition packages found.")
        return None

    print()
    print("Recognition Packages:")

    for i, name in enumerate(chars, start=1):
        print(f"{i}. {name}")

    print()
    char_choice = input("Select Recognition Package > ").strip().translate(str.maketrans("１２３４５６７８９０", "1234567890"))
    if not char_choice.isdigit():
        print("Invalid Selection")
        return None

    index = int(char_choice) - 1

    if not 0 <= index < len(chars):
        print("Invalid Selection")
        return None

    selected = chars[index]
    print(f"Loading Recognition Package: {selected}")
    runtime_result = load_character_package(selected)

    if not isinstance(runtime_result, dict):
        print("Runtime result was not returned as a dictionary.")
        return None

    recognition_resolution = runtime_result.get("recognition_resolution")

    if isinstance(recognition_resolution, dict):
        structural_observation = build_structural_observation(recognition_resolution)
        runtime_result["structural_observation"] = structural_observation

        print()
        print("=== Structural Observation Summary ===")
        print(structural_observation.get("summary", {}))

    brief = build_reconstruction_brief(runtime_result)
    runtime_result["reconstruction_brief"] = brief

    print()
    print(format_reconstruction_brief(brief))

    return runtime_result


def main():
    choice = show_menu()

    if choice == "1":
        run_llm_distortion()
    elif choice == "2":
        run_reconstruction()
    else:
        print("Unknown Mode")


if __name__ == "__main__":
    main()