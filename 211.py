def add(*numbers):
    total = 0


    for number in numbers :
        total = total + number

    return total 

print(add(10,20))
print(add(10,20,30)) 

print(add(10,20,30,40,50))