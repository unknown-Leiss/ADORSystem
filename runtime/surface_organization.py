def build_surface_organization(surface_observation):
    print()
    print("=== Surface Organization Runtime ===")

    surface_chunks = surface_observation.get("surface_chunks", [])

    organized_chunks = []

    for chunk in surface_chunks:
        organized_chunks.append({
            "text": chunk,
            "type": "unknown"
        })

    chunk_relations = []

    for index in range(len(organized_chunks) - 1):
        chunk_relations.append({
            "from": index,
            "to": index + 1,
            "relation": "adjacent"
        })

    surface_organization = {
        "surface_observation": surface_observation,
        "organized_chunks": organized_chunks,
        "chunk_relations": chunk_relations,
        "organization_status": "provisional",
        "purpose": "Organize surface fragments before structural observation"
    }

    print("Surface Organization Ready")

    return surface_organization