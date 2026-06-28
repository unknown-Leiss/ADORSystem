def build_meaning_map(character_context):
    print()
    print("=== Meaning Extraction Runtime ===")

    identity = character_context.get("identity")
    behavior = character_context.get("behavior")
    recognition = character_context.get("recognition")
    verification = character_context.get("verification")
    reconstruction = character_context.get("reconstruction")

    meaning_map = {
        "identity_meaning": {
            "source": identity,
            "meaning_status": "provisional",
        },
        "behavior_meaning": {
            "source": behavior,
            "meaning_status": "provisional",
        },
        "recognition_meaning": {
            "source": recognition,
            "meaning_status": "provisional",
        },
        "verification_meaning": {
            "source": verification,
            "meaning_status": "provisional",
        },
        "reconstruction_meaning": {
            "source": reconstruction,
            "meaning_status": "provisional",
        },
        "runtime_role": "Extract meaning from Character Context before Scenario Interpretation",
    }

    print("Meaning Map Ready")

    return meaning_map