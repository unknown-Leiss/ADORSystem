runtime_state = {
    "identity": {},
    "behavior": {},
    "recognition": {},
    "verification": {},
    "reconstruction": {}
}


def read_header_value(lines, label):
    """
    RAG SEARCH ANCHOR のように

    Document Title:
    [T3-Character] ...

    の形式で、ラベルの次の行を読む。
    """
    for i, line in enumerate(lines):
        line = line.strip()

        if line.startswith(label):
            if i + 1 < len(lines):
                return lines[i + 1].strip()

    return None


def apply_layer(content, layer_name):
    """
    DocumentをLayerとしてRuntime Stateへ反映する。
    ここではCharacterを定義しない。
    Document RoleをRuntime Stateへ登録する。
    """
    global runtime_state

    lines = content.splitlines()

    layer_data = {
        "document_title": read_header_value(lines, "Document Title:"),
        "character_name": read_header_value(lines, "Character Name:"),
        "document_type": read_header_value(lines, "Document Type:"),
        "document_role": read_header_value(lines, "Document Role:"),
    }

    runtime_state[layer_name] = layer_data

    print()
    print("=== Layer Runtime Updated ===")
    print(f"Layer: {layer_name}")
    print("-----------------------------")
    print(f"Document Title: {layer_data['document_title']}")
    print(f"Character Name: {layer_data['character_name']}")
    print(f"Document Type: {layer_data['document_type']}")
    print(f"Document Role: {layer_data['document_role']}")
    print()

    show_runtime_state()

    return runtime_state


def show_runtime_state():
    print()
    print("=== Runtime State ===")
    print(runtime_state)

def show_runtime_state():
    print()
    print("=== Runtime State ===")
    print("---------------------")

    for layer_name, layer_data in runtime_state.items():
        print(f"[{layer_name}]")

        if not layer_data:
            print("  empty")
            continue

        print(f"  Document Title: {layer_data['document_title']}")
        print(f"  Character Name: {layer_data['character_name']}")
        print(f"  Document Type: {layer_data['document_type']}")
        print(f"  Document Role: {layer_data['document_role']}")
        print()