try :
    a = int(input("Enter first number :"))
    b = int(input("Enter second number : "))

    result = a / b


except ValueError :
    print("Enter number only")

except ZeroDivisionError :
    print("Cannot divide by zero ")


else :

    print("Result :" , result)