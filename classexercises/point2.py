"""
Python In - Class Assignment
    This class represents a point in a d dimensional space
@Author: Jacob Kattampilly
"""


class Point(object):
    def __init__(self, *args):
        """
        Constructor: used to set all the coordinates of an array.
        :param args: Coordinates of the Point in n-dimensional space.
        """
        self.coordinates = [i for i in args]

    def __getitem__(self, key):
        """
        Returns the coordinate in the key-th dimension.
        :param key: dimension
        :return:
        """
        return self.coordinates[key]

    def __setitem__(self, key, value):
        """
        :param key: dimension
        :param value: coordinate at key-th dimension
        :return:
        """
        self.setitem(self, key, value)

    def setitem(self, key, value):
        """
        this function exists solely because pyLint does
        not accept classes as pure data containers.
        :param key: dimension
        :param value: coordinate at key-th dimension
        :return:
        """
        self.coordinates[key] = value

    def __iter__(self):
        """
        function called when we iterate through all values
        :return:
        """
        return iter(self.coordinates)

    def getdimensions(self):
        """
        :return: dimension of the space in which the point exists
        """
        return len(self.coordinates)
