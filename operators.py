# Python operators - symbols used to perform operations on values and the variables that hold those values.

print()

# Assignment opearator (=)
name = 'Dave'
print(name)

print()

meaning = 42
print(meaning)
print()

# Arithmetic opearator
print(2 + 2)    # addition
print(4 - 2)    # subtraction
print(2 * 2)    # multiplication
print(24 / 5)   # division

print(24 // 5)  # floor division - going to round the answer down
print(round(24 / 5))    # round method - going to round the answer up
print(24 % 5)   # remainder
print(2 ** 3)   # to the power of - 2 ** 3 (2 * 2 * 2)

# Combining the assignment operator and the arithmetic operator
meaning = 42
meaning += 1    # same as meaning = meaning + 1
print(meaning)

meaning -= 1
print(meaning)

meaning *= 10
print(meaning)

meaning /= 10
print(meaning)

meaning = round(meaning)
print(meaning)

# Concatination
print("Dave " + "Gray")

# Comparison operator
print(42 == 41)
print(42 == 42)
print()
print(42 != 42)
print(42 != 43)
print()
print(10 < 5)
print(10 > 5)
print(10 >= 10)
print(10 <= 10)

x = True
y = False
z = True

print(not x)
print(not y)
print(not z)
print()
print(x and y)
print(y or x)

# if else statement
meaning = 42

if meaning > 10:
    print('Right on!')
else:
    print('Not today!')

# Tenary operator
print('right on!') if meaning > 10 else print('Not today!')

# Identity operator
'''
Identity operators finds out if two objects are
stored with the same memory address
IS and IS NOT
'''

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(id(a))
print(id(b))
print(id(c))

print(a is b)
print(a is not b)
print(a is c)
print(a is not c)
print(a == c)   # Checks for value not memory address

# identity operators can be defferent with strings,
# integers, floats and booleans.
x = 'Angie'
y = x
z = 'Angie'

print(x is y)
print(x is z)


# Membership operator

'''
IN and NOT IN - checks if something is or is not in a sequence
(list, string, set, dictionary, tuple)
'''

ice_cream = 'I love chocolate ice cream'

print('love' in ice_cream)
print('hate' not in ice_cream)

numbers = [1, 2, 3, 4, 5]
this_num = 4

print(this_num in numbers)
print(this_num not in numbers)


'''**************'''
# Bitwise operator
'''
You can omit the first four zeros in binary and
will still mean the number

eg.

00001010 which is the number 10

is the same as

1010 which is also the number 10
'''

# Complement operator - reverses the binary format of the giving num (1 becomes 0, 0 becomes 1)
num = ~12
print(num)

# Storing nagative numbers on your computer
'''
Use the 2's complement formular - 1's complement + 1

First reverse the binary format of the positive 
number of the nagative number presented then add 1.

example
Storing -13

solution
get the binary number of 13 then reverse it and add 1 to it

'''

# bitwise AND (&)
'''
0 0 -> 0
1 0 -> 0
0 1 -> 0
1 1 -> 1
'''

# bitwise OR (|)
'''
0 0 -> 0
1 0 -> 1
0 1 -> 1
1 1 -> 1
'''
print(12 & 13)
print(12 | 13)
print(25 & 30)

# Bitwise XOR (^)
'''
0 0 -> 0
0 1 -> 1
1 0 -> 1
1 1 -> 0
'''
print(12 ^ 13)
print(25 ^ 30)

# Leftshift operator (<<)
'''
Numbers are like this in binary format 1010.0000
Leftshift (<<) means the number gains values from
the right side
'''
print(10 << 2)

# Rightshift operator (>>)
'''
Numbers are like this in binary format 1010.0000
Rightshift (>>) means the number lose values from
the left side
'''
print(10 >> 3)
