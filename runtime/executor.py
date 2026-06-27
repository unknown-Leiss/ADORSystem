from layer_runtime import apply_layer

def execute_character_core(content):
    print("\n=== Character Core Executor ===")
    apply_layer(content, "identity")
    print("Character Core Loaded")

def execute_operational_rail(content):
    print("\n=== Operational Rail Executor ===")
    apply_layer(content, "behavior")
    print("Operational Rail Loaded")

def execute_verification(content):
    print("\n=== Verification Executor ===")
    apply_layer(content, "verification")
    print("Verification Loaded")

def execute_reconstruction(content):
    print("\n=== Reconstruction Executor ===")
    apply_layer(content, "reconstruction")
    print("Reconstruction Loaded")

def execute_unknown(content):
    print("\n=== Unknown Executor ===")
    print("Unknown executor called")

def execute_recognition(content):
    print("\n=== Recognition Executor ===")
    apply_layer(content, "recognition")
    print("Recognition Loaded")