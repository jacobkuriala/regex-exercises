from Point import Point
import math


class ConvexPolygon(object):
    """
    This class represents a convex Polygon in 2-d space
    """
    def __init__(self, *args):
        """
        This function initializes the ConvexPolygon class
        It sets the points in an ordered position from leftmost
        to rightmost.
        :param args: These are the points of the convex polygon
        Assumption:The points will be provided in the counter-clockwise
        direction
        """
        self.points = []
        self.upperchain = []
        self.lowerchain = []
        # finding the min and max x values help us to find the
        # leftmost and rightmost points so we can cut the convex polygon
        # into upper and lower parts
        if len(args) < 3:
            raise ValueError('Polygon must have a minimum of 3 points')

        self.minxpoint = args[0]
        self.maxxpoint = args[0]
        for point in args:
            if type(point) is not Point:
                raise TypeError('ConvexPolygon: Must be initialized with points')
            else:
                # append point to list of points
                self.points.append(point)
                # also find min and max x points so we can divide the
                # polygon into upper and lower chains.
                if point.x < self.minxpoint.x:
                    self.minxpoint = point
                elif point.x == self.minxpoint.x and point.y < self.minxpoint.y:
                    self.minxpoint = point
                if point.x > self.maxxpoint.x:
                    self.maxxpoint = point
                elif point.x == self.maxxpoint.x and point.y > self.maxxpoint.y:
                    self.maxxpoint = point
        minindex = self.points.index(self.minxpoint)

        orderedpoints = []

        for i in range(minindex, minindex + len(self.points)):
            j = i
            if j >= len(self.points):
                j = (j % len(self.points))
            orderedpoints.append(self.points[j])
        self.points = orderedpoints
        minindex = self.points.index(self.minxpoint)
        maxindex = self.points.index(self.maxxpoint)

        for j in range(len(orderedpoints)):
            if j > maxindex:
                self.upperchain.append(self.points[j])
            if j == maxindex or j == minindex:
                self.upperchain.append(self.points[j])
                self.lowerchain.append(self.points[j])
            if minindex < j < maxindex:
                self.lowerchain.append(self.points[j])
        print(self.points)
        print(self.upperchain)
        print(self.lowerchain)

    def inside(self, p):
        """
        determines if point p is in this convexpolygon
        :param p:
        :return:
        """
        if self.ispointbelowupperchain(p) and self.ispointabovelowerchain(p):
            return True
        else:
            return False

    def ispointbelowupperchain(self, p):
        """
        This function checks if the point p in on or below the upper
        chain
        :return: Boolean
        """
        foundpoint, foundpointnext = self.findclosestlessthanpoint(self.upperchain, p)
        if self.is_between(foundpoint, p, foundpointnext):
            return True
        isvertical, m, c = self.getlineequation(foundpoint, foundpointnext)
        #y = mx+c
        if p.y - (m*p.x) - c < 0:
            return True
        else:
            return False

    def ispointabovelowerchain(self, p):
        """
        This function checks if the point p in on or below the upper
        chain
        :return: Boolean
        """
        foundpoint, foundpointnext = self.findclosestlessthanpoint(self.lowerchain, p)
        if self.is_between(foundpoint, p, foundpointnext):
            return True

        isvertical, m, c = self.getlineequation(foundpoint, foundpointnext)
        #y = mx+c
        if p.y - (m*p.x) - c > 0:
            return True
        else:
            return False


    def findclosestlessthanpoint(self, chain, p):
        """

        :param chain:
        :param p:
        :return:
        """
        for i in range(len(chain)-1):
            currentpoint, nextpoint = chain[i], chain[i+1]
            if currentpoint.x <= p.x < nextpoint.x and not self.islinevertical(currentpoint,nextpoint):
                foundpoint = currentpoint
                foundpointnext = nextpoint
                break
        else:
            pos = len(chain)-2
            foundpoint = chain[pos]
            foundpointnext = chain[pos+1]
            while self.islinevertical(foundpoint,foundpointnext) and pos >=0:
                pos -= 1
                foundpoint = chain[pos]
                foundpointnext = chain[pos + 1]

        return foundpoint, foundpointnext

    def islinevertical(self,a,b):
        return b.x - a.x == 0

    def getlineequation(self, a, b):
        """
        Calculates the equation of the line given 2 points
        y = mx + c
        :param a: one point on the line
        :param b: second point on the line
        :return: m , c
        """

        # if slope is not defined
        if b.x-a.x == 0:
            m = 'irrelevant'
            c = b.x
            return True, m, c
        m = (b.y- a.y) / (b.x-a.x)
        c = a.y - (m * a.x)
        return False, m, c

    def distance(self,a, b):
        return math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)

    def is_between(self, a, c, b):
        return self.distance(a, c) + self.distance(c, b) == self.distance(a, b)

if __name__=="__main__":
    points = [Point(*p) for p in [(0, 0), (2, 0), (2, 2), (0, 2)]]
    polygon = ConvexPolygon(*points)

    # test ordering 2
    points = [Point(*p) for p in [(2, 2), (0, 2), (0, 0), (2, 0)]]
    polygon = ConvexPolygon(*points)
    # print(polygon.points[0][0])
    p = Point(3, 0)
    q = Point(0, 0)
    r = Point(1, 1)

    closest, closestnext = polygon.findclosestlessthanpoint(polygon.lowerchain, p)
    #print(closest, " ", closestnext)
    print(polygon.inside(p))
    print(polygon.inside(q))
    print(polygon.inside(r))





