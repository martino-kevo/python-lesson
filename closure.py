# Closure is a function having access to the scope of it's
# parent function after the parent function has returned.

def parent_function(person, coins):

    # coins = 3

    def play_game():

        nonlocal coins
        coins -= 1

        if coins > 1:
            print(f"\n{person} has {coins} coins left.")
        elif coins == 1:
            print(f"\n{person} has {coins} coin left.")
        else:
            print(f"\n{person} is out of coins.")

    return play_game


tommy = parent_function("Temmy", 3)
jenny = parent_function("Jenny", 5)

tommy()
tommy()

jenny()

tommy()
print()
