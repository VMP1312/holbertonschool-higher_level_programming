#!/usr/bin/python3
"""
Add numbers
a & b must be integer or float
return a + b
"""


def add_integer(a, b=98):
    """Add module
    a & b must be integer or float
    return a + b"""

    if type(a) is int or type(a) is float:
        a = int(a)
    else:
        raise TypeError('a must be an integer')
    if type(b) is int or type(b) is float:
        b = int(b)
    else:
        raise TypeError('b must be an integer')
    return a + b
