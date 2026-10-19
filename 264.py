try :
    number = int(input("Enter a number :"))
    print("You entered :", number)

except ValueError :
    print("Invalid number")

finally :
    print("Program finished")