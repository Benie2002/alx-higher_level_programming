#!/usr/bin/python3
"""Base module
base class for my Rectangle class
"""

from . import base


class Rectangle(base.Base):
    """Rectangle class
    subclass of Base class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Rectangle class
        constructor

        args:
            width (int): rectangle width
            height (int): rectangle width
            x (int): starting point
            y (int): starting point
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        super().__init__(id)

    @property
    def width(self):
        """
        returns the width set by setter
        """
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        self.__width = width

    @property
    def height(self):
        """
        returns height
        """
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height

    @property
    def x(self):
        """
        returns x
        """
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x

    @property
    def y(self):
        """
        returns y
        """
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y

    def area(self):
        """
        returns the area value of the rectangle instance
        """
        return self.__width * self.__height

    def display(self):
        """
        prints in stdout the Rectangle instance with character #
        """
        for i in range(self.y):
            print()
        for r in range(self.height):
            print(' ' * self.x, end="")
            for c in range(self.width):
                print('#', end="")
            print()

    def __str__(self):
        """
        returns a string representation of the object
        """
        return "[{}] ({}) {}/{} - {}/{}".format(
                type(self).__name__,
                self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """updates the attributes of the class
        """
        if len(args) > 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.width = arg
                if i == 2:
                    self.height = arg
                if i == 3:
                    self.x = arg
                if i == 4:
                    self.y = arg
        elif len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'width':
                    self.width = value
                if key == 'height':
                    self.height = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value

    def to_dictionary(self):
        """returns a dictionary of Rectangle
        """
        my_dict = {}
        for key, value in self.__dict__.items():
            if key == '_Rectangle__width':
                my_dict['width'] = value
            if key == 'id':
                my_dict['id'] = value
            if key == '_Rectangle__y':
                my_dict['y'] = value
            if key == '_Rectangle__height':
                my_dict['height'] = value
            if key == '_Rectangle__x':
                my_dict['x'] = value
        return my_dict
