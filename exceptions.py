class JustNotCoolError(Exception):
    pass


x = 2
print()

try:
    raise JustNotCoolError("This just isn't cool, man.")
    # raise Exception("I'm a custom exception")
    # print(x / 1)
    # if type(x) is not str:
    #     raise TypeError("Only strings are allowed.")
except NameError:
    print("NameError means something is probably undefined.")
except ZeroDivisionError:
    print("Please do not divide by zero.")
except Exception as error_msg:
    print(error_msg)
else:
    print("I'm only going to print when there's no error")
finally:
    print("I'm going to print with or without an error.")

print()
