def car_info(**details):


    for key , value in details.items() :

        print(key , ":", value)


car_info(
    brand = "BMW",
    model = "something",
    year = 2016,
    price = 6700000
)