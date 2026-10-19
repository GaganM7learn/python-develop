from functools import reduce 
numbers = [2,3,4,5]
result = reduce( lambda a , b : a * b , numbers)


print(result)