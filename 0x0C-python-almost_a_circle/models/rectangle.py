#!/usr/bin/python3
"""Rectangle class"""


from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Rectangle, width getter"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Rectangle, width setter"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """Rectangle, height getter"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Rectangle, Height setter"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """Rectangle, X getter"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """Rectangle, X setter"""
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """Rectngle, Y getter"""
        return (self.__y)

    @y.setter
    def y(self, value):
        """Rectangle, Y setter"""
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """Rectangle, Area"""
        return (self.__width * self.__height)

    def display(self):
        """Rectangle Display"""
        for y in range(self.__y):
            print("")
        for h in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for w in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Rectangle __str__"""
        nm = type(self).__name__
        idd = self.id
        x = self.x
        y = self.y
        w = self.width
        h = self.height
        return "[{}] ({}) {}/{} - {}/{}".format(nm, idd, x, y, w, h)

    def update(self, *args, **kwargs):
        """Rectangle Update"""
        for cnt, st in enumerate(args):
            if cnt == 0:
                self.id = st
            elif cnt == 1:
                self.width = st
            elif cnt == 2:
                self.height = st
            elif cnt == 3:
                self.x = st
            elif cnt == 4:
                self.y = st
        if args is None or len(args) == 0:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'width' in kwargs:
                self.__width = kwargs['width']
            if 'height' in kwargs:
                self.__height = kwargs['height']
            if 'x' in kwargs:
                self.__x = kwargs['x']
            if 'y' in kwargs:
                self.__y = kwargs['y']

    def to_dictionary(self):
        """Rectangle Dictionary"""
        dic = {}
        dic["id"] = self.id
        dic["width"] = self.width
        dic["height"] = self.height
        dic["x"] = self.x
        dic["y"] = self.y
        return dic
