students = [
    {"name": "Mia", "score": 82},
    {"name": "Leo", "score": 95},
    {"name": "Ava", "score": 88}
]

result = sorted(students , key=lambda s: s["score"])

print(result)