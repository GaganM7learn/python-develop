try :
    age = int(input("Enter your age :"))

    if age < 0 :
        raise ValueError("age cannot be negative")

    print("Age :", age)

except ValueError as Error:
    print("Error" , Error )