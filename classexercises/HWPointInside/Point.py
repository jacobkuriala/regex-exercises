"""
Python Take home assignment Assignment
    This module has a class which represents a point in a 2 dimensional space
@Author: Jacob Kattampilly
"""


class Point(object):
    """
    This class represents a point in a 2 dimensional space
    """

    @property
    def x(self):
        return self.coordinates[0]

    @property
    def y(self):
        return self.coordinates[1]

    def __str__(self):
        """

        :return:
        """
        if self.coordinates:
            return '[' +str(self.x) + ', ' + str(self.y) + ']'
        else:
            return 'No Dimensions:'

    def __repr__(self):
        return self.__str__()

    def __init__(self, *args):
        """
        Constructor: used to set all the coordinates of an array.
        :param args: Coordinates of the Point in n-dimensional space.
        """
        self.coordinates = [i for i in args]
        if self.get_dimensions() != 2:
            raise ValueError('Point cannot have more than 2 dimensions.')

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
