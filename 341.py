numbers = [1,2,3,4,5,6]

odd_number = {
    number : number * number 
    for number in numbers
    if number%2 != 0 
}

print(odd_number)