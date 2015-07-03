#!/usr/bin/env python3

"""Three words

Let's teach the Robots to distinguish words and numbers.

You are given a string with words and numbers separated by whitespaces
(one space). The words contains only letters. You should check if the
string contains three words in succession. For example, the string
"start 5 one two three 7 end" contains three words in succession.

Input: A string with words.

Output: The answer as a boolean.

How it is used: This teaches you how to work with strings and introduces
some useful functions.

Precondition: The input contains words and/or numbers. There are no
mixed words (letters and digits combined).
0 < len(words) < 100

"""


def checkio(words):
    return "aaa" in ''.join('a' if w.isalpha() else ' ' for w in words.split())


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World hello") is True, "Hello"
    assert checkio("He is 123 man") is False, "123 man"
    assert checkio("1 2 3 4") is False, "Digits"
    assert checkio("bla bla bla bla") is True, "Bla Bla"
    assert checkio("Hi") is False, "Hi"
