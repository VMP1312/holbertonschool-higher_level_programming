#!/usr/bin/python3
"""
Module.
"""


def write_file(filename="", text=""):
    """Writes a string to a text file"""
    with open(filename, 'w') as fl:
        wr = fl.write(text)
    return wr
