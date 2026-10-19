numbers = [ 10,15,20,25,30,35,40]

result = filter( lambda x : x % 2 == 0 , numbers )

print(list(result))