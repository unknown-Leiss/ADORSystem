"""Reconstruction Brief builder.

This module does not interpret scenario meaning or select package information by itself.
It organizes Exrela Runtime reconstruction outputs into a stable full brief that an Exrela-guided LLM can read.
"""


def _safe_get(mapping, key, default=None):
    if isinstance(mapping, dict):
        return mapping.get(key, default)
    return default


def build_reconstruction_brief(runtime_result):
    """Build an AI-facing Reconstruction Brief from package_reader runtime output.

    The brief is intended to be passed to an Exrela-guided LLM after Exrela Runtime
    has loaded the Character Package and prepared intermediate reconstruction structures.
    """
    if not isinstance(runtime_result, dict):
        return {
            "status": "blocked",
            "reason": "runtime_result is not a dictionary",
            "brief": "Reconstruction Brief could not be generated.",
        }

    character = _safe_get(runtime_result, "character", "Unknown")
    scenario_interpretation = _safe_get(runtime_result, "scenario_interpretation", {})
    scenario = (
        _safe_get(runtime_result, "scenario", "")
        or _safe_get(scenario_interpretation, "scenario", "")
    )
    context = _safe_get(runtime_result, "context", {})
    understanding = _safe_get(runtime_result, "understanding", {})
    meaning_expansion = _safe_get(runtime_result, "meaning_expansion", {})
    structural_observation = _safe_get(runtime_result, "structural_observation", {})
    recognition_resolution = _safe_get(runtime_result, "recognition_resolution", {})

    brief = {
        "status": "ready_for_exrela_guided_reconstruction",
        "mode": "Reconstruction",
        "character": character,
        "purpose": (
            "Provide the loaded Character Package, Exrela Runtime outputs, and user scenario "
            "to an Exrela-guided LLM so it can perform scenario-based source selection, "
            "required rail extraction, and reconstruction prompt artifact generation."
        ),
        "boundary": {
            "runtime_role": "Load Character Package sources and organize reconstruction structures without deciding final scenario-based source selection.",
            "llm_role": "Use the user-provided scenario and full package/runtime inputs to perform meaning interpretation, Character Package selection, required rail extraction, and prompt reconstruction.",
            "runtime_interpretation_status": "provisional",
            "prefer_original_scenario": True,
            "do_not_treat_runtime_as_identity_source": True,
            "package_information_policy": "full_package_context_allowed",
            "source_selection_owner": "exrela_guided_llm",
        },
        "scenario": scenario,
        "scenario_source": {
            "raw": scenario,
            "source": "User Input",
            "runtime_status": "anchored",
            "note": "This is the scenario written by the user. Preserve it as the primary scenario reference during reconstruction.",
        },
        "inputs": {
            "character_context": context,
            "character_understanding": understanding,
            "recognition_resolution": recognition_resolution,
            "structural_observation": structural_observation,
            "meaning_expansion": meaning_expansion,
            "scenario_interpretation": scenario_interpretation,
        },
        "output_instruction": {
            "primary_output": "image_prompt_artifact",
            "required_layers": [
                "Character Core",
                "Meaning",
                "Behavior",
                "Presence",
                "Physical",
                "Rendering",
                "Negative Constraints",
            ],
            "selection_rule": (
                "Use the full Character Package context as available input. "
                "Select scenario-relevant information during Exrela-guided reconstruction, "
                "while preserving identity continuity and recognition continuity."
            ),
        },
    }

    return brief


def format_reconstruction_brief(brief):
    """Format a Reconstruction Brief for console output or copy-paste use."""
    if not isinstance(brief, dict):
        return "Reconstruction Brief could not be formatted."

    lines = []
    lines.append("=== Reconstruction Brief ===")
    lines.append(f"Status: {brief.get('status', 'unknown')}")
    lines.append(f"Mode: {brief.get('mode', 'unknown')}")
    lines.append(f"Character: {brief.get('character', 'Unknown')}")
    lines.append("")
    lines.append("Purpose:")
    lines.append(str(brief.get("purpose", "")))
    lines.append("")
    lines.append("Boundary:")
    boundary = brief.get("boundary", {})
    if isinstance(boundary, dict):
        for key, value in boundary.items():
            lines.append(f"- {key}: {value}")
    lines.append("")
    lines.append("Scenario:")
    lines.append(str(brief.get("scenario", "")))
    lines.append("")
    lines.append("Scenario Source:")
    scenario_source = brief.get("scenario_source", {})
    if isinstance(scenario_source, dict):
        for key, value in scenario_source.items():
            lines.append(f"- {key}: {value}")
    lines.append("")
    lines.append("Output Instruction:")
    output_instruction = brief.get("output_instruction", {})
    if isinstance(output_instruction, dict):
        for key, value in output_instruction.items():
            lines.append(f"- {key}: {value}")

    return "\n".join(lines)