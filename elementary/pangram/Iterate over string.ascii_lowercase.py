#!/usr/bin/env python3

"""Pangram

A pangram (Greek: pan gramma, "every letter") or holoalphabetic sentence
for a given alphabet is a sentence using every letter of the alphabet at
least once. Perhaps you are familiar with the well known pangram "The
quick brown fox jumps over the lazy dog".

For this mission, we will use the latin alphabet (A-Z). You are given a
text with latin letters and punctuation symbols. You need to check if
the sentence is a pangram or not. Case does not matter.

Input: A text as a string.

Output: Whether the sentence is a pangram or not as a boolean.

How it is used: Pangrams have been used to display typefaces, test
equipment, and develop skills in handwriting, calligraphy, and
keyboarding for ages.

Precondition:

all(ch in (string.punctuation + string.ascii_letters + " ") for ch in text)
0 < len(text)

"""

import string


def check_pangram(text):
    for letter in string.ascii_lowercase:
        if letter not in text.lower():
            return False
    return True


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_pangram("The quick brown fox jumps over the lazy dog."), "brown fox"
    assert not check_pangram("ABCDEF"), "ABC"
    assert check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!"), "Bored?"
