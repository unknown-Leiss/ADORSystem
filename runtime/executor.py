from layer_runtime import apply_layer

runtime_state = {}

def execute_character_core(content):
    global runtime_state

    print()
    print("=== Character Core Executor ===")
    print()

    lines = content.splitlines()

    runtime_state = {
        "document_title": None,
        "character_name": None,
        "document_type": None,
        "document_role": None,
    }

    for i, line in enumerate(lines):
        line = line.strip()

        if line.startswith("Document Title:"):
            runtime_state["document_title"] = lines[i + 1].strip()

        elif line.startswith("Character Name:"):
            runtime_state["character_name"] = lines[i + 1].strip()

        elif line.startswith("Document Type:"):
            runtime_state["document_type"] = lines[i + 1].strip()

        elif line.startswith("Document Role:"):
            runtime_state["document_role"] = lines[i + 1].strip()

    print("Runtime State")
    print("-------------")
    print(f"Document Title: {runtime_state['document_title']}")
    print(f"Character Name: {runtime_state['character_name']}")
    print(f"Document Type: {runtime_state['document_type']}")
    print(f"Document Role: {runtime_state['document_role']}")

    print()
    print("Character Core Loaded")

def execute_operational_rail(content):
    global runtime_state

    print()
    print("=== Operational Rail Executor ===")
    print()

    lines = content.splitlines()

    runtime_state["rail_title"] = None
    runtime_state["rail_role"] = None
    runtime_state["rail_type"] = None

    for i, line in enumerate(lines):
        line = line.strip()

        if line.startswith("Document Title:"):
            runtime_state["rail_title"] = lines[i + 1].strip()

        elif line.startswith("Document Role:"):
            runtime_state["rail_role"] = lines[i + 1].strip()

        elif line.startswith("Document Type:"):
            runtime_state["rail_type"] = lines[i + 1].strip()

    print("Runtime State Updated")
    print("---------------------")
    print(f"Rail Title: {runtime_state['rail_title']}")
    print(f"Rail Type: {runtime_state['rail_type']}")
    print(f"Rail Role: {runtime_state['rail_role']}")

    print()
    print("Operational Rail Loaded")

def execute_verification(content):
    print()
    print("=== Verification Executor ===")
    print("Preparing Verification...")
    print()

def execute_reconstruction(content):
    print()
    print("=== Reconstruction Executor ===")
    print("Preparing Reconstruction...")
    print()

def execute_unknown(content):
    print()
    print("Unknown Executor")

def execute_recognition(content):
    print("\n=== Recognition Executor ===")
    apply_layer(content, "recognition")
    print("Recognition Loaded")