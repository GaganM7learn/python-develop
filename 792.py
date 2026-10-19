try:
    with open("missing.txt", "r") as file:
        print(file.read())

except FileNotFoundError :
    print("File not found")