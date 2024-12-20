# Module lesson example

from random import choice

capital = "Ikeja"

bird = "Sparrow"

flower = "Roseflower"

song = "Imagine dragon"


def randomfunfact():

    funfacts = [
        "Lagos is always busy.",
        "Victoria island is the largest city in Lagos.",
        "A portion of Victoria island city is in Banana island.",
        "Almost all lagosians love visiting Victoria island."
    ]

    index = choice("0123")

    print(funfacts[int(index)])


# Always do this when you want to call a function inside of a module.
if __name__ == "__main__":
    randomfunfact()
