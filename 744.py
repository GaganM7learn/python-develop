numbers = [3,4,5,3,7,5,9]

unique = []

for number in numbers :
    if number not in unique :
        unique.append(number)

print(unique)
