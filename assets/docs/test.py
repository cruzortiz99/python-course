from functools import reduce

some_list = [1, 2, 3, 4]
reduced_list = reduce(lambda acc, current: acc + current, some_list)
print(some_list, reduced_list)
