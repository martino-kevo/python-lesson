# Lists

users = ['Dave', 'Sarah', 'John']

data = ['Dave', 45, True]

empty_list = []

print()

print("Dave" in empty_list)
print()
print(users[0])
print(users[-1])
print(users[-2])
print()
print(users.index("Sarah"))
print()
print(users[0:2])
print(users[1:])
print(users[-3:-1])
print()
print(len(users))
print()

users.append('Elsa')
print(users)

users += ['Jason']
print(users)

users.extend(['Sam', 'Jimmy'])
print(users)

# users.extend(data)
# print(users)

# users += data
# print(users)
print()

users.insert(0, 'Bob')
print(users)
print()

users[2:2] = ['Eddie', 'Alex']
print(users)
print()

users[1:3] = ['Ron', 'Paker']
print(users)
print()

users.remove('Bob')
print(users)
print()

print(users.pop())
print(users)
print()

del users[0]
print(users)
print()

# del data
data.clear()
print(data)
print()

users[1:2] = ['dave']
users.sort()
print(users)
print()

users.sort(key=str.lower)
print(users)
print()

nums = [4, 42, 78, 1, 5]
nums.reverse()
print(nums)
print()

# nums.sort(reverse=True)
# print(nums)
# print()

print(sorted(nums, reverse=True))
print(nums)
print()

numscopy = nums.copy()
my_nums = list(nums)
my_copy = nums[:]

print(numscopy)
print(my_nums)
my_copy.sort()
print(my_copy)
print(nums)
print()

print(type(nums))
print()

my_list = list([1, 'Neil', True])
print(my_list)
print()

# Tuples

my_tuple = tuple(('Dave', 42, True))

another_tuple = (1, 4, 2, 8, 2, 2)

print(my_tuple)
print(type(my_tuple))
print(type(another_tuple))
print()

new_list = list(my_tuple)
new_list.append('Neil')
new_tuple = tuple(new_list)
print(new_tuple)
print()

(one, *two, hey) = another_tuple
print(one)
print(*two)
print(hey)
print()

print(another_tuple.count(2))
print()

c_tuple = (1, 2, 3, 4, 5)
print(c_tuple)

(*l,) = c_tuple
l.extend([6, 7])

print()
c_tuple = tuple((l))
print(c_tuple)
