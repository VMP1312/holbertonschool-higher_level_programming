#!/usr/bin/python3
"Square class"


from models.rectangle import Rectangle


class Square(Rectangle):
    "Square class"

    def __init__(self, size, x=0, y=0, id=None):
        "Initializate"
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        "Size"
        return (self.__width)

    @size.setter
    def size(self, value):
        "Setter"
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value
        self.__height = value

    def __str__(self):
        "str"
        nm = type(self).__name__
        idd = self.id
        x = self.x
        y = self.y
        w = self.width
        return "[{}] ({}) {}/{} - {}".format(nm, idd, x, y, w)

    def update(self, *args, **kwargs):
        "Rectangle Update"
        for cnt, st in enumerate(args):
            if cnt == 0:
                self.id = st
            elif cnt == 1:
                self.size = st
            elif cnt == 2:
                self.x = st
            elif cnt == 3:
                self.y = st
        if args is None or len(args) == 0:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """Rectangle Dictionary"""
        dic = {}
        dic["id"] = self.id
        dic["size"] = self.size
        dic["x"] = self.x
        dic["y"] = self.y
        return dic
