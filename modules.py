# Modules - small code liberies that are based on related features, eg: Math module (contains functions and constant values for use in mathematical equations)

# Math module is a built-in module in Python (Pythons comes with it)

from math import pi
import sys
import random as rdm
from enum import Enum
import lagos
from python_game_project.rps2 import rps


print()
print(pi)

# for item in dir(rdm):
#     print(item)

print()

print(lagos.capital)
lagos.randomfunfact()
print()

print(__name__)
print(lagos.__name__)
print()

rock_paper_scissors = rps('kelvin')
rock_paper_scissors()
