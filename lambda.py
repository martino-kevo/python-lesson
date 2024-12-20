# A lamdbda function is a single expression that returns a value.

from functools import reduce
print()


def squared(num): return num * num
# lambda num: num * num
# squred = lambda num: num * num


print(squared(2))


def add_two(num): return num + 2


print(add_two(12))


def sum_total(a, b): return a + b
# lambda a, b: a + b
# sum_total = lambda a, b: a + b


print(sum_total(10, 8))
print()


#######################

def func_builder(x):
    return lambda num: num + x


add_ten = func_builder(10)
add_twenty = func_builder(20)

print(add_ten(7))
print(add_twenty(7))
print()


# Higher-order function
# This is a function that takes one or more functions as arguments...
#   or
# A function that returns a function as its result

lambda num: num * num

numbers = [3, 7, 12, 18, 20, 21]

squared_nums = map(lambda num: num * num, numbers)

print(list(squared_nums))

for num in squared_nums:
    print(num)

print()


##################

odd_nums = filter(lambda num: num % 2 != 0, numbers)

print(list(odd_nums))
print()


# Reduce can be a more complex higher-order function but in a simple term it just adds everyrhting together
#
# The function that reduce accepts needs two parameters (accumulator or subtotal, current_item)

numbers = [1, 2, 3, 4, 5, 1]

total = reduce(lambda acc, curr: acc + curr, numbers,)

print(total)
print(sum(numbers, 10))
print()

names = ['Dave Gray', 'Sarah Ito', 'John Jacob Jingleheimerschmidt']

char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)

print(char_count)
print(len(names))
print()
