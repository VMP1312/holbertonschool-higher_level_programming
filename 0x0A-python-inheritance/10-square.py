#!/usr/bin/python3
"""
Module.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class"""

    def __init__(self, size):
        """Initialize"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area"""
        return self.__size ** 2
