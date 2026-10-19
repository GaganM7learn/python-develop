student = {
    "name" : "Gagan" ,
    "age" : 19
}

city = student.setdefault("city" , "UnKnown" )

print(city)
print(student)