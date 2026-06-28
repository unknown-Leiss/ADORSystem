

def run_meaning_expansion(meaning_verification):
    print()
    print("=== Meaning Expansion Runtime ===")

    meaning = meaning_verification.get("meaning", {})
    scene_meaning = meaning.get("scene_meaning", {})

    subject = scene_meaning.get("subject")
    main_action = scene_meaning.get("main_action")
    mood = scene_meaning.get("mood")
    context = scene_meaning.get("context")

    expanded_meaning = {
        "verified_meaning": meaning_verification,
        "expanded_subject": expand_subject(subject),
        "expanded_action": expand_action(main_action),
        "expanded_mood": expand_mood(mood),
        "expanded_context": expand_context(context),
        "expansion_status": "provisional",
        "ready_for_operational_intent": True,
        "purpose": "Expand verified meaning before Operational Intent Runtime",
    }

    print("Meaning Expansion Ready")

    return expanded_meaning


def expand_subject(subject):
    if not subject:
        return None

    text = subject.get("text")

    expansion = {
        "source": subject,
        "text": text,
        "identity_relation": "scenario_subject",
        "semantic_role": "existence_anchor",
    }

    if text == "Leiss":
        expansion["identity_source_link"] = "Character Understanding identity_source"
        expansion["presence_direction"] = "quiet_existing_person"

    return expansion


def expand_action(action):
    if not action:
        return None

    text = action.get("text", "")

    expansion = {
        "source": action,
        "text": text,
        "behavior_role": "main_behavior",
        "operational_notes": [],
    }

    if "見下ろ" in text:
        expansion["behavior_interpretation"] = "observational_gaze"
        expansion["gaze_structure"] = "downward_view_toward_target_space"
        expansion["body_state"] = "mostly_still"
        expansion["operational_notes"].extend([
            "prioritize observation over performance",
            "keep the body calm and non-dramatic",
            "treat the viewed space as important context",
        ])

    return expansion


def expand_mood(mood):
    if not mood:
        return None

    text = mood.get("text", "")

    expansion = {
        "source": mood,
        "text": text,
        "mood_role": "behavior_modifier",
        "presence_notes": [],
    }

    if "静か" in text:
        expansion["emotional_tone"] = "calm"
        expansion["presence_intensity"] = "low"
        expansion["presence_notes"].extend([
            "avoid exaggerated emotion",
            "avoid performance-like posing",
            "favor restrained presence",
        ])

    return expansion


def expand_context(context):
    if not context:
        return None

    text = context.get("text", "")

    expansion = {
        "source": context,
        "text": text,
        "context_role": "scene_grounding",
        "context_notes": [],
    }

    if "山頂" in text:
        expansion["spatial_meaning"] = "high_place"
        expansion["viewing_condition"] = "wide_view_from_above"
        expansion["context_notes"].extend([
            "treat the location as elevated",
            "support a downward viewing structure",
            "allow the environment to dominate the scene",
        ])

    return expansion