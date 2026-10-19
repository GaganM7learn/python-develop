numbers = [15, 22, 34, 41, 56]
all_result = all( number > 10 for number in numbers)
any_result = any( number % 5 == 0 for number in numbers)

print(all_result)
print(any_result)