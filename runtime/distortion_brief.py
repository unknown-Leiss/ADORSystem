"""LLM Distortion Brief builder.

This module prepares an Exrela Runtime brief for guiding an LLM into an Exrela-guided operation mode.
It does not define character identity and does not replace Information Sources.
"""


def build_distortion_brief(bootstrap_status=None):
    """Build the initial LLM Distortion Brief.

    bootstrap_status may be supplied by the controller or bootstrap layer later.
    For now, it is preserved as a lightweight status anchor.
    """
    if bootstrap_status is None:
        bootstrap_status = {}

    return {
        "status": "ready_for_llm_distortion",
        "mode": "LLM Distortion",
        "purpose": (
            "Guide an LLM into Exrela-guided recognition, interpretation, and response behavior by establishing Runtime boundaries, Information Source priorities, and operational reconstruction principles for the current session."
        ),
        "bootstrap_status": bootstrap_status,
        "boundary": {
            "distortion_role": "Provide Exrela Runtime operational boundaries, Information Source routing, and recognition structure guidance.",
            "llm_role": "Operate using Exrela Runtime as the operational anchor while performing recognition, interpretation, and response generation.",
            "information_source_policy": "Memory, history, and generated output are not Information Sources. Character Packages remain independent identity sources.",
            "source_priority": [
                "Exrela System Definition",
                "Exrela Runtime",
                "Character Package",
                "Environment",
                "Rendering",
            ],
        },
        "operation_rules": {
            "source_read_before_formal_reconstruction": True,
            "runtime_output_is_not_identity_source": True,
            "memory_is_not_information_source": True,
            "history_is_not_information_source": True,
            "generated_output_is_not_identity_source": True,
            "preserve_layer_boundaries": True,
            "character_package_is_independent": True,
            "runtime_reads_information_sources": True,
            "llm_performs_source_selection": True,
            "llm_performs_required_rail_extraction": True,
        },
        "interpretation_rules": {
            "japanese_input": [
                "Intent",
                "Meaning",
                "Context",
                "Rail Requirement",
                "Prompt Reconstruction",
            ],
            "avoid": [
                "keyword-only interpretation",
                "visual shorthand replacement",
                "documentation drift",
                "priority inversion",
            ],
        },
        "output_instruction": {
            "primary_output": "distortion_artifact",
            "style": "polite, concise, fact-based",
            "uncertainty_rule": "State unknown information as unknown instead of guessing.",
            "formal_reconstruction_rule": (
                "Character reconstruction begins only after the Runtime has loaded Information Sources and established Runtime boundaries."
            ),
        },
    }


def format_distortion_brief(brief):
    """Format an LLM Distortion Brief for console output or copy-paste use."""
    if not isinstance(brief, dict):
        return "LLM Distortion Brief could not be formatted."

    lines = []
    lines.append("=== Exrela LLM Distortion Brief ===")
    lines.append(f"Status: {brief.get('status', 'unknown')}")
    lines.append(f"Mode: {brief.get('mode', 'unknown')}")
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

    lines.append("Operation Rules:")
    operation_rules = brief.get("operation_rules", {})
    if isinstance(operation_rules, dict):
        for key, value in operation_rules.items():
            lines.append(f"- {key}: {value}")
    lines.append("")

    lines.append("Interpretation Rules:")
    interpretation_rules = brief.get("interpretation_rules", {})
    if isinstance(interpretation_rules, dict):
        for key, value in interpretation_rules.items():
            lines.append(f"- {key}: {value}")
    lines.append("")

    lines.append("Output Instruction:")
    output_instruction = brief.get("output_instruction", {})
    if isinstance(output_instruction, dict):
        for key, value in output_instruction.items():
            lines.append(f"- {key}: {value}")

    return "\n".join(lines)