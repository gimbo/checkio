#!/usr/bin/env python3

"""Feed Pigeons

I start to feed one of the pigeons. A minute later two more fly by and a
minute after that another 3. Then 4, and so on (Ex: 1+2+3+4+...). One
portion of food lasts a pigeon for a minute, but in case there's not
enough food for all the birds, the pigeons who arrived first ate
first. Pigeons are hungry animals and eat without knowing when to
stop. If I have N portions of bird feed, how many pigeons will be fed
with at least one portion of wheat?

Input: A quantity of portions wheat as a positive integer.

Output: The number of fed pigeons as an integer.

How it is used: This task illustrates how we can model various
situations. Of course, the model has a limited approximation, but
often-times we don't need a perfect model.

Precondition: 0 < N < 10 ** 5.

"""


def checkio(feed):
    incoming = 1  # How many pigeons incoming at each step?
    pigeons = 0   # How many pigeons have we got in totoal?
    fed = 0       # How many pigeons have eaten at least once?
    while feed > 0:
        feed = max(feed - pigeons, 0)     # Old pigeons eat
        pigeons = pigeons + incoming      # New pigeons arrive
        new_eaters = min(feed, incoming)  # How many new pigeons get to eat?
        fed = fed + new_eaters
        feed = feed - new_eaters
        incoming = incoming + 1
    return fed


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"
