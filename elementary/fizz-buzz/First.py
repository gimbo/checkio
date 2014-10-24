#!/usr/bin/env python3

"""Fizz Buzz

"Fizz buzz" is a word game we will use to teach the robots about
division. Let's learn computers.

You should write a function that will receive a positive integer and return:
"Fizz Buzz" if the number is divisible by 3 and by 5;
"Fizz" if the number is divisible by 3;
"Buzz" if the number is divisible by 5;
The number as a string for other cases.

Input: A number as an integer.

Output: The answer as a string.

How it is used: Here you can learn how to write the simplest function
and work with if-else statements.

Precondition: 0 < number <= 1000

"""


def checkio(number):
    fizz = (number % 3) == 0
    buzz = (number % 5) == 0
    if fizz and buzz:
        return 'Fizz Buzz'
    elif fizz:
        return 'Fizz'
    elif buzz:
        return 'Buzz'
    else:
        return str(number)


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert checkio(6) == "Fizz", "6 is divisible by 3"
    assert checkio(5) == "Buzz", "5 is divisible by 5"
    assert checkio(7) == "7", "7 is not divisible by 3 or 5"
