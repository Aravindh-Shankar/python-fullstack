with open("notes.txt", "w") as file:
    file.write("Hello, Aravindh!\n")
    file.write("Welcome to python file handling.\n")

with open("notes.txt", "a") as file:
    file.write("This is a new line.\n")

with open("notes.txt", "r") as file:
    content = file.read()
    print(content)

with open("notes.txt", "r") as file:
    for line in file:
        print("Line:", line.strip())