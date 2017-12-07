"""Point and Rectangle classes.

This code is in the public domain.

Point  -- point with (x,y) coordinates
Rect  -- two points, forming a rectangle

Taken from https://wiki.python.org/moin/PointsAndRectangles
"""

import math
from typing import Tuple

class Point:
    """A point identified by (x,y) coordinates.

    supports: +, -, *, /, str, repr

    length  -- calculate length of vector to point from origin
    distance_to  -- calculate distance between two points
    as_tuple  -- construct tuple (x,y)
    clone  -- construct a duplicate
    integerize  -- convert x & y to integers
    floatize  -- convert x & y to floats
    move_to  -- reset x & y
    slide  -- move (in place) +dx, +dy, as spec'd by point
    slide_xy  -- move (in place) +dx, +dy
    rotate  -- rotate around the origin
    rotate_about  -- rotate around another point
    """

    def __init__(self, x:float=0.0, y:float=0.0):
        self.x = x
        self.y = y

    @classmethod
    def from_tuple(cls, pt_as_tuple:Tuple[float,float]):
        return cls(x=pt_as_tuple[0],y=pt_as_tuple[1])

    def __iter__(self):
        return iter((self.x, self.y))

    def __getitem__(self, item):
        if item == 0:
            return self.x
        elif item == 1:
            return self.y
        else:
            raise RuntimeError("Index %d does not make sense in a point" % (item))

    def __attrs(self):
        """
        All attributes in a single representation.
        Returns:
            A tuple with all attributes.

        """
        return (self.x, self.y)

    def __eq__(self, other):
        return isinstance(other, Point) and self.__attrs() == other.__attrs()

    def __hash__(self):
        return hash(self.__attrs())

    def __add__(self, another_pt):
        """Point(x1+x2, y1+y2)"""
        return Point(self.x + another_pt.x, self.y + another_pt.y)

    def __sub__(self, another_point):
        """Point(x1-x2, y1-y2)"""
        return Point(self.x - another_point.x, self.y - another_point.y)

    def __isub__(self, another_point):
        self.x += another_point.x
        self.y += another_point.y
        return self


    def __mul__(self, scalar):
        """Point(x1*x2, y1*y2)"""
        return Point(self.x * scalar, self.y * scalar)

    def __div__(self, scalar):
        """Point(x1/x2, y1/y2)"""
        return Point(self.x / scalar, self.y / scalar)

    def __str__(self):
        return "(%.2f, %.2f)" % (self.x, self.y)

    def __repr__(self):
        return "%s(%r, %r)" % (self.__class__.__name__, self.x, self.y)

    def length(self) -> float:
        """norm of vector (0,0) to this point"""
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def distance_to(self, another_point) -> float:
        """Calculate the distance between two points."""
        return (self - another_point).length()

    def as_tuple(self):
        """(x, y)"""
        return (self.x, self.y)

    def clone(self):
        """Return a full copy of this point."""
        return Point(self.x, self.y)

    def integerize(self):
        """Convert co-ordinate values to integers."""
        self.x = int(round(self.x))
        self.y = int(round(self.y))
        return self

    def floatize(self):
        """Convert co-ordinate values to floats."""
        self.x = float(self.x)
        self.y = float(self.y)

    def move_to(self, x, y):
        """Reset x & y coordinates."""
        self.x = x
        self.y = y

    def translate_following(self, a_vector):
        """
        Move to new (x+dx,y+dy).
        :param a_vector: Vector 2D I have to follow.
        :return: Unit.
        """
        self.x = self.x + a_vector.x
        self.y = self.y + a_vector.y
        return self

    def slide_xy(self, dx, dy):
        '''Move to new (x+dx,y+dy).

        Can anyone think up a better name for this function?
        slide? shift? delta? move_by?
        '''
        self.x = self.x + dx
        self.y = self.y + dy

    def rotate(self, rad):
        """Rotate counter-clockwise by rad radians.

        Positive y goes *up,* as in traditional mathematics.

        Interestingly, you can use this in y-down computer graphics, if
        you just remember that it turns clockwise, rather than
        counter-clockwise.

        The new position is returned as a new Point.
        """
        a_sinus, a_cosinus = [f(rad) for f in (math.sin, math.cos)]
        x, y = (a_cosinus * self.x - a_sinus * self.y, a_sinus * self.x + a_cosinus * self.y)
        return Point(x, y)

    def rotate_about(self, a_point, theta):
        """Rotate counter-clockwise around a point, by theta degrees.

        Positive y goes *up,* as in traditional mathematics.

        The new position is returned as a new Point.
        """
        result = self.clone()
        result.slide_xy(-a_point.x, -a_point.y)
        result.rotate(theta)
        result.slide_xy(a_point.x, a_point.y)
        return result

POINT_ZEROZERO = Point(x=0.0, y=0.0)

def average_between(pt1: Point, pt2: Point) -> Point:
    """Returns the point in the 'middle' of the two."""
    return Point((pt1.x + pt2.x)/2, (pt1.y + pt2.y)/2)
