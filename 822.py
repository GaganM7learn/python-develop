class Device :
    def __init__(self , brand) :
        self.brand = brand

class Laptop(Device):
    def __init__(self , brand ,ram):
        super().__init__(brand)
        self.ram = ram

buy = Laptop("Dell", "16GB")

print(buy.brand , buy.ram)