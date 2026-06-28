from recognition_engine import run_recognition_engine


def build_recognition_organization(surface_organization):
    print()
    print("=== Recognition Organization Runtime ===")

    organized_chunks = surface_organization.get("organized_chunks", [])
    chunk_relations = surface_organization.get("chunk_relations", [])

    recognition_candidates = run_recognition_engine(organized_chunks)

    recognition_organization = {
        "surface_organization": surface_organization,
        "recognition_candidates": recognition_candidates,
        "candidate_relations": chunk_relations,
        "organization_status": "provisional",
        "purpose": "Build recognition candidates before structural observation"
    }

    print("Recognition Organization Ready")

    return recognition_organization