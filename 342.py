numbers = [10,20,30,40,50]


large = {
    number : number*2 
    for number in numbers
    if number > 10
}

print(large)