#!/usr/bin/env python3

"""The Most Wanted Letter

You are given a text, which contains different english letters and
punctuation symbols. You should find the most frequent letter in the
text. The letter returned must be in lower case.  While checking for the
most wanted letter, casing does not matter, so for the purpose of your
search, "A" == "a". Make sure you do not count punctuation symbols,
digits and whitespaces, only letters.

qIf you have two or more letters with the same frequency, then return the letter which comes first in the latin alphabet. For example -- "one" contains "o", "n", "e" only once for each, thus we choose "e".

Input: A text for analysis as a string (unicode for py2.7).

Output: The most frequent letter in lower case as a string.

How it is used: For most decryption tasks you need to know the frequency
of occurrence for various letters in a section of text. For example: we
can easily crack a simple addition or substitution cipher if we know the
frequency in which letters appear. This is interesting stuff for
language experts!

Precondition:
A text contains only ASCII symbols.
0 < len(text) <= 105

"""

from collections import Counter
import re


def checkio(text):
    letters = re.sub("[^a-zA-Z]", "", text)
    counts = Counter(letters.lower())
    candidates = [k for (k, v) in counts.items() if v == max(counts.values())]
    return sorted(candidates)[0]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
