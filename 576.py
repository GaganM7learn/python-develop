scores = [42, 73, 81, 58, 91]
result = any( score >= 70 and score <= 80 for score in scores)

print(result)