"""Testing Rectangle class"""


import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """ Suite to test Rectangle class """

    def setUp(self):
        """ Method invoked for each test """
        Base._Base__nb_objects = 0

    def test_new_rectangle(self):
        """ Test Rectangle"""

        setrec = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(setrec.width, 1)
        self.assertEqual(setrec.height, 2)
        self.assertEqual(setrec.x, 3)
        self.assertEqual(setrec.y, 4)
        self.assertEqual(setrec.id, 5)
