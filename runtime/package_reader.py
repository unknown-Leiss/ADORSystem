from loader import list_character_files, load_document, detect_document_type
from router import route

def load_character_package(character_name):
    print()
    print("=== Character Package Reader ===")
    print(f"Character: {character_name}")

    files = list_character_files(character_name)

    if not files:
        print("No documents found.")
        return

    for document in files:
        print()
        print(f"Loading Document: {document}")

        content = load_document(character_name, document)
        doc_type = detect_document_type(document)

        if content:
            print(f"Document Type: {doc_type}")
            route(doc_type, content)
        else:
            print("Failed to load document")

    print()
    print("=== Character Package Loaded ===")