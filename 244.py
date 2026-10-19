from functools import reduce
numbers =[ 10,20,30,40]
result = reduce( lambda a , b : a + b , numbers )
print(result)