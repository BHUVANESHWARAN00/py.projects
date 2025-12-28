
filename = input("Enter the filename to open or create: ")
try:
    with open(filename, "r") as file:
        print(f"\nFile '{filename}' opened successfully.\n")
        print("Current content:\n")
        print(file.read())
except FileNotFoundError:
    print(f"\n'{filename}' not found. Creating a new file.\n")

print("Enter your text (type 'SAVE' on a new line to save and exit):")
lines = []
while True:
    line = input()
    if line.strip().upper() == "SAVE":
        break
    lines.append(line)
with open(filename, "w") as file:
    file.write("\n".join(lines))
print(f"\nFile '{filename}'saved.")

