from character_context import build_character_context
from character_understanding import build_character_understanding
from meaning_extraction import build_meaning_map
from structural_observation import build_structural_observation
from scenario_interpretation import build_scenario_interpretation
from loader import list_character_files, load_document, detect_document_type
from router import route

def load_character_package(character_name):
    print()
    print("=== Character Package Reader ===")
    print(f"Character: {character_name}")

    files = list_character_files(character_name)

    if not files:
        print("No documents found.")
        return

    for document in files:
        print()
        print(f"Loading Document: {document}")

        content = load_document(character_name, document)
        doc_type = detect_document_type(document)

        if content:
            print(f"Document Type: {doc_type}")
            route(doc_type, content)
        else:
            print("Failed to load document")

    context = build_character_context()

    print()
    print("Character Context")
    print(context)

    meaning_map = build_meaning_map(context)

    print()
    print("Meaning Map")
    print(meaning_map)

    understanding = build_character_understanding(meaning_map)

    print()
    print("Character Understanding")
    print(understanding)

    scenario = input("\nScenario > ")

    observation = build_structural_observation(
        understanding,
        scenario,
    )

    print()
    print("Structural Observation")
    print(observation)

    interpretation = build_scenario_interpretation(
        understanding,
        observation,
    )

    print()
    print("Scenario Interpretation")
    print(interpretation)

    print()
    print("=== Character Package Loaded ===")