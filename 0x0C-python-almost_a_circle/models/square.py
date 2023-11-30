#!/usr/bin/python3
"""Square class
inherits from the Rectangle class
"""
from . import rectangle


class Square(rectangle.Rectangle):
    """imports from the Rectangle class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """constructor for the square class
        args:
            size (int): width or height
            x (int):
            y (int):
            id (int): object id
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns a string rep of Square class
        """
        return "[{}] ({}) {}/{} - {}".format(
                type(self).__name__,
                self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """
        sets and returns the width and height with the same value
        """
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """assigns attributes
        """
        if len(args) > 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.size = arg
                if i == 2:
                    self.x = arg
                if i == 3:
                    self.y = arg
        elif len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'size':
                    self.size = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value

    def to_dictionary(self):
        """returns a dictionary representation of
        the object
        """
        my_dict = {}
        for attr in ['id', 'size', 'x', 'y']:
            my_dict[attr] = getattr(self, attr)
        return my_dict
