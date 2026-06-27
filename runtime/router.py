from executor import (
    execute_character_core,
    execute_operational_rail,
    execute_recognition,
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

    elif document_type == "Verification Specification":
        execute_verification(content)

    elif document_type == "Reconstruction Procedure":
        execute_reconstruction(content)

    else:
        execute_unknown(content)