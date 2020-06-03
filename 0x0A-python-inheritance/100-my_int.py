#!/usr/bin/python3
"""
Module.
"""


class MyInt(int):
    """Class"""

    def __ne__(self, other):
        return super().__eq__(other)

    def __eq__(self, other):
        return super().__ne__(other)
