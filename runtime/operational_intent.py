

def run_operational_intent(meaning_expansion):
    print()
    print("=== Operational Intent Runtime ===")

    operational_intent = {
        "meaning_expansion": meaning_expansion,
        "intent_focus": build_intent_focus(meaning_expansion),
        "behavior_intent": build_behavior_intent(meaning_expansion),
        "presence_intent": build_presence_intent(meaning_expansion),
        "context_intent": build_context_intent(meaning_expansion),
        "intent_status": "provisional",
        "ready_for_scenario_interpretation": True,
        "purpose": "Convert expanded meaning into operational intent before Scenario Interpretation",
    }

    print("Operational Intent Ready")

    return operational_intent


def build_intent_focus(meaning_expansion):
    subject = meaning_expansion.get("expanded_subject", {})
    action = meaning_expansion.get("expanded_action", {})
    context = meaning_expansion.get("expanded_context", {})

    return {
        "subject": subject.get("text"),
        "main_behavior": action.get("behavior_interpretation"),
        "context_condition": context.get("spatial_meaning"),
        "priority": [
            "preserve identity source",
            "prioritize observation",
            "support quiet presence",
            "keep environment meaningful",
        ],
    }


def build_behavior_intent(meaning_expansion):
    action = meaning_expansion.get("expanded_action", {})

    return {
        "behavior_role": action.get("behavior_role"),
        "behavior_interpretation": action.get("behavior_interpretation"),
        "gaze_structure": action.get("gaze_structure"),
        "body_state": action.get("body_state"),
        "operational_notes": action.get("operational_notes", []),
    }


def build_presence_intent(meaning_expansion):
    subject = meaning_expansion.get("expanded_subject", {})
    mood = meaning_expansion.get("expanded_mood", {})

    return {
        "identity_relation": subject.get("identity_relation"),
        "semantic_role": subject.get("semantic_role"),
        "presence_direction": subject.get("presence_direction"),
        "emotional_tone": mood.get("emotional_tone"),
        "presence_intensity": mood.get("presence_intensity"),
        "presence_notes": mood.get("presence_notes", []),
    }


def build_context_intent(meaning_expansion):
    context = meaning_expansion.get("expanded_context", {})

    return {
        "context_role": context.get("context_role"),
        "spatial_meaning": context.get("spatial_meaning"),
        "viewing_condition": context.get("viewing_condition"),
        "context_notes": context.get("context_notes", []),
    }