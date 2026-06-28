

def run_meaning_reconstruction(structural_organization):
    print()
    print("=== Meaning Reconstruction Runtime ===")

    existence_structure = structural_organization.get("existence_structure", [])
    behavior_structure = structural_organization.get("behavior_structure", {})
    context_structure = structural_organization.get("context_structure", [])
    spatial_structure = structural_organization.get("spatial_structure", [])

    actions = behavior_structure.get("actions", [])
    attributes = behavior_structure.get("attributes", [])

    meaning = {
        "structural_organization": structural_organization,
        "existence_meaning": {
            "entities": existence_structure,
            "purpose": "Identify who or what exists in the scenario",
        },
        "behavior_meaning": {
            "actions": actions,
            "attributes": attributes,
            "purpose": "Identify what is happening and how it is performed",
        },
        "context_meaning": {
            "structures": context_structure,
            "spatial_relations": spatial_structure,
            "purpose": "Identify where the scenario is grounded and how elements relate spatially",
        },
        "scene_meaning": {
            "subject": existence_structure[0] if existence_structure else None,
            "main_action": actions[0] if actions else None,
            "mood": attributes[0] if attributes else None,
            "context": context_structure[0] if context_structure else None,
        },
        "meaning_status": "provisional",
        "purpose": "Reconstruct meaning from organized structures before Scenario Interpretation",
    }

    print("Meaning Reconstruction Ready")
    return meaning