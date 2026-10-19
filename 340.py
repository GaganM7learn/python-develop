numbers = [1,2,3,4,5,6]

even_squares = {
    number : number * number 
    for number in numbers
    if number%2 == 0
}

print(even_squares)