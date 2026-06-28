from layer_runtime import runtime_state


def build_character_context():
    print()
    print("=== Character Context Builder ===")

    context = {
        "identity": runtime_state.get("identity"),
        "behavior": runtime_state.get("behavior"),
        "recognition": runtime_state.get("recognition"),
        "verification": runtime_state.get("verification"),
        "reconstruction": runtime_state.get("reconstruction"),
    }

    print("Character Context Ready")

    return context