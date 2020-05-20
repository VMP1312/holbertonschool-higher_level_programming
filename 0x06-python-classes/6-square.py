#!/usr/bin/python3
"""Create"""


class Square:
    """Class"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialization"""
        self.__size = size
        self.position = position

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
        pos = self.__position
        if size is not 0:
            for check in range(pos[1]):
                print()
            for move in range(size):
                for spaces in range(pos[0]):
                    print(" ", end="")
                for hasht in range(size):
                    print("#", end="")
                print()
        else:
            print("")

    @property
    def position(self):
        """Position"""
        return self.__position

    @position.setter
    def position(self, posvalue):
        """Setter"""
        if type(posvalue) is not tuple or len(posvalue) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(type(check) is not int for check in posvalue):
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(val < 0 for val in posvalue):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = posvalue
