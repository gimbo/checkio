#!/usr/bin/env python3

"""Min and Max

In this mission you should write you own py3 implementation (but you can
use py2 for this) of the built-in functions min and max. Some builtin
functions are closed here: import, eval, exec, globals. Don't forget you
should implement two functions in your code.

max(iterable, *[, key]) or min(iterable, *[, key])
max(arg1, arg2, *args[, key]) or min(arg1, arg2, *args[, key])

    Return the largest (smallest) item in an iterable or the
    largest(smallest) of two or more arguments.

    If one positional argument is provided, it should be an iterable. The
    largest (smallest) item in the iterable is returned. If two or more
    positional arguments are provided, the largest (smallest) of the
    positional arguments is returned.

    The optional keyword-only key argument specifies a function of one
    argument that is used to extract a comparison key from each list element
    (for example, key=str.lower).

    If multiple items are maximal (minimal), the function returns the first
    one encountered.

    -- Python Documentation (Built-in Functions)

Input: One positional argument as an iterable or two or more positional
arguments. Optional keyword argument as a function.

Output: The largest item for the "max" function and the smallest for the "min" function.

How it is used: This task will help you understand how some of the
built-in functions work on a more precise level.

Precondition: All test cases are correct and functions don't have to raise exceptions.

"""

from functools import partial
from operator import gt, lt


def _worker(op, *args, **kwargs):
    iterator = iter(args[0] if len(args) == 1 else args)
    key = kwargs.get("key", lambda x: x)
    current = next(iterator)
    for candidate in iterator:
        if op(key(candidate), key(current)):
            current = candidate
    return current


min = partial(_worker, lt)
max = partial(_worker, gt)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
