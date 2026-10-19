students = {
    "s1": {"name": "Anu", "age": 22, "city": "Bangalore", "course": "Java"},
    "s2": {"name": "Vijay", "age": 24, "city": "Chennai"},
    "s3": {"name": "Riya", "age": 21, "course": "Python"},
    "s4": {"name": "Sahil", "age": 25, "city": "Delhi", "course": "C++"},
    "s5": {"name": "Pooja", "age": 23}
}

for student_id , info in students.items():
    if "city" in info and "course" in info :
        print(info["name"] ,"both city and course imformation is given")