students = {
    "s1": {"name": "Vikram", "age": 25, "course": "C++"},
    "s2": {"name": "Sneha", "age": 19, "course": "Python"},
    "s3": {"name": "Manish", "age": 23, "course": "C++"},
    "s4": {"name": "Tanya", "age": 21, "course": "Java"},
    "s5": {"name": "Rakesh", "age": 26, "course": "Python"}
}

grouped = {}

for student_id , info in students.items():
    course = info["course"]

    if course not in grouped :
        grouped[course] = []

    grouped[course].append({
        "name" : info["name"], 
        "age" :  info["age"]
    })

print(grouped)