#!/usr/bin/python3
"""
Programt that prints a name
prints a name
Return None
"""


def say_my_name(first_name, last_name=""):
    """Programt that prints a name
    prints a name
    Return None"""

    first = False
    last = False
    if type(first_name) is str:
        first = True
    else:
        raise TypeError("first_name must be a string")
    if type(last_name) is str:
        last = True
    else:
        raise TypeError("last_name must be a string")

    if first is True and last is False:
        print("My name is {} ".format(first_name))
    else:
        print("My name is {} {}".format(first_name, last_name))