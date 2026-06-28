def build_recognition_resolution(recognition_organization):
    print()
    print("=== Recognition Resolution Runtime ===")

    candidates = recognition_organization.get("recognition_candidates", [])

    accepted = []
    held = []
    rejected = []

    candidates_by_source = {}

    for candidate in candidates:
        source_key = tuple(candidate.get("source_chunks", []))
        candidates_by_source.setdefault(source_key, []).append(candidate)

    for source_key, grouped_candidates in candidates_by_source.items():
        best_candidate = select_best_candidate(grouped_candidates)

        for candidate in grouped_candidates:
            if candidate is best_candidate:
                if candidate.get("confidence") == "medium":
                    accepted.append(candidate)
                else:
                    held.append(candidate)
            else:
                held.append(candidate)

    resolved = {
        "accepted": accepted,
        "held": held,
        "rejected": rejected,
        "resolution_status": "provisional",
        "purpose": "Resolve recognition candidates before structural observation"
    }

    print("Recognition Resolution Ready")

    return resolved


def select_best_candidate(candidates):
    priority = {
        "action": 4,
        "attribute": 3,
        "relation": 2,
        "unknown": 1,
        "compound": 0,
    }

    best_candidate = candidates[0]
    best_score = get_candidate_score(best_candidate, priority)

    for candidate in candidates[1:]:
        score = get_candidate_score(candidate, priority)

        if score > best_score:
            best_candidate = candidate
            best_score = score

    return best_candidate


def get_candidate_score(candidate, priority):
    candidate_body = candidate.get("candidate", {})
    candidate_type = candidate_body.get("type", "unknown")
    confidence = candidate.get("confidence")

    confidence_score = 1 if confidence == "medium" else 0
    type_score = priority.get(candidate_type, 0)

    return (confidence_score, type_score)


# === Structural Observation Runtime ===
def build_structural_observation(recognition_resolution):
    print()
    print("=== Structural Observation Runtime ===")

    accepted = recognition_resolution.get("accepted", [])
    held = recognition_resolution.get("held", [])

    structural_units = {
        "entities": [],
        "actions": [],
        "relations": [],
        "attributes": [],
        "structures": [],
        "held": held,
        "observation_status": "provisional",
        "purpose": "Reconstruct Japanese input as structural observation units, not word enumeration"
    }

    for candidate in accepted:
        candidate_body = candidate.get("candidate", {})
        candidate_type = candidate_body.get("type", "unknown")
        value = candidate_body.get("value")

        observation_unit = build_observation_unit(candidate)

        if not value:
            structural_units["held"].append(candidate)
            continue

        if candidate_type == "entity":
            structural_units["entities"].append(observation_unit)
        elif candidate_type == "action":
            structural_units["actions"].append(observation_unit)
        elif candidate_type == "relation":
            structural_units["relations"].append(observation_unit)
        elif candidate_type == "attribute":
            structural_units["attributes"].append(observation_unit)
        elif candidate_type == "structure":
            structural_units["structures"].append(observation_unit)
        else:
            structural_units["held"].append(candidate)

    structural_units["summary"] = build_structural_summary(structural_units)

    print("Structural Observation Ready")

    return structural_units


def build_observation_unit(candidate):
    candidate_body = candidate.get("candidate", {})

    return {
        "type": candidate_body.get("type", "unknown"),
        "value": candidate_body.get("value"),
        "source_chunks": candidate.get("source_chunks", []),
        "confidence": candidate.get("confidence"),
        "reason": candidate.get("reason")
    }


def build_structural_summary(structural_units):
    return {
        "entity_count": len(structural_units.get("entities", [])),
        "action_count": len(structural_units.get("actions", [])),
        "relation_count": len(structural_units.get("relations", [])),
        "attribute_count": len(structural_units.get("attributes", [])),
        "structure_count": len(structural_units.get("structures", [])),
        "held_count": len(structural_units.get("held", []))
    }