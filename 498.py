students = {
    "s1": {"name": "Harish", "age": 20, "course": "Python"},
    "s2": {"name": "Kavya", "age": 26, "course": "Python"},
    "s3": {"name": "Nitin", "age": 23, "course": "Java"},
    "s4": {"name": "Swati", "age": 29, "course": "Java"},
    "s5": {"name": "Ajay", "age": 21, "course": "C++"},
    "s6": {"name": "Komal", "age": 25, "course": "C++"}
}

oldest = {}
for student_id , info in students.items():
    course = info["course"]

    if course not in oldest:
        oldest[course] = {
            "name" : info["name"], 
            "age" : info["age"]
        }

    elif info["age"] > oldest[course]["age"] :
        oldest[course] ={
            "name" : info["name"],
            "age" : info["age"]
        }

print(oldest)