def build_structural_observation(understanding, recognition_organization):
    print()
    print("=== Structural Observation Runtime ===")

    entities = []
    relations = []
    actions = []
    attributes = []

    recognition_candidates = recognition_organization.get("recognition_candidates", [])

    for candidate in recognition_candidates:
        chunk = candidate.get("candidate", {})
        chunk_type = chunk.get("type")

        if chunk_type == "entity":
            entities.append(candidate)
        elif chunk_type == "relation":
            relations.append(candidate)
        elif chunk_type == "action":
            actions.append(candidate)
        elif chunk_type == "attribute":
            attributes.append(candidate)

    observation = {
        "character_understanding": understanding,
        "recognition_organization": recognition_organization,
        "entities": entities,
        "relations": relations,
        "actions": actions,
        "attributes": attributes,
        "observation_order": [],
        "raw_structure": [],
        "observation_status": "provisional",
        "purpose": "Build observable structures from recognition candidates"
    }

    print("Structural Observation Ready")

    return observation