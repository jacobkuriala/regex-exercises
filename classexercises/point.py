"""
Python In - Class Assignment
    This module has a class which represents a point in an n dimensional space
@Author: Jacob Kattampilly
"""


class Point:
    """
    This class represents a point in a d dimensional space
    """

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
        self.setitem(key, value)

    def setitem(self, key, value):
        """
        this function exists solely because pyLint does
        not accept classes as pure data containers.

        And pyLint also does not allow 3 arguments when using
        __setitem__(self,key,value) to have 3 arguments. Weird.
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

    def get_dimensions(self):
        """
        :return: dimension of the space in which the point exists
        """
        return len(self.coordinates)
