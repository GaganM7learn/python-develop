class Phone :
    def __init__(self , name , price):
        self.name = name
        self.price = price

phone = Phone("Samsung" , 25000)

print(phone.name)

print(phone.price)