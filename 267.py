try :
    age = int(input("Enter your age :"))

    if age < 0 :
        raise ValueError("Age cannot be negative")

    print("Age", age)


except ValueError as error :
    print("Error" , error)