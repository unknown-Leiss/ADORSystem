from character_context import build_character_context
from character_understanding import build_character_understanding
from meaning_extraction import build_meaning_map
from token_observation import build_token_observation
from surface_organization import build_surface_organization
from recognition_organization import build_recognition_organization
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

    token_observation = build_token_observation(scenario)

    print()
    print("Token Observation")
    print(token_observation)

    surface_organization = build_surface_organization(
        token_observation,
    )

    print()
    print("Surface Organization")
    print(surface_organization)

    recognition_organization = build_recognition_organization(
        surface_organization,
    )

    print()
    print("Recognition Organization")
    print(recognition_organization)

    observation = build_structural_observation(
        understanding,
        recognition_organization,
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