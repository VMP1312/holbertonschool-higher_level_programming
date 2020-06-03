#!/usr/bin/python3
"""
Module.
"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file"""
    with open(filename, 'a') as fl:
        wr = fl.write(text)
    return wr
