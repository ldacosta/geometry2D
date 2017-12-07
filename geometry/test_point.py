# -*- coding: utf-8 -*-
"""Unit Tests for Point Definition.

This module tests all there is a for a point.

Attributes:
    None

TODO:

"""

import unittest

import math
from random import randint, random
from geometry.point import Point

class TestPoint(unittest.TestCase):
    """Tests Point definition."""

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
        pt_1 = Point(randint(0, 10), randint(0, 10))
        pt_2 = pt_1
        self.assertEqual(pt_1, pt_2)
        pt_3 = Point(x=pt_1.x, y=pt_1.y)
        self.assertEqual(pt_1, pt_3)

    def test_unpacking_works(self):
        """Can I unpack it?"""
        pt_1 = Point(randint(0, 10), randint(0, 10))
        (x,y) = pt_1
        self.assertEqual(x, pt_1.x)
        self.assertEqual(y, pt_1.y)

    def test_integerize(self):
        """Behaviour of 'convert 2 integer'"""
        a_pt = Point(random(), random())
        a_pt1 = a_pt.clone().integerize()
        self.assertTrue(a_pt1.x == math.ceil(a_pt.x) if a_pt.x > 0.5 else a_pt1.x == math.floor(a_pt.x), "[x failed] a_pt = %s, a_pt1 = %s" % (a_pt, a_pt1))
        self.assertTrue(a_pt1.y == math.ceil(a_pt.y) if a_pt.y > 0.5 else a_pt1.y == math.floor(a_pt.y), "[y failed] a_pt = %s, a_pt1 = %s" % (a_pt, a_pt1))


