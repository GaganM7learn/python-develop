try :
    a = int(input("Enter first number :"))
    b = int(input("Enter sceond number :"))

    result = a / b 

except ValueError :
    print("Invalid number")

except ZeroDivisionError :
    print("Cannot divdie with Zero ")

else :
    print("Division successful ", result)

finally :
    print("Program finished")