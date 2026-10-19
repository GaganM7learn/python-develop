students = {
    "s1": {"name": "Arun", "age": 22, "course": "Python"},
    "s2": {"name": "Megha", "age": 27, "course": "Python"},
    "s3": {"name": "Ravi", "age": 21, "course": "Java"},
    "s4": {"name": "Pooja", "age": 26, "course": "Java"},
    "s5": {"name": "Karan", "age": 24, "course": "C++"},
    "s6": {"name": "Divya", "age": 28, "course": "C++"}
}

oldest = {}

for student_id , info in students.items():
    course = info["course"]
    if course not in oldest :
        oldest[course] = {
            "name" : info["name"] , 
            "age" : info["age"]
        }
    elif info["age"] > oldest[course]["age"] :
        oldest[course] = {
            "name" : info["name"] , 
            "age" : info["age"]
        }
print(oldest)