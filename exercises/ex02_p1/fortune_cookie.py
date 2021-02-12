"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "730400848"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    print(fortune_cookie())
    print("Now, go spread positive vibes!")


def fortune_cookie() -> str:
    """Defining fortune cookie function."""
    fortune: int = randint(0, 40)

    if fortune <= 20:
        if fortune <= 10:
            return("You a real one.")
        else:
            return("Somebody new will enjoy your presence today.")
    else:
        if fortune <= 30:
            return("Your current path will lead to personal glory.")
        else:
            return("Some table is about to turn.")


# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 
if __name__ == "__main__":
    main()