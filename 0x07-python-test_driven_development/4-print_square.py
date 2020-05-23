#!/usr/bin/python3
"""
Prints a square
Use # to draw
Return none
"""


def print_square(size):
    """Prints a square
    Use # to draw
    Return none"""

    if isinstance(size, int):
        for Rw in range(size):
            for Cl in range(size):
                print('#', end="")
            print()
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')