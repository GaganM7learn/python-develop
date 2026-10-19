def student_info(**details):
    for key,value in details.items():

        print(key, ":", value)

student_info(
    name = "Gagan",
    age = 19,
    city = "Bangalore"

)    