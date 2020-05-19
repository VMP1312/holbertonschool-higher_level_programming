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

    def my_print(self):
        """print the Square"""
        size = self.__size
        if size is not 0:
            for column in range(size):
                for row in range(size):
                    print("#", end="")
                print("")
        print("")
