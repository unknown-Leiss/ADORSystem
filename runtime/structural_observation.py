def build_structural_observation(understanding, recognition_organization):
    print()
    print("=== Structural Observation Runtime ===")

    entities = []
    relations = []
    actions = []
    attributes = []
    structures = []

    recognition_candidates = recognition_organization.get("accepted", [])

    def to_observed_item(candidate):
        chunk = candidate.get("candidate", {})
        chunk_type = chunk.get("type")

        return {
            "text": chunk.get("text"),
            "type": chunk_type,
            "kind": (
                chunk.get("entity_hint")
                or chunk.get("relation_hint")
                or chunk.get("action_hint")
                or chunk.get("attribute_hint")
                or chunk.get("structure_hint")
            ),
            "source_chunks": candidate.get("source_chunks", []),
            "confidence": candidate.get("confidence"),
        }

    for candidate in recognition_candidates:
        chunk = candidate.get("candidate", {})
        chunk_type = chunk.get("type")

        observed_item = to_observed_item(candidate)

        if chunk_type == "entity":
            entities.append(observed_item)
        elif chunk_type == "relation":
            relations.append(observed_item)
        elif chunk_type == "action":
            actions.append(observed_item)
        elif chunk_type == "attribute":
            attributes.append(observed_item)
        elif chunk_type == "structure":
            structures.append(observed_item)

    observation = {
        "character_understanding": understanding,
        "recognition_organization": recognition_organization,
        "entities": entities,
        "relations": relations,
        "actions": actions,
        "attributes": attributes,
        "structures": structures,
        "observation_order": [],
        "raw_structure": [],
        "observation_status": "provisional",
        "purpose": "Build observable structures from recognition candidates"
    }

    print("Structural Observation Ready")

    return observation