"""
This module tests the point.py module
@Author: Jacob Kattampilly
"""
import unittest
from Point import Point
from ConvexPolygon import ConvexPolygon


class PointandConvexPolygonTest(unittest.TestCase):
    """
    This class is used to test then point.py module
    """
    '''Point Tests'''
    def test_point_creation(self):
        """
        :return:none
        """
        mypoint = Point(1,2)
        self.assertEquals(1, mypoint[0])
        self.assertEquals(2, mypoint[1])

    def test_point_iteration(self):
        """
        :return:none
        """
        mypoint = Point( 3, 4)
        index = 0
        for coordinate in mypoint:
            self.assertEqual(mypoint[index], coordinate)
            index += 1

    def test_point_set_value(self):
        """
        I had implemented __setitem__ but unfortunately Pylist
        complains when i use it with 3 parameters so i implemented
        this differently
        :return:none
        """
        mypoint = Point(1, 2)
        mypoint.setitem(0, 2)
        mypoint[1] = 100
        self.assertEqual(mypoint.coordinates[0], 2)
        self.assertEqual(mypoint.coordinates[1], 100)

    def test_point_dimensions(self):
        """
        :return:none
        """
        mypoint = Point(1,2)
        self.assertEqual(mypoint.get_dimensions(), 2)

    def test_point_MultiplePointCreation(self):
        points = [Point(*p) for p in [(0, 0), (2, 0), (2, 2), (0, 2)]]
        self.assertEquals(points[1][0], 2 )

    '''Convex Hull Tests'''
    def test_polygon_Creation(self):
        points = [Point(*p) for p in [(0, 0), (2, 0), (2, 2), (0, 2)]]
        polygon = ConvexPolygon(*points)
        self.assertEquals(polygon.points[0].x, 0)
        self.assertEquals(polygon.points[0].y, 0)

        self.assertEquals(polygon.points[1].x, 2)
        self.assertEquals(polygon.points[1].y, 0)

        self.assertEquals(polygon.points[2].x, 2)
        self.assertEquals(polygon.points[2].y, 2)

        self.assertEquals(polygon.points[3].x, 0)
        self.assertEquals(polygon.points[3].y, 2)

    def test_polygon_findclosestlessthanpoint(self):
        points = [Point(*p) for p in [(0, 0), (2, 0), (2, 2), (0, 2)]]
        polygon = ConvexPolygon(*points)
        p = Point(3, 0)
        point , nextpoint = polygon.findclosestlessthanpoint(polygon.lowerchain,p)
        self.assertEquals(point.x,0)
        self.assertEquals(point.y, 0)
        self.assertEquals(nextpoint.x, 2)
        self.assertEquals(nextpoint.y, 0)

    def test_ispointabovelowerchain(self):
        points = [Point(*p) for p in [(0, 0), (2, 0), (2, 2), (0, 2)]]
        polygon = ConvexPolygon(*points)
        p = Point(3, 0)
        self.assertFalse(polygon.ispointabovelowerchain(p))



if __name__ == '__main__':
    unittest.main()
