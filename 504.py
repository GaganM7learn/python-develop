students = {
    "s1": {"name": "Anil", "age": 23, "course": "Python"},
    "s2": {"name": "Bhavna", "age": 18, "course": "Java"},
    "s3": {"name": "Chetan", "age": 30, "course": "C++"},
    "s4": {"name": "Divya", "age": 21, "course": "Python"},
    "s5": {"name": "Eshan", "age": 27, "course": "Java"},
    "s6": {"name": "Farah", "age": 20, "course": "C++"}
}
highest_age = 0
lowest_age = 999

oldest_student = {}
youngest_student = {}

for student_id , info in students.items():
    if info["age"] < lowest_age :
        lowest_age = info["age"]

        youngest_student = {
            "name" : info["name"], 
            "age" : info["age"], 
            "course" : info["course"]
        }

    if info["age"] > highest_age :
        highest_age = info["age"]

        oldest_student = {
            "name" : info["name"] , 
            "age" : info["age"],
            "course" : info["course"] 
        }

print("Oldest student :" , oldest_student)

print("Youngest student :" , youngest_student)