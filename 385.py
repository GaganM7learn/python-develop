student = {
    "name" : "Gagan" , 
    "age" : 19
}

city = student.setdefault("city" , "Bangalore")

print(city)

print(student)