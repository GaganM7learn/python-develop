numbers = [10,20,30,40,50]

try :
    index = int(input('Enter an index no :'))

    print(numbers[index])

except ValueError : 
    print("Invalid Value")



except IndexError :
    print("Invalid index ")