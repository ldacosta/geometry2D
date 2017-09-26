# -*- coding: utf-8 -*-
"""Unit Tests for Point Definition.

This module tests all there is a for a point.

Attributes:
    None

TODO:

"""

import unittest

from random import randint
from geometry.point import Point

class TestPoint(unittest.TestCase):
    """Tests Point definition."""

    def setUp(self):
        """
        Creates proper structures to test.
        Returns:

        """

    def tearDown(self):
        """
        This method is called after each test
        """
        pass

    def test_equality_works(self):
        """Equality works as expected?"""
        pt_1 = Point(randint(0, 10), randint(0, 10))
        pt_2 = pt_1
        self.assertEqual(pt_1, pt_2)
        pt_3 = Point(x=pt_1.x, y=pt_1.y)
        self.assertEqual(pt_1, pt_3)
