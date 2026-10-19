class Vehicle :
    def move(self):
        print("Moving")

class Bike(Vehicle) :
    pass
child = Bike()
child.move()    