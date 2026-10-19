class Employee:
    company = "TechCorp"

    def __init__(self, name):
        self.name = name

person = Employee("Ava")
print(person.company)