#!/usr/bin/python3
"""
Base class tests using unittests
"""
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """class to test Base class
    """

    def test_class_instance(self):
        """test if obj is an instance
        of Base class
        """

        b1 = Base()
        self.assertIsInstance(b1, Base)

    def test_class_with_no_args(self):
        """test the obj when no args
        are passed to constructor
        """

        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)
