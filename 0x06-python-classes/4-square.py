#!/usr/bin/python3
"""Create"""


class Square:
    """Class"""
    def __init__(self, size=0):
        """Initialization"""
        self.__size = size

    def area(self):
        """Area"""
        return self.__size ** 2

    @property
    def size(self):
        """Size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Define"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
