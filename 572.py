students = {
    "s1": {"name": "Kabir", "age": 15},
    "s2": {"name": "Anaya", "age": 16},
    "s3": {"name": "Ritesh", "age": 17},
    "s4": {"name": "Tara", "age": 20}
}

ages = []
for student_id , info in students.items():
    ages.append(info["age"])

result = any( age >= 18 for age in ages)
print(result)