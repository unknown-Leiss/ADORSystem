def build_recognition_organization(surface_organization):
    print()
    print("=== Recognition Organization Runtime ===")

    recognition_candidates = []

    organized_chunks = surface_organization.get("organized_chunks", [])
    chunk_relations = surface_organization.get("chunk_relations", [])

    for index, chunk in enumerate(organized_chunks):
        recognition_candidates.append({
            "id": index,
            "candidate": chunk,
            "status": "candidate",
            "confidence": "unknown"
        })

    recognition_organization = {
        "surface_organization": surface_organization,
        "recognition_candidates": recognition_candidates,
        "candidate_relations": chunk_relations,
        "organization_status": "provisional",
        "purpose": "Build recognition candidates before structural observation"
    }

    print("Recognition Organization Ready")

    return recognition_organization