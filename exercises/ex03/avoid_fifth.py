"""EX03 - avoid_fifth function."""

__author__: str = "730400848"


def main() -> None:
    """Entrypoint of the program."""
    # Put print statements here to test your function
    print(avoid_fifth("I need to see if this works well or not."))
    print(avoid_fifth("Hehee ha ha."))
    # ex. print(avoid_fifth("hello there"))
    print(avoid_fifth("hello there"))


def avoid_fifth(word: str) -> str:
    """Avoid fifth function."""
    i = 0
    word_list: list[str] = []
    while i < len(word):
        word_list.append(word[i])
        i += 1
    i = 0
    while i < len(word_list):
        while ord(word_list[i]) == ord("E") or ord(word_list[i]) == ord("e"): 
            word_list.pop(i)
            i -= 1
        i += 1
    join_add: str = ""
    back_word: str = join_add.join(word_list)
    return back_word


if __name__ == "__main__":
    main()