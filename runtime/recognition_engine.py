from recognition_modules.particle_module import apply_particle_module
from recognition_modules.compound_module import apply_compound_module


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

    print("Recognition Engine Ready")

    return recognition_candidates