with open("notes.txt" , "w") as file :
    file.write("Hello Python")

with open("notes.txt" , 'r') as file :
    print(file.read())