from package_reader import load_character_package
from recognition_resolution import build_structural_observation
from reconstruction_brief import (
    build_reconstruction_brief,
    format_reconstruction_brief,
)

from loader import (
    bootstrap,
    list_characters,
)


def show_menu():
    print("ADOR Runtime Controller")
    print()
    print("Select Operation:")
    print("1. LLM Distortion")
    print("2. Reconstruction")
    return input("> ").strip().translate(str.maketrans("１２", "12"))


def run_llm_distortion():
    print("LLM Distortion Mode")
    print("Not implemented yet.")


def run_reconstruction():
    print("Reconstruction Mode")

    bootstrap()

    chars = list_characters()

    if not chars:
        print("No character packages found.")
        return None

    print()
    print("Characters:")

    for i, name in enumerate(chars, start=1):
        print(f"{i}. {name}")

    print()
    char_choice = input("Select Character > ").strip().translate(str.maketrans("１２３４５６７８９０", "1234567890"))
    if not char_choice.isdigit():
        print("Invalid Selection")
        return None

    index = int(char_choice) - 1

    if not 0 <= index < len(chars):
        print("Invalid Selection")
        return None

    selected = chars[index]
    print(f"Loading: {selected}")
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