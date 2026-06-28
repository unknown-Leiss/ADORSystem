from character_context import build_character_context
from character_understanding import build_character_understanding
from meaning_extraction import build_meaning_map
from token_observation import build_token_observation
from surface_organization import build_surface_organization
from recognition_organization import build_recognition_organization
from recognition_resolution import build_recognition_resolution
from structural_observation import build_structural_observation
from structural_organization import run_structural_organization
from meaning_reconstruction import run_meaning_reconstruction
from meaning_verification import run_meaning_verification
from meaning_expansion import run_meaning_expansion
from operational_intent import run_operational_intent
from scenario_interpretation import build_scenario_interpretation
from loader import list_character_files, load_document, detect_document_type
from router import route

DEBUG_VERBOSE = False


def print_runtime_output(title, data):
    print()
    print(title)

    if DEBUG_VERBOSE:
        print(data)
        return

    if not isinstance(data, dict):
        print(data)
        return

    print_compact_summary(title, data)


def print_compact_summary(title, data):
    print(f"keys: {list(data.keys())}")

    if title == "Character Context":
        for layer_name, layer_data in data.items():
            if isinstance(layer_data, dict):
                print(f"- {layer_name}: {layer_data.get('document_title')}")

    elif title == "Character Understanding":
        print(f"available_sources: {data.get('available_sources')}")
        print(f"missing_sources: {data.get('missing_sources')}")
        print(f"ready_for_scenario: {data.get('ready_for_scenario')}")

    elif title == "Recognition Organization":
        candidates = data.get("recognition_candidates", [])
        print(f"recognition_candidates: {len(candidates)}")

    elif title == "Recognition Resolution":
        print(f"accepted: {len(data.get('accepted', []))}")
        print(f"held: {len(data.get('held', []))}")
        print(f"rejected: {len(data.get('rejected', []))}")

    elif title == "Structural Observation":
        print(f"entities: {extract_texts(data.get('entities', []))}")
        print(f"actions: {extract_texts(data.get('actions', []))}")
        print(f"attributes: {extract_texts(data.get('attributes', []))}")
        print(f"structures: {extract_texts(data.get('structures', []))}")

    elif title == "Structural Organization":
        print(f"existence_structure: {extract_texts(data.get('existence_structure', []))}")
        behavior = data.get("behavior_structure", {})
        print(f"behavior_actions: {extract_texts(behavior.get('actions', []))}")
        print(f"behavior_attributes: {extract_texts(behavior.get('attributes', []))}")
        print(f"context_structure: {extract_texts(data.get('context_structure', []))}")

    elif title == "Meaning Reconstruction":
        scene_meaning = data.get("scene_meaning", {})
        print(f"subject: {extract_text(scene_meaning.get('subject'))}")
        print(f"main_action: {extract_text(scene_meaning.get('main_action'))}")
        print(f"mood: {extract_text(scene_meaning.get('mood'))}")
        print(f"context: {extract_text(scene_meaning.get('context'))}")

    elif title == "Meaning Verification":
        print(f"verification_status: {data.get('verification_status')}")
        print(f"ready_for_expansion: {data.get('ready_for_expansion')}")

    elif title == "Meaning Expansion":
        print(f"expanded_subject: {extract_text(data.get('expanded_subject'))}")
        print(f"expanded_action: {extract_text(data.get('expanded_action'))}")
        print(f"expanded_mood: {extract_text(data.get('expanded_mood'))}")
        print(f"expanded_context: {extract_text(data.get('expanded_context'))}")
        print(f"ready_for_operational_intent: {data.get('ready_for_operational_intent')}")

    elif title == "Operational Intent":
        intent_focus = data.get("intent_focus", {})
        behavior_intent = data.get("behavior_intent", {})
        presence_intent = data.get("presence_intent", {})
        context_intent = data.get("context_intent", {})
        print(f"subject: {intent_focus.get('subject')}")
        print(f"main_behavior: {intent_focus.get('main_behavior')}")
        print(f"context_condition: {intent_focus.get('context_condition')}")
        print(f"body_state: {behavior_intent.get('body_state')}")
        print(f"presence_direction: {presence_intent.get('presence_direction')}")
        print(f"presence_intensity: {presence_intent.get('presence_intensity')}")
        print(f"viewing_condition: {context_intent.get('viewing_condition')}")
        print(f"ready_for_scenario_interpretation: {data.get('ready_for_scenario_interpretation')}")

    elif title == "Scenario Interpretation":
        print(f"interpretation_status: {data.get('interpretation_status')}")
        print(f"purpose: {data.get('purpose')}")


def extract_text(item):
    if isinstance(item, dict):
        return item.get("text")
    return None


def extract_texts(items):
    texts = []

    for item in items:
        if isinstance(item, dict):
            texts.append(item.get("text"))

    return texts

def load_character_package(character_name):
    print()
    print("=== Character Package Reader ===")
    print(f"Character: {character_name}")

    files = list_character_files(character_name)

    if not files:
        print("No documents found.")
        return

    for document in files:
        if ".original-before-anchor" in document:
            print()
            print(f"Skipping Backup Document: {document}")
            continue

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
    print_runtime_output("Character Context", context)

    meaning_map = build_meaning_map(context)
    print_runtime_output("Meaning Map", meaning_map)

    understanding = build_character_understanding(meaning_map)
    print_runtime_output("Character Understanding", understanding)

    scenario = input("\nScenario > ")
    token_observation = build_token_observation(scenario)
    print_runtime_output("Token Observation", token_observation)

    surface_organization = build_surface_organization(
        token_observation,
    )
    print_runtime_output("Surface Organization", surface_organization)

    recognition_organization = build_recognition_organization(
        surface_organization,
    )
    print_runtime_output("Recognition Organization", recognition_organization)

    recognition_resolution = build_recognition_resolution(
        recognition_organization,
    )
    print_runtime_output("Recognition Resolution", recognition_resolution)

    observation = build_structural_observation(
        understanding,
        recognition_resolution,
    )
    print_runtime_output("Structural Observation", observation)

    structural_organization = run_structural_organization(
        observation,
    )
    print_runtime_output("Structural Organization", structural_organization)

    meaning_reconstruction = run_meaning_reconstruction(
        structural_organization,
    )
    print_runtime_output("Meaning Reconstruction", meaning_reconstruction)

    meaning_verification = run_meaning_verification(
        meaning_reconstruction,
    )
    print_runtime_output("Meaning Verification", meaning_verification)

    meaning_expansion = run_meaning_expansion(
        meaning_verification,
    )
    print_runtime_output("Meaning Expansion", meaning_expansion)

    operational_intent = run_operational_intent(
        meaning_expansion,
    )
    print_runtime_output("Operational Intent", operational_intent)

    interpretation = build_scenario_interpretation(
        understanding,
        operational_intent,
    )
    print_runtime_output("Scenario Interpretation", interpretation)

    print()
    print("=== Character Package Loaded ===")