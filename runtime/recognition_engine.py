from recognition_modules.particle_module import apply_particle_module
from recognition_modules.compound_module import apply_compound_module

from recognition_modules.action_module import apply_action_module
from recognition_modules.attribute_module import apply_attribute_module
from recognition_modules.relation_module import apply_relation_module
from recognition_modules.entity_module import apply_entity_module


def run_recognition_engine(organized_chunks):
    print()
    print("=== Recognition Engine ===")

    recognition_candidates = []

    recognition_candidates.extend(
        apply_particle_module(organized_chunks)
    )

    recognition_candidates.extend(
        apply_compound_module(organized_chunks)
    )

    recognition_candidates.extend(
        apply_entity_module(organized_chunks)
    )

    recognition_candidates.extend(
        apply_action_module(organized_chunks)
    )

    recognition_candidates.extend(
        apply_attribute_module(organized_chunks)
    )

    recognition_candidates.extend(
        apply_relation_module(organized_chunks)
    )

    print("Recognition Engine Ready")

    return recognition_candidates