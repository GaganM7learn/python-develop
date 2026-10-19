with open("course.txt" , "w") as file :
    file.write("Python Course Complete")

with open("course.txt" , "r") as file :
    print(file.read())