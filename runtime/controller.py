from loader import bootstrap

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
else:
    print("Unknown Mode")