"""Different shapes and its classes.


Code for Rect(angle) was taken from https://wiki.python.org/moin/PointsAndRectangles

Rect  -- two points, forming a rectangle

"""

from random import random

from geometry.coordinates import CoordinatesDirection
from geometry.point import Point, average_between


def random_between(a_float: float, another_float: float) -> float:
    """ Random number in a range.
    Args:
        a_float: one side of the range.
        another_float: the other side.

    Returns:
        a random number as a float.

    """
    the_min = min(a_float, another_float)
    the_max = max(a_float, another_float)
    return random() * (the_max - the_min) + the_min

class Rect(object):
    """A rectangle identified by two points.

    The rectangle stores left, top, right, and bottom values.

    Coordinates are based on screen coordinates.

    origin                               top
       +-----> x increases                |
       |                           left  -+-  right
       v                                  |
    y increases                         bottom

    set_points  -- reset rectangle coordinates
    contains  -- is a point inside?
    overlaps  -- does a rectangle overlap?
    top_left  -- get top-left corner
    bottom_right  -- get bottom-right corner
    expanded_by  -- grow (or shrink)
    TODO: add description of effect of 'direction'
    """

    def __init__(self, direction: CoordinatesDirection, pt1: Point, pt2: Point):
        """Initialize a rectangle from two points."""
        self.coord_direction = direction
        self.set_points(pt1, pt2)

    @classmethod
    def from_topleft_widthheight(cls, top: float, left: float, width: float, height: float):
        top_left_pt = Point.from_tuple((top,left))
        return Rect(direction=CoordinatesDirection.SCREEN_DIRECTION, pt1=top_left_pt,
                            pt2=Point(x=top_left_pt.x + width,
                                      y=top_left_pt.y + height))


    def set_points(self, pt1, pt2):
        """Reset the rectangle coordinates."""
        (x_pt1, y_pt1) = pt1.as_tuple()
        (x_pt2, y_pt2) = pt2.as_tuple()
        self.left = min(x_pt1, x_pt2)
        self.right = max(x_pt1, x_pt2)
        if self.coord_direction == CoordinatesDirection.SCREEN_DIRECTION:
            self.top = min(y_pt1, y_pt2)
            self.bottom = max(y_pt1, y_pt2)
        else:
            self.top = max(y_pt1, y_pt2)
            self.bottom = min(y_pt1, y_pt2)
        self.topleft = Point(self.left, self.top)
        self.topright = Point(self.right, self.top)
        self.bottomright = Point(self.right, self.bottom)
        self.bottomleft = Point(self.left, self.bottom)
        self.center = average_between(pt1 = self.topleft, pt2 = self.bottomright)
        self.midbottom = Point(x =(self.topleft.x + self.bottomright.x) / 2, y = self.bottom)
        self.midtop = Point(x =(self.topleft.x + self.bottomright.x) / 2, y = self.top)
        self.height = self.bottom - self.top
        self.width = self.right - self.left
        self.midleft = Point(x = self.left, y = self.top + self.height/2)
        self.midright = Point(x = self.right, y = self.top + self.height/2)

    def top_left(self) -> Point:
        """Return the top-left corner as a Point."""
        return self.topleft

    def bottom_right(self) -> Point:
        """Return the bottom-right corner as a Point."""
        return self.bottomright

    def clone(self):
        """
        Clones the contents of the other rectangle.
        Args:
            another_rect:

        Returns:

        """
        return Rect(direction=self.coord_direction, pt1=self.bottomright, pt2=self.topleft)

    def get_random_point(self) -> Point:
        """
        Gets a random point belonging to this rectangle.
        Returns:
            a Point

        """
        an_x = random_between(self.right, self.left)
        a_y = random_between(self.top, self.bottom)
        return Point(x = an_x, y = a_y)

    def contains(self, a_pt: Point)-> bool:
        """Return true if a point is inside the rectangle."""
        x, y = a_pt.as_tuple()
        ok_on_x = self.left <= x <= self.right
        ok_on_y = (
            (
                self.coord_direction == CoordinatesDirection.SCREEN_DIRECTION and
                (self.top <= y <= self.bottom)
            )
            or
            (
                self.coord_direction == CoordinatesDirection.ANTI_SCREEN_DIRECTION and
                (self.top >= y >= self.bottom)
            )
        )
        return ok_on_x and ok_on_y

    def overlaps(self, other) -> bool:
        """Return true if a rectangle overlaps this rectangle."""
        return (self.right > other.left and self.left < other.right and
                self.top < other.bottom and self.bottom > other.top)

    def expanded_by(self, n_units):
        """Return a rectangle with extended borders.

        Create a new rectangle that is wider and taller than the
        immediate one. All sides are extended by "n_units" points.
        """
        pt1 = Point(self.left - n_units, self.top - n_units)
        pt2 = Point(self.right + n_units, self.bottom + n_units)
        return Rect(self.coord_direction, pt1, pt2)

    def __attrs(self):
        """
        All attributes in a single representation.
        Returns:
            A tuple with all attributes.

        """
        return (self.coord_direction, self.left, self.right, self.top, self.bottom)

    def __eq__(self, other):
        return isinstance(other, Rect) and self.__attrs() == other.__attrs()

    def __hash__(self):
        return hash(self.__attrs())

    def __str__(self):
        return "coordinates: %s; <Rect %s-%s>" % \
               (self.coord_direction, self.topleft, self.bottomright)

    def __repr__(self):
        return "%s(%r, %r)" % (self.__class__.__name__,
                               Point(self.left, self.top),
                               Point(self.right, self.bottom))
