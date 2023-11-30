#!/usr/bin/python3
"""tests for the Rectangle class
using unittest
"""
import unittest
import io
import sys
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    """class contains tests for the rectangle class
    """

    def test_instance(self):
        """Rectange class unittest"""
        r5 = Rectangle(10, 2)
        self.assertIsInstance(r5, Base)
        self.assertIsInstance(r5, Rectangle)

    def test_with_arguments(self):
        """Rectangle test with args and without"""
        r7 = Rectangle(3, 5)
        r02 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r7.id, 10)
        self.assertEqual(r02.id, 12)
        self.assertEqual(r7.x, 0)
        self.assertEqual(r7.y, 0)

    def test_with_attributes(self):
        """test Rectangle class using wrong
        data types
        """
        r8 = Rectangle(10, 2)
        with self.assertRaises(AttributeError):
            r8.__width
        with self.assertRaises(AttributeError):
            r8.__height
        with self.assertRaises(AttributeError):
            r8.__x
        with self.assertRaises(AttributeError):
            r8.__y

    def test_attr_with_wrong_types(self):
        """test Rectangle class using wrong values
        """
        with self.assertRaises(TypeError):
            r9 = Rectangle('a', 2)
        with self.assertRaises(TypeError):
            r10 = Rectangle(2, 'a')
        with self.assertRaises(TypeError):
            r11 = Rectangle(2, 2, 'a')
        with self.assertRaises(TypeError):
            r12 = Rectangle(2, 2, 2, 'a')

    def test_attr_with_wrong_range(self):
        """test the attributes for wrong ranges
        """
        with self.assertRaises(ValueError):
            r13 = Rectangle(0, 2)
        with self.assertRaises(ValueError):
            r14 = Rectangle(2, 0)
        with self.assertRaises(ValueError):
            r15 = Rectangle(-2, 2)
        with self.assertRaises(ValueError):
            r16 = Rectangle(2, -2)
        with self.assertRaises(ValueError):
            r17 = Rectangle(2, 2, -1)
        with self.assertRaises(ValueError):
            r18 = Rectangle(2, 2, 0, -1)

    def test_area_method(self):
        """Tets for the area method in Rectangle
        """
        r19 = Rectangle(10, 10)
        self.assertEqual(r19.area(), 100)

    def test_display_method(self):
        """Test the display method in
        class Rectangle
        """
        output = io.StringIO()
        sys.stdout = output
        my_r = Rectangle(2, 2, 2, 1)
        my_r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "\n  ##\n  ##\n")

    def test_str_method(self):
        """tests the str method in class
        """
        r20 = Rectangle(2, 2)
        str_rep = r20.__str__()
        self.assertEqual(str_rep, '[Rectangle] (8) 0/0 - 2/2')
        r02 = Rectangle(2, 2, 0, 0, 12)
        str_rep2 = r02.__str__()
        self.assertEqual(str_rep2, '[Rectangle] (12) 0/0 - 2/2')

    def test_update_method(self):
        """tests the update method in Rectangle class
        with args
        """
        r21 = Rectangle(10, 10, 10, 10)
        r21.update(89)
        self.assertEqual(r21.id, 89)
        r21.update(89, 2)
        self.assertEqual(r21.width, 2)
        r21.update(89, 2, 3)
        self.assertEqual(r21.height, 3)
        r21.update(89, 2, 3, 4)
        self.assertEqual(r21.x, 4)
        r21.update(89, 2, 3, 4, 5)
        self.assertEqual(r21.y, 5)

    def test_update_method(self):
        """test the update method in Rectangle class with kwargs
        """
        r22 = Rectangle(10, 10, 10, 10)
        r22.update(height=1)
        str_rep = r22.__str__()
        self.assertEqual(str_rep, '[Rectangle] (9) 10/10 - 10/1')
        r22.update(width=1, x=2)
        str_rep = r22.__str__()
        self.assertEqual(str_rep, '[Rectangle] (9) 2/10 - 1/1')
        r22.update(y=1, width=2, x=3, id=89)
        str_rep = r22.__str__()
        self.assertEqual(str_rep, '[Rectangle] (89) 3/1 - 2/1')
        r22.update(x=1, height=2, y=3, width=4)
        str_rep = r22.__str__()
        self.assertEqual(str_rep, '[Rectangle] (89) 1/3 - 4/2')
