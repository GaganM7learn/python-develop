def add_numbers(*numbers):
  total = 0
  for number in numbers :
             total = total + number

  return total 

print(add_numbers(10,20,30))

print(add_numbers(5,10,15,20,25))