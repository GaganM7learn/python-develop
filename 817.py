class Animal :
    def speak(self):
        print("Animal sound")

class Dog(Animal) :
    pass

pet = Dog()
pet.speak()