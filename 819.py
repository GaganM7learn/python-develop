class Animal :
    def speak(self):
        print("Some sound")

class Cat(Animal) :
    def speak(self):
        print("Meow")

pet = Cat()
pet.speak()