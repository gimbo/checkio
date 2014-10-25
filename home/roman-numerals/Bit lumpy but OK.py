#!/usr/bin/env python3

"""Roman numerals

Roman numerals come from the ancient Roman numbering system. They are
based on specific letters of the alphabet which are combined to signify
the sum (or, in some cases, the difference) of their values. The first
ten Roman numerals are:

I, II, III, IV, V, VI, VII, VIII, IX, and X.

The Roman numeral system is decimal based but not directly positional
and does not include a zero. Roman numerals are based on combinations of
these seven symbols:

Symbol Value
I 1 (unus)
V 5 (quinque)
X 10 (decem)
L 50 (quinquaginta)
C 100 (centum)
D 500 (quingenti)
M 1,000 (mille)

More additional information about roman numerals can be found on the
Wikipedia article.

For this task, you should return a roman numeral using the specified
integer value ranging from 1 to 3999.

Input: A number as an integer.

Output: The Roman numeral as a string.

How it is used: This is an educational task that allows you to explore
different numbering systems. Since roman numerals are often used in the
typography, it can alternatively be used for text generation. The year
of construction on building faces and cornerstones is most often written
by Roman numerals. These numerals have many other uses in the modern
world and you read about it here... Or maybe you will have a customer
from Ancient Rome ;-)

Precondition: 0 < number < 4000

"""


def checkio(data):

    rest, units = divmod(data, 10)
    rest, tens = divmod(rest, 10)
    rest, hundreds = divmod(rest, 10)
    rest, thousands = divmod(rest, 10)

    parts = ['M'] * thousands

    romans(parts, hundreds, 'C', 'M', 'D')
    romans(parts, tens,     'X', 'C', 'L')
    romans(parts, units,    'I', 'X', 'V')

    return ''.join(parts)


def romans(parts, count, unit, top, half):
    if count == 9:
        parts.extend([unit, top])
    elif count == 4:
        parts.extend([unit, half])
    else:
        if count >= 5:
            parts.append(half)
            count = count - 5
        parts.extend([unit] * count)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
