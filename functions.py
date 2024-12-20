def hello_world():
    print("Hello world!")


print()

hello_world()
print()


def sum(num1=0, num2=0):
    if type(num1) is not int or type(num2) is not int:
        return
    return num1 + num2


total = sum(2, 4)
print(total)
print()


def multiple_items(*args):
    print(args)
    print(type(args))


multiple_items('Dave', 'Sarah', 'John')
print()


def multi_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))


multi_named_items(first="Dave", last="Gray")
