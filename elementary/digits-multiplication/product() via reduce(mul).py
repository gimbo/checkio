#!/usr/bin/env python3

"""Digits Multiplication

You are given a positive integer. Your function should calculate the
product of the digits excluding any zeroes.

For example: The number given is 123405. The result will be
1*2*3*4*5=120 (don't forget to exclude zeroes).

Input: A positive integer.

Output: The product of the digits as an integer.

How it is used: This task can teach you how to solve a problem with
simple data type conversion.

Precondition: 0 < number < 10 **6

"""

from functools import reduce
from operator import mul


def checkio(number):
    return reduce(mul, [int(x) for x in str(number) if int(x)], 1)


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
