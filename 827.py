class Student :
    school = 'Central School'

    def __init__(self , name):
        self.name = name

person = Student("Ravi")
print(person.school)