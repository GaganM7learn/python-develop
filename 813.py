class Rectangle:
    def __init__(self , width , height) :
        self.width = width
        self.height = height

    def area (self) :
        return self.width * self.height

shape = Rectangle(5,3)

print(shape.area())