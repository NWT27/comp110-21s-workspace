"""EX03 - prime functions."""

__author__: str = "730400848"


def main() -> None:
    """Entrypoint of the program."""
    # Put print statements here to test your function
    print(is_prime(20))
    print(is_prime(2))
    print(is_prime(3))
    # ex. print(is_prime(5)), print(list_primes(10, 20))
    print(is_prime(5))
    print(list_primes(3, 7))
    print(list_primes(10, 20))
    print(list_primes(25, 28))
    print(list_primes(-1, 5))


def is_prime(number: int) -> bool:
    """A function to determine if a number is prime."""
    i = 2
    if number == -1 or number == 0 or number == 1:
        return False
    while number > i: 
        if number % i == 0:
            return False
        i += 1
    return True


def list_primes(start: int, stop: int) -> list[int]:
    """A function for checking a list for primes."""
    i = start
    list_of_primes: list[int] = []
    while i < stop:
        prime_check: bool = is_prime(i)
        if prime_check == True: 
            list_of_primes.append(i)
        i += 1
    return list_of_primes




if __name__ == "__main__":
    main()