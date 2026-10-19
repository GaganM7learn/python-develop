try:
    number = int(input("Enter a number :"))
    print("Invalid number")


except ValueError :
    print("Invalid number")


finally :
    print("Program finished")