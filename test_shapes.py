# -*- coding: utf-8 -*-
"""Unit Tests for Player.

This module tests all there is a for an abstract Player.

Attributes:
    None

TODO:
    * Actually implement them properly.

"""

import unittest

from random import randint
from hockey_core.util.geometry.point import Point
from hockey_core.util.geometry.shapes import Rect
from hockey_core.util.geometry.coordinates import CoordinatesDirection

class TestShapes(unittest.TestCase):
    """Tests all players' concerns.
    """

    def setUp(self):
        """
        Creates proper structures to test.
        Returns:

        """
        pass

    def tearDown(self):
        """
        This method is called after each test
        """
        pass

    def test_equality_works(self):
        """Equality works as expected?"""
        a_rect_screen_dir = Rect(
            direction=CoordinatesDirection.SCREEN_DIRECTION,
            pt1=Point(x=randint(0, 10), y=randint(0, 10)),
            pt2=Point(x=randint(0, 10), y=randint(0, 10)))
        self.assertEqual(a_rect_screen_dir, a_rect_screen_dir)
        # cloning conserves equality:
        another_rect = a_rect_screen_dir.clone()
        self.assertEqual(a_rect_screen_dir, another_rect)
        # a change will break the equality:
        another_rect.set_points(
            pt1=Point(x=randint(0, 10), y=randint(0, 10)),
            pt2=Point(x=randint(0, 10), y=randint(0, 10)))
        self.assertNotEqual(another_rect, a_rect_screen_dir)

    def test_rect_basic_belonging(self):
        """Basic test for point belonging to rectangle."""
        a_rect_screen_dir = Rect(
            direction=CoordinatesDirection.SCREEN_DIRECTION,
            pt1=Point(x=0.0, y=0.0),
            pt2=Point(x=5.0, y=5.0))
        a_rect_anti_screen_dir = Rect(
            direction=CoordinatesDirection.ANTI_SCREEN_DIRECTION,
            pt1=Point(x=0.0, y=0.0),
            pt2=Point(x=5.0, y=5.0))
        for a_rect in [a_rect_screen_dir, a_rect_anti_screen_dir]:
            print(a_rect)
            self.assertTrue(a_rect.contains(Point(x=3.0, y=3.0)))
            self.assertFalse(a_rect.contains(Point(x=3.0, y=30.0)))

    def test_composed_belonging(self):
        """Test random generation and belonging."""
        a_rect = Rect(
            direction=CoordinatesDirection.ANTI_SCREEN_DIRECTION,
            pt1=Point(x=0.0, y=0.0),
            pt2=Point(x=5.0, y=5.0))
        for i in range(10):
            a_pt = a_rect.get_random_point()
            self.assertTrue(a_rect.contains(a_pt))


if __name__ == '__main__':
    unittest.main()
