value = 1
print()

# while value <= 10:
#     print(value)
#     if value == 5:
#         break
#     value += 1

# while value <= 10:
#     value += 1
#     if value == 5:
#         continue
#     print(value)
# print("Value is now equal to " + str(value))

names = ['Dave', 'Sarah', 'John']
# for x in names:
#     print(x)
# print()

# for y in "Mississippi":
#     print(y)
# print()

# for x in names:
#     if x == 'Sarah':
#         break
#     print(x)

# for x in names:
#     if x == 'Sarah':
#         continue
#     print(x)
# print()

# for x in range(4):
#     print(x)

# for x in range(1, 5):
#     print(x)

# for x in range(5, 101, 5):
#     print(x)
# print("Glad that's over!")

names = ['Dave', 'Sarah', 'John']
actions = ['codes', 'eats', 'sleeps']
foods = ['Pizzar', 'Cookie', 'Beans']

# for name in names:
#     for action in actions:
#         print(name + " " + action + ".")

for action in actions:
    for food in foods:
        for name in names:
            print(name + " " + action + " " + "and loves " + food + ".")

print()
