try : 
    a = int(input("Enter first number"))
    b = int(input("Enter second number"))

    result = a / b 

    print(result)

except ValueError :
    print("Invalid value")


except ZeroDivisionError : 
    print("Please do not divide it with zero ")