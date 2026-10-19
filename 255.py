numbers = [10,20,30]

try :
    index = int(input("Enter an index"))
    print(numbers[index])

except ValueError :
    print("Please enetr a number")

except IndexError :
    print("That index does not  exist")