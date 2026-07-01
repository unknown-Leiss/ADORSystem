from executor import (
    execute_character_core,
    execute_operational_rail,
    execute_recognition,
    execute_persistent_state,
    execute_physical_specification,
    execute_projection,
    execute_archive,
    execute_package_index,
    execute_verification,
    execute_reconstruction,
    execute_unknown,
)

def route(document_type, content):

    if document_type == "Character Core":
        execute_character_core(content)

    elif document_type == "Operational Rail":
        execute_operational_rail(content)

    elif document_type == "Recognition":
        execute_recognition(content)

    elif document_type == "Persistent State":
        execute_persistent_state(content)

    elif document_type == "Physical Specification":
        execute_physical_specification(content)

    elif document_type == "Projection Form":
        execute_projection(content)

    elif document_type == "Drift Archive":
        execute_archive(content)

    elif document_type == "Package Index":
        execute_package_index(content)

    elif document_type == "Verification Specification":
        execute_verification(content)

    elif document_type == "Reconstruction Procedure":
        execute_reconstruction(content)

    else:
        execute_unknown(content)