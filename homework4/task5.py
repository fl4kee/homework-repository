"""
This task is optional.
Write a generator that takes a number N as an input
and returns a generator that yields N FizzBuzz numbers*
Don't use any ifs, you can find an approach for the implementation in this video**.
Definition of done:
 - function is created
 - function is properly formatted
 - function has tests
>>> list(fizzbuzz(5))
['1', '2', 'fizz', '4', 'buzz']
"""
from typing import Generator


def fizzbuzz(numbers: int) -> Generator[str, None, None]:
    for number in range(1, numbers + 1):
        yield "fizz" * (not number % 3) + "buzz" * (not number % 5) or str(number)
