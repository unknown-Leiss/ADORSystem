from loader import (
    bootstrap,
    list_characters,
    list_character_files,
)

print("ADOR Runtime Controller")
print()

print("Select Operation:")
print("1. Analysis")
print("2. Reconstruction")
print("3. Construction")
print("4. Prompt Reconstruction")
print("5. Verification")
print("6. PoC")

choice = input("> ").strip().translate(str.maketrans("１２３４５６", "123456"))
print(f"Selected: {repr(choice)}")

if choice == "2":
    print("Reconstruction Mode")

    bootstrap()

    chars = list_characters()

    print()
    print("Characters:")

    for i, name in enumerate(chars, start=1):
        print(f"{i}. {name}")

    print()
    char_choice = input("Select Character > ").strip().translate(str.maketrans("１２３４５６", "123456"))
    index = int(char_choice) - 1

    if 0 <= index < len(chars):
        selected = chars[index]
        print(f"Loading: {selected}")
        files = list_character_files(selected)
        print()
        print("Documents:")
        for i, file in enumerate(files, start=1):
            print(f"{i}. {file}")
    else:
        print("Invalid Selection")
else:
    print("Unknown Mode")