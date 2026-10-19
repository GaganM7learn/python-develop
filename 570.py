students = {
    "s1": {"name": "Neha", "age": 21},
    "s2": {"name": "Vikram", "age": 23},
    "s3": {"name": "Sneha", "age": 19},
    "s4": {"name": "Ravi", "age": 20}
}
ages = []

for student_id , info in students.items():
    if info["age"] >= 0 :
        ages.append(info["age"])

result = all(age >= 18 for age in ages)

print(result)