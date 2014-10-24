#!/usr/bin/env python3

"""House password.

Stephan and Sophia forget about security and use simple passwords for
everything. Help Nikola develop a password security check module. The
password will be considered strong enough if its length is greater than
or equal to 10 symbols, it has at least one digit, as well as containing
one uppercase letter and one lowercase letter in it. The password
contains only ASCII latin letters or digits.

Input: A password as a string (Unicode for python 2.7).

Output: Is the password safe or not as a boolean or any data type that
can be converted

How it is used: If you are worried about the security of your app or
service, you can check your users' passwords for complexity. You can use
these skills to require that your users passwords meet more conditions
(punctuations or unicode).

Precondition:
re.match("[a-zA-Z0-9]+", password)
0 < len(password) ≤ 64

"""

def checkio(data):
    if len(data) < 10:
        return False
    if not any([c.isdigit() for c in data]):
        return False
    if not any([c.islower() for c in data]):
        return False
    if not any([c.isupper() for c in data]):
        return False
    return True


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') is False, "1st example"
    assert checkio('bAse730onE4') is True, "2nd example"
    assert checkio('asasasasasasasaas') is False, "3rd example"
    assert checkio('QWERTYqwerty') is False, "4th example"
    assert checkio('123456123456') is False, "5th example"
    assert checkio('QwErTy911poqqqq') is True, "6th example"
