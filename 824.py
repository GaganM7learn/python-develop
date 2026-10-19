class Product :
    def __init__(self , price) :
        self.price = price

    @property
    def price(self) :
        return self._price 

    @price.setter

    def price(self , value):
        if value < 0 :
            raise ValueError("Price cannot be negative")
                             
        self._price = value

item = Product(250)

print(item.price)