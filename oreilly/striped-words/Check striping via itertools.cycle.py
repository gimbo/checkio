#!/usr/bin/env python3

"""Striped Words

Our robots are always working to improve their linguistic skills. For
this mission, they research the latin alphabet and its applications.

The alphabet contains both vowel and consonant letters (yes, we divide
the letters).

Vowels -- A E I O U Y
Consonants -- B C D F G H J K L M N P Q R S T V W X Z

You are given a block of text with different words. These words are
separated by white-spaces and punctuation marks. Numbers are not
considered words in this mission (a mix of letters and digits is not a
word either). You should count the number of words (striped words) where
the vowels with consonants are alternating, that is; words that you
count cannot have two consecutive vowels or consonants. The words
consisting of a single letter are not striped -- do not count
those. Casing is not significant for this mission.

Input: A text as a string (unicode)

Output: A quantity of striped words as an integer.

How it is used: This idea in this task is a useful exercise for
linguistic research and analysis. Text processing is one of the main
tools used in the analysis of various books and languages and can help
translate print text to a digital format.

Precondition:The text contains only ASCII symbols.
0 < len(text) < 105

"""

from itertools import cycle
from re import split

VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"


def checkio(text):
    words = [w.upper() for w in split('\W+', text) if len(w) > 1 and w.isalpha()]
    return len([w for w in words if striped(w)])


def striped(word):
    vowel_states = [x in VOWELS for x in word]
    starter = (vowel_states[0], not vowel_states[0])
    return all([s == c for (s, c) in zip(vowel_states, cycle(starter))])


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
