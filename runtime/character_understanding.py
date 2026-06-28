def build_character_understanding(meaning_map):
    print()
    print("=== Character Understanding Runtime ===")

    required_sources = [
        "identity",
        "behavior",
        "recognition",
        "verification",
        "reconstruction",
    ]

    available_sources = []
    missing_sources = []

    for source in required_sources:
        source_data = meaning_map.get(f"{source}_meaning", {}).get("source")

        if source_data and source_data.get("document_title"):
            available_sources.append(source)
        else:
            missing_sources.append(source)

    understanding = {
        "identity_source": meaning_map.get("identity_meaning"),
        "behavior_source": meaning_map.get("behavior_meaning"),
        "recognition_source": meaning_map.get("recognition_meaning"),
        "verification_source": meaning_map.get("verification_meaning"),
        "reconstruction_source": meaning_map.get("reconstruction_meaning"),
        "available_sources": available_sources,
        "missing_sources": missing_sources,
        "ready_for_scenario": len(missing_sources) == 0,
        "understanding_status": "provisional",
        "purpose": "Prepare AI recognition state before scenario interpretation",
    }

    print("Available Sources:", available_sources)
    print("Missing Sources:", missing_sources)
    print("Ready for Scenario:", understanding["ready_for_scenario"])
    print("Character Understanding Ready")

    return understanding