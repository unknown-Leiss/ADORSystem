

def apply_recognition_rules(organized_chunks):
    recognition_candidates = []
    index = 0

    while index < len(organized_chunks):
        candidate = build_particle_connection_candidate(
            organized_chunks,
            index,
        )

        if candidate:
            recognition_candidates.append({
                "id": len(recognition_candidates),
                **candidate,
            })
            index = candidate["next_index"]
            continue

        recognition_candidates.append({
            "id": len(recognition_candidates),
            "candidate": organized_chunks[index],
            "source_chunks": [index],
            "status": "candidate",
            "confidence": "unknown"
        })

        index += 1

    return recognition_candidates


def build_particle_connection_candidate(organized_chunks, index):
    if index + 2 >= len(organized_chunks):
        return None

    left = organized_chunks[index]
    particle = organized_chunks[index + 1]
    right = organized_chunks[index + 2]

    particle_text = particle.get("text")

    particle_relation_map = {
        "の": "modifier",
        "から": "origin",
        "へ": "direction",
        "に": "location_or_target",
        "で": "place_or_means",
        "を": "object",
        "と": "with_or_relation",
    }

    if particle_text not in particle_relation_map:
        return None

    merged_text = (
        left.get("text", "")
        + particle.get("text", "")
        + right.get("text", "")
    )

    return {
        "candidate": {
            "text": merged_text,
            "type": "unknown",
            "relation_hint": particle_relation_map[particle_text]
        },
        "source_chunks": [index, index + 1, index + 2],
        "status": "candidate",
        "confidence": "low",
        "next_index": index + 3,
    }