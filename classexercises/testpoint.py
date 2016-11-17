"""
This module tests the point.py module
@Author: Jacob Kattampilly
"""
import unittest

from classexercises.point import Point


class PointTest(unittest.TestCase):
    """
    This class is used to test then point.py module
    """
    def test_point_creation(self):
        """
        :return:none
        """
        mypoint = Point(1, 2, 3, 4)
        self.assertEqual(mypoint[0], 1)

    def test_iteration(self):
        """
        :return:none
        """
        mypoint = Point(1, 2, 3, 4)
        index = 0
        for coordinate in mypoint:
            self.assertEqual(mypoint[index], coordinate)
            index += 1

    def test_set_value(self):
        """
        I had implemented __setitem__ but unfortunately Pylist
        complains when i use it with 3 parameters so i implemented
        this differently
        :return:none
        """
        mypoint = Point(1, 2, 3, 4)
        mypoint.setitem(1, 100)
        mypoint[2] = 50
        self.assertEqual(mypoint.coordinates[1], 100)
        self.assertEqual(mypoint.coordinates[2], 50)

    def test_dimensions(self):
        """
        :return:none
        """
        mypoint = Point()
        self.assertEqual(mypoint.get_dimensions(), 0)

if __name__ == '__main__':
    unittest.main()
