numbers =

double_numbers = list(map(lambda x: x * 2, numbers))
print(double_numbers)

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

from functools import reduce
sum_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_numbers)
