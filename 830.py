class AgeError(Exception):
    pass
age =-6

try:
    if age < 0:
        raise AgeError("Age cannot be negative")
except AgeError as error:
    print(error)