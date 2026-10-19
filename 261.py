try :
    a = int(input("Enter first number :"))
    b = int(input("Enter second number :"))

    result = a / b 

except ValueError :
    print("Invalid value")

except ZeroDivisionError :
    print("Cannot divide with zero")


else :
    print("Division Successful :" , result)