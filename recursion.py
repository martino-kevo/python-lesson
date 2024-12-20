# Recursive function calls itself

def add_one(num):
    if num >= 9:
        return num + 1

    total = num + 1
    print(total)

    return add_one(total)


print()

my_new_total = add_one(0)
print(my_new_total)
print()


# def ad_one(num):
#     pnum = num + 1
#     while pnum <= 9:
#         print(pnum)
#         pnum += 1

#     return pnum


# print()

# my_nw_total = ad_one(0)
# print(my_nw_total)
# print()
