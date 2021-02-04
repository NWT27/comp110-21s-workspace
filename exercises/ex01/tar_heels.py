"""An exercise in remainders and boolean logic."""

__author__ = "730400848"


number: int = int(input("enter an int: "))

if number % 2 == 0 and number % 7 == 0:
    print ("TAR HEELS")
else:
    if number % 7 == 0:
        print ("HEELS")
    if number % 2 == 0: 
        print ("TAR") 
if not number % 2 == 0 and not number % 7 == 0:
    print ("Carolina")

