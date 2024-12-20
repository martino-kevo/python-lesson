import math

# String data type

# literal assignment
first = "Dave"
last = "Gray"

# print()
# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))
# print()

# constructor function
# pizza = str("pepperoni")
# print()
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))
# print()

# Concatenation
fullname = first + " " + last
# print()
# print(fullname)
# print()

# fullname += "!"
# print()
# print(fullname)
# print()

# Casting a number to a string
decade = str(1980)
# print()
# print(type(decade))
# print(decade)
# print()

statement = "I like rock music from the " + decade + "s."
# print()
# print(statement)
# print()

# Multiple lines
multilines = '''
Hey, how are you?   

I was just checking in.   
                            All good?

'''

# print()
# print(multilines)
# print()

# Escaping special characters
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
# print()
# print(sentence)
# print()

# String Medthods
# print()
# print(first.lower())
# print(first.upper())
# print(first)
# print()

# print()
# print(multilines.title())
# print(multilines.replace("good", "ok"))
# print(multilines)
# print()

# print()
# print(len(multilines))
# multilines += "                                 "
# multilines = "                      " + multilines
# print(len(multilines))
# print()

# print()
# print(len(multilines.strip()))
# print(len(multilines.lstrip()))
# print(len(multilines.rstrip()))
print()

# Build a menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Cheesecake".ljust(16, ".") + "$4".rjust(4))
print()

# string index values
print(first[1])
print(first[-1])
print(first[1: -1])
print(first[1:])
print()

# Some methods return boolean data
print(first.startswith("D"))
print(first.endswith("Z"))
print()

# Boolean data types
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))
print()

# Numeric data types

# integer type
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))
print()

# float type
gpa = 3.28
y = float(1.48)
print(type(gpa))
print()

# complex type
comp_value = 5 + 3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)
print()

# Built-in functions for numbers
print(abs(gpa))
print(abs(gpa * -1))

print(round(gpa))
print(round(gpa, 1))
print()

# Math module
print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))
print()

# Casting a string to a number
zipcode = "10001"
zip_values = int(zipcode)
print(type(zip_values))
print()

# Error if you attempt to cast incorrect data
# zip_values = int("New York")
# print()

floor_division = 24 // 5
print(floor_division)
print()

ceil_division = round(24 / 5)
print(ceil_division)
print()

getting_remainder = 24 % 5
print(getting_remainder)
print()

to_the_power_of = 2 ** 5
print(to_the_power_of)
print()

# Boolean operators
x = True
y = False
z = True

# logical operators
movie_is_out = not x
print(movie_is_out)
song_is_out = not y
book_is_out = not z
print()

print(x and y)
print(y or z)

# If, else and elf
meaning = 43
print()

if meaning < 10:
    print("Right on!")
elif meaning == 42:
    print("Equal")
else:
    print("Never mind")

print()

# Teneri operator
print("Right on!") if meaning < 42 else print("Not today")

print()
