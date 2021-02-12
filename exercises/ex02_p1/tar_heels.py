"""Tar Heels exercise redux as a structured program."""

__author__ = "730400848"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    choice: int = int(input("Enter an int: "))
    print(tar_heels(choice))
    return None


def tar_heels(choice: int) -> str:
    """The definition of the tar_heel function."""
    if choice % 2 == 0 and choice % 7 == 0:
        return("TAR HEELS")
    else:
        if choice % 7 == 0:
            return("HEELS")
        if choice % 2 == 0: 
            return("TAR") 
        if not choice % 2 == 0 and not choice % 7 == 0:
            return("CAROLINA")
        return "None"


if __name__ == "__main__":
    main()