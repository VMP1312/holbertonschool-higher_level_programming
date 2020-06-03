#!/usr/bin/python3
"""
Module.
"""


def read_file(filename=""):
    """Reads a text file"""
    with open(filename, 'r') as fl:
        read = fl.read()
    print(read, end="")
