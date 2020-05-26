#!/usr/bin/python3
def magic_string():
    setattr(magic_string, "cnt", getattr(magic_string, "cnt", -1) + 1)
    return "Holberton" + ", Holberton" * magic_string.cnt
