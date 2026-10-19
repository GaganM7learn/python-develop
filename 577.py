numbers = [12, 18, 24, 30]

all_result = all(number % 2 == 0 for number in numbers )
any_result = any(number > 25 for number in numbers)
print(all_result)
print(any_result)