numbers = [4, 2, 4, 6, 2, 8, 6]

unique = []

for number in numbers :
    if number not in unique:
        unique.append(number)

print(unique)