import unittest

from geometry.angle import AngleInRadians, AngleInDegrees

class UnitTestAngle(unittest.TestCase):
    def setUp(self):
        pass

    def test_conversion(self):
        """Radians to degrees."""
        a_rads = AngleInRadians(value = AngleInRadians.PI_HALF)
        a_degrees = AngleInDegrees.from_radians(angle_in_radians=a_rads)
        self.assertAlmostEqual(a_degrees.value, 90)
        a_rads = AngleInRadians(value = AngleInRadians.THREE_HALFS_OF_PI)
        a_degrees = AngleInDegrees.from_radians(angle_in_radians=a_rads)
        self.assertAlmostEqual(a_degrees.value, 270)
