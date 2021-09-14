"""
Write a function that takes a number N as an input and returns N FizzBuzz numbers*
Write a doctest for that function.
Definition of done:
 - function is created
 - function is properly formatted
 - function has doctests
 - doctests are run with pytest command
You will learn:
 - the most common test task for developers
 - how to write doctests
 - how to run doctests
assert fizzbuzz(5) == ["1", "2", "fizz", "4", "buzz"]
* https://en.wikipedia.org/wiki/Fizz_buzz
** Энциклопедия профессора Фортрана page 14, 15, "Робот Фортран, чисть картошку!"
"""
from typing import List


def fizzbuzz(n: int) -> List[str]:
    """
    Returns n numbers. Number that is divisible by 3 is replaced with fizz
    Number that is divisible by 3 is replaced with buzz
    If number is divisible by 3 and 5 it is replaced with fizzbuzz
    >>> fizzbuzz(14)
    ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11', 'fizz', '13', '14']
    """
    fizzbuzz_list = []
    for number in range(1, n + 1):
        fizzbuzz_list.append("fizz" * (not number % 3) + "buzz" * (not number % 5) or str(number))
    return fizzbuzz_list
