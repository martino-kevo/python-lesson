print()
a = ['w', 'e', 'y', 'g', 'y']
b = a
c = ['w', 'e', 'y', 'g', 'y']
d = ['w', 'e', 'y', 'g', 'y']
e = ['w', 'e', 'y', 'g', 'y']

# Python tries to manage memory for int, float, str and bool
# data types, but not for list, set, dict and tuple
# data structures.

print(a is not d)
print(a is e)
print()


def ao(*g):
    (*j,) = g
    print(j)


ao(2.4, 5, 'y')
print()


class Woman:

    def __init__(self):
        print('All women are beautiful')


class Boy:

    # Static variables
    food = 'We are sharing this food 😋'
    idd = 3

    def __init__(self, n, a, c):
        self.name = n
        self.age = a
        self.country = c

    # You can only have static variables in a static method
    @staticmethod
    def playing(self):
        self.idd += 1
        # print(f"{self.food} is playing... {self.idd}")
        print(f"I am playing Play Station {self.idd}")

    class Girl(Woman):
        pass


print("The girl class is saying:")
girl = Boy.Girl()

print()

print("The woman class is saying:")
woman = Woman()
print()

# My question now is, "why would one want to have a nested class"?

boy1 = Boy('Dale', 13, 'GHN')
print(f"My name is {boy1.name}")
print(boy1.food)
boy1.playing(self=Boy)

print()

boy2 = Boy('Tim', 10, 'USA')
print(f"My name is {boy2.name}")
print(boy2.food)
boy2.playing(self=Boy)

# All instances / objects of a class share
# the same static variables and static method 😉.
