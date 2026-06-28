def build_structural_observation(understanding, scenario):

    print()
    print("=== Structural Observation Runtime ===")

    observation = {
        "character_understanding": understanding,
        "scenario": scenario,

        "entities": [],
        "relations": [],
        "actions": [],
        "attributes": [],
        "observation_order": [],
        "raw_structure": [],

        "observation_status": "provisional",
        "purpose": "Disassemble scenario into observable structures"
    }

    print("Structural Observation Ready")

    return observation