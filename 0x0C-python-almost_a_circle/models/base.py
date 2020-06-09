#!/usr/bin/python3
"""
Base Class
"""
import json
from os import path


class Base:
    """Base Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializate"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        "To Json"
        if list_dictionaries is None:
            list_dictionaries = []
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        "Save"
        dic = []
        if list_objs:
            for cnt in list_objs:
                dic.append(cls.to_dictionary(cnt))
        with open(cls.__name__ + ".json", "w") as file:
            file.write(cls.to_json_string(dic))

    @staticmethod
    def from_json_string(json_string):
        "From Json"
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        "Create"
        if cls.__name__ is "Rectangle":
            from models.rectangle import Rectangle
            object = Rectangle(1, 1)
        elif cls.__name__ is "Square":
            from models.square import Square
            object = Square(1)
        object.update(**dictionary)
        return (object)

    @classmethod
    def load_from_file(cls):
        "Base Classmetohd"
        if not path.isfile(cls.__name__ + ".json"):
            return []
        else:
            with open(cls.__name__ + ".json", "r") as f:
                return[cls.create(**d) for d in cls.from_json_string(f.read())]
