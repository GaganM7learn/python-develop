def student_info(**detials):

    for key, value in detials.items():

        print(key , ":", value)


student_info(
    name = "Gagan",
    age = 19 , 
    course = "Pyhton",
    goal = "pyhton Developer"
)