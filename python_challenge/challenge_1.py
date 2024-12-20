'''
Create a funtion to check if a number is disarium or not.

A number is disarium where the sum of each
digit raised to the power of its position 
is equal to the number itself.

let us pick the number 175

eg: 1^1 + 7^2 + 5^3 = 175
'''

# Solution


def is_disarium_number(num):

    position = 0
    s_num = str(num)
    a_num = 0

    for x in s_num:
        position += 1
        a_num += int(x)**position

    if a_num == num:
        return True
    else:
        return False


print()

for num in range(3000001):
    if is_disarium_number(num) == True:
        print(f"{num}\t{is_disarium_number(num)}\n")


# is_num_disarium = is_disarium_number(num)
# print()
# print(is_num_disarium)
