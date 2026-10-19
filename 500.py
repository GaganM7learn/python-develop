students = {
    "s1": {"name": "Ritu", "age": 22, "course": "Python"},
    "s2": {"name": "Mohan", "age": 31, "course": "Java"},
    "s3": {"name": "Sanjay", "age": 27, "course": "C++"},
    "s4": {"name": "Lakshmi", "age": 25, "course": "Python"},
    "s5": {"name": "Gopal", "age": 29, "course": "Java"},
    "s6": {"name": "Pavan", "age": 24, "course": "C++"}
}

oldest_student = {}
highest_age = 0

for student_id , info in students.items():
    if info['age'] > highest_age :
        highest_age = info["age"]

        oldest_student = {
            "name" : info["name"], 
            "age" : info['age'],
            "course" : info["course"]
        }

print(oldest_student)