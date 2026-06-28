from recognition_rules import build_particle_connection_candidate


def apply_particle_module(organized_chunks):
    candidates = []
    index = 0

    while index < len(organized_chunks):
        candidate = build_particle_connection_candidate(
            organized_chunks,
            index,
        )

        if candidate:
            candidates.append(candidate)
            index = candidate["next_index"]
            continue

        index += 1

    return candidates