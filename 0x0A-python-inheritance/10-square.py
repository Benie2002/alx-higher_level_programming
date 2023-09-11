#!/usr/bin/python3

""" Define square module """
Square = __import__('10-square').Square


class Square(Rectangle):
    """ Square class body """

    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size
        Rectangle.__init__(self, size, size)

    def area(self):
        return self.__size * self.__size
