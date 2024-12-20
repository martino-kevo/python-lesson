# Global scope: variable or function that is not defined
# inside a function

# Local scope: variable or function that is defined
# inside a function

name = "Dave"
count = 1
print()


def another():

    colour = "Blue"
    global count
    count += 1
    print(count)

    def greeting(name):
        nonlocal colour
        colour = "Red"
        print(colour)
        print(name)

    greeting("Dave")


another()
print()
