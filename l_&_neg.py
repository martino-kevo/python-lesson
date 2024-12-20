# Modifying different lists value at the same index at the same time

r = [1, 2, 3]
g = [4, 5, 6]
l = [7, 8, 9]


def po():

    count = 0

    def ao():
        nonlocal count
        count += 1
        return count

    return ao


p = po()


for x in r, g, l:
    x[-1] = p()

print(r)
print(g)
print(l)

# Checking for negative values

wq = input('\nEnter\n')
wq = int(wq)

y = abs(wq) * -1

print("\nCan't have a negative value, bro!") if wq == y else print(
    "\nStay positive 😎")

print(wq)
