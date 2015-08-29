#!/usr/bin/env python3

"""The End of Other

For language training our Robots want to learn about suffixes.

In this task, you are given a set of words in lower case. Check whether
there is a pair of words, such that one word is the end of another (a
suffix of another). For example: {"hi", "hello", "lo"} -- "lo" is the
end of "hello", so the result is True.

Input: Words as a set of strings.

Output: True or False, as a boolean.

How it is used: Here you can learn about iterating through set type and
string data type functions.

Precondition: 2 <= len(words) < 30
all(re.match(r"\A[a-z]{1,99}\Z", w) for w in words)

"""

def checkio(words_set):
    for (i, word1) in enumerate(words_set):
        for (j, word2) in enumerate(words_set):
            if i != j and word1.endswith(word2):
                return True
    return False


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio({"hello", "lo", "he"}) is True, "helLO"
    assert checkio({"hello", "la", "hellow", "cow"}) is False, "hellow la cow"
    assert checkio({"walk", "duckwalk"}) is True, "duck to walk"
    assert checkio({"one"}) is False, "Only One"
    assert checkio({"helicopter", "li", "he"}) is False, "Only end"
