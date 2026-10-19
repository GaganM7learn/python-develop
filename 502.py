students = {
    "s1": {"name": "Deepa", "age": 22, "course": "Python"},
    "s2": {"name": "Rakesh", "age": 19, "course": "Java"},
    "s3": {"name": "Naveen", "age": 26, "course": "C++"},
    "s4": {"name": "Sita", "age": 17, "course": "Python"},
    "s5": {"name": "Manoj", "age": 24, "course": "Java"},
    "s6": {"name": "Geeta", "age": 20, "course": "C++"}
}

youngest_age = 999
youngest_student = {}

for student_id , info in students.items():
    if info["age"] < youngest_age :
        youngest_age = info["age"]


        youngest_student = {
            "name" : info["name"] , 
            "age" : info["age"],
            "course" : info["course"]
        }
print(youngest_student)