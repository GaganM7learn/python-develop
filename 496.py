students = {
    "s1": {"name": "Aman", "age": 21, "course": "Python"},
    "s2": {"name": "Riya", "age": 19, "course": "Python"},
    "s3": {"name": "Karan", "age": 25, "course": "Java"},
    "s4": {"name": "Neha", "age": 22, "course": "Java"},
    "s5": {"name": "Vivek", "age": 20, "course": "C++"},
    "s6": {"name": "Pooja", "age": 18, "course": "C++"}
}
youngest = {}
for student_id , info in students.items():
    course = info["course"]

    if course not in youngest :
        youngest[course] = {
            "name" : info["name"],
            "age" : info["age"]
        }

    elif info["age"] < youngest[course]['age'] :
        youngest[course] = {
            "name" : info["name"] , 
            "age" : info["age"]
        }
print(youngest)