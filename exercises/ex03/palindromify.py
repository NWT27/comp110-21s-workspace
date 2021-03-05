"""EX03 - palindromify function."""

__author__: str = "730400848"


def main() -> None:
    """Entrypoint of the program."""
    # Put print statements here to test your function
    print(palindromify("han", True))
    print(palindromify("red", True))
    print(palindromify("live on time ", False))
    # ex. print(palindromify("race", false))
    print(palindromify("race", False))


def palindromify(word: str, even_odd: bool) -> str:
    """A function to make any string a palindrome."""
    i = 0
    word_list: list[str] = []
    join_add: str = ""
    while i < len(word):
        word_list.append(word[i])
        i += 1
    if even_odd == True:
        rev_even_list: list = reversed(word_list)
        rev_even_new: str = join_add.join(rev_even_list)
        palindrome_even: str = (f"{word}{rev_even_new}")
        return palindrome_even
    if even_odd == False:
        i = len(word_list) - 1
        word_list.pop(i)
        rev_odd_list: list = reversed(word_list)
        rev_odd_new: str = join_add.join(rev_odd_list)
        palindrome_odd: str = (f"{word}{rev_odd_new}")
        return palindrome_odd


if __name__ == "__main__":
    main()