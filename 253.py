try :
    a = int(input("Enter first number"))
    b = int(input("Enter second number"))

    result = a / b

    print(a ,"/", b , "=", result)


except ZeroDivisionError :

    print("Cannot divide by zero")