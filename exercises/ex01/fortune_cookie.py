"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730400848"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
print ("Your fortune cookie says...")

from random import randint

fortune: int=randint(0,40)

if fortune <= 20:
    if fortune <= 10:
        print ("You a real one.")
    else:
        print ("Somebody new will enjoy your presence today.")
else:
    if fortune <= 30:
        print ("Your current path will lead to personal glory.")
    else:
        print ("Some table is about to turn.")
print ("Now, go spread good vibes!")