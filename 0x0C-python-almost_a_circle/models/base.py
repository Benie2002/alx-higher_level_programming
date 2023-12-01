#!/usr/bin/python3
"""base
my class
"""
import json


class Base(object):
    """Base class
    base class for all other classes
    """
    __no_objects = 0

    def __init__(self, id=None):
        """__init__ is a constructor for
        base class
        """

        if id is not None:
            self.id = id
        else:
            Base.__no_objects += 1
            self.id = Base.__no_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns a JSON string representation of
        list_dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        if len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of
        list_objs to a file
        """
        obj_list = []
        obj_string = "[]"

        if list_objs is not None:
            for obj in list_objs:
                obj_list.append(obj.to_dictionary())

        if len(obj_list) > 0:
            obj_string = Base.to_json_string(obj_list)

        with open(cls.__name__ + ".json", 'w') as f:
            f.write(obj_string)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON
        sring representation json_string
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes
        already set
        """
        obj = None
        if cls.__name__ == 'Rectangle':
            obj = cls(1, 1)
        elif cls.__name__ == 'Square':
            obj = cls(1)
        cls.update(obj, **dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """returns a list of instances
        """
        my_list = []
        try:
            with open(cls.__name__ + ".json", 'r', encoding='utf-8') as f:
                my_output = cls.from_json_string(f.read())
                for obj in my_output:
                    my_list.append(cls.create(**obj))
        except Exception:
            return []
        return my_list
