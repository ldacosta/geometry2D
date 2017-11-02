import pickle
import unittest

# import random
from random import randint, random
from geometry.angle import AngleInRadians
from geometry.point import Point
from geometry.vector import Vec2d, NULL_VECTOR, angle_between, X_UNIT_VECTOR, Y_UNIT_VECTOR


####################################################################
class UnitTestVec2D(unittest.TestCase):
    def setUp(self):
        pass

    def testCreationAndAccess(self):
        v = Vec2d(111, 222)
        self.assert_(v.x == 111 and v.y == 222)
        v.x = 333
        v[1] = 444
        self.assert_(v[0] == 333 and v[1] == 444)

    def testMath(self):
        v = Vec2d(111, 222)
        self.assertEqual(v + 1, Vec2d(112, 223))
        self.assert_(v - 2 == [109, 220])
        self.assert_(v * 3 == (333, 666))
        self.assert_(v / 2.0 == Vec2d(55.5, 111))
        self.assert_(v / 2 == (55.5, 111))
        self.assert_(v ** Vec2d(2, 3) == [12321, 10941048])
        self.assert_(v + [-11, 78] == Vec2d(100, 300))
        self.assert_(v / [10, 2] == [11.1, 111])

    def testReverseMath(self):
        v = Vec2d(111, 222)
        self.assert_(1 + v == Vec2d(112, 223))
        self.assert_(2 - v == [-109, -220])
        self.assert_(3 * v == (333, 666))
        self.assert_([222, 888] / v == [2, 4])
        self.assert_([111, 222] ** Vec2d(2, 3) == [12321, 10941048])
        self.assert_([-11, 78] + v == Vec2d(100, 300))

    def testUnary(self):
        v = Vec2d(111, 222)
        v = -v
        self.assert_(v == [-111, -222])
        v = abs(v)
        self.assert_(v == [111, 222])

    def testLength(self):
        v = Vec2d(3, 4)
        self.assert_(v.length == 5)
        self.assert_(v.get_length_sqrd() == 25)
        self.assert_(v.normalize_return_length() == 5)
        self.assert_(v.length == 1)
        v.length = 5
        self.assert_(v == Vec2d(3, 4))
        v2 = Vec2d(10, -2)
        self.assert_(v.get_distance(v2) == (v - v2).get_length())

    def testAngles(self):
        v = Vec2d(0, 3)
        self.assertEquals(v.angle, 90)
        v2 = Vec2d(v)
        v.rotate(-90)
        self.assertAlmostEqual(v.get_angle_between(v2), 90)
        v2.angle -= 90
        self.assertEqual(v.length, v2.length)
        self.assertEquals(v2.angle, 0)
        self.assertEqual(v2, [3, 0])
        self.assert_((v - v2).length <= .00001)
        self.assertEqual(v.length, v2.length)
        v2.rotate(300)
        self.assertAlmostEquals(v.get_angle_between(v2), -60)
        v2.rotate(v2.get_angle_between(v))
        angle = v.get_angle_between(v2)
        self.assertAlmostEquals(angle, 0)

    def testHighLevel(self):
        basis0 = Vec2d(5.0, 0)
        basis1 = Vec2d(0, .5)
        v = Vec2d(10, 1)
        self.assert_(v.convert_to_basis(basis0, basis1) == [2, 2])
        self.assert_(v.projection(basis0) == (10, 0))
        self.assert_(basis0.dot(basis1) == 0)

    def testCross(self):
        lhs = Vec2d(1, .5)
        rhs = Vec2d(4, 6)
        self.assert_(lhs.cross(rhs) == 4)

    def testComparison(self):
        int_vec = Vec2d(3, -2)
        flt_vec = Vec2d(3.0, -2.0)
        zero_vec = Vec2d(0, 0)
        self.assert_(int_vec == flt_vec)
        self.assert_(int_vec != zero_vec)
        self.assert_((flt_vec == zero_vec) == False)
        self.assert_((flt_vec != int_vec) == False)
        self.assert_(int_vec == (3, -2))
        self.assert_(int_vec != [0, 0])
        self.assert_(int_vec != 5)
        self.assert_(int_vec != [3, -2, -5])

    def testInplace(self):
        inplace_vec = Vec2d(5, 13)
        inplace_ref = inplace_vec
        inplace_src = Vec2d(inplace_vec)
        inplace_vec *= .5
        inplace_vec += .5
        inplace_vec /= (3, 6)
        inplace_vec += Vec2d(-1, -1)
        self.assertEquals(inplace_vec, inplace_ref)

    def testPickle(self):
        testvec = Vec2d(5, .3)
        testvec_str = pickle.dumps(testvec)
        loaded_vec = pickle.loads(testvec_str)
        self.assertEquals(testvec, loaded_vec)

    def testNull(self):
        """Properties for null vector"""
        self.assertTrue(NULL_VECTOR.is_null())
        self.assertTrue(Vec2d(0, 0).is_null())
        self.assertTrue(Vec2d.origin_to(Point(0,0)).is_null())
        a_pt = Point(1,2)
        self.assertTrue(Vec2d.from_to(a_pt, a_pt).is_null())

    def testFromVector(self):
        """Creating Vector from angle"""
        import math
        an_angle = AngleInRadians(value = AngleInRadians.PI_HALF)
        v1 = Vec2d.from_angle(an_angle)
        self.assertAlmostEquals(v1.x, 0)
        self.assertAlmostEquals(v1.y, 1)

    def testAngle(self):
        """Do angles make sense?"""
        self.assertAlmostEquals(angle_between(v1 = Vec2d(1,1), v2 = Vec2d(10,10)).value, 0)
        self.assertAlmostEquals(angle_between(v1 = Vec2d(1,1), v2 = Vec2d(-1,-1)).value, AngleInRadians.PI)
        self.assertAlmostEquals(angle_between(v1 = Vec2d(1,1), v2 = Vec2d(-1,1)).value, AngleInRadians.PI_HALF)

    def test_angle_with_positive_x(self):
        self.assertEqual(Vec2d(0,0).angle_with_positive_x_axis(), AngleInRadians(0))
        for _ in range(10): # repetition of test
            an_int = randint(-100, 100)
            if an_int > 0:
                self.assertEqual(
                    Vec2d(0,an_int).angle_with_positive_x_axis().value, AngleInRadians.PI_HALF,
                    "Testing with Vec2d(0,%d)" % (an_int))
            elif an_int < 0: # case with (0,0) is tested above.
                self.assertEqual(
                    Vec2d(0,an_int).angle_with_positive_x_axis().value, AngleInRadians.THREE_HALFS_OF_PI,
                    "Testing with Vec2d(0,%d)" % (an_int))
        self.assertAlmostEquals(angle_between(v1 = X_UNIT_VECTOR, v2 = Y_UNIT_VECTOR).value, AngleInRadians.PI_HALF)
        self.assertAlmostEquals(angle_between(v1 = Y_UNIT_VECTOR, v2 = Vec2d(.5,.5)).value, AngleInRadians.PI_HALF / 2, places=5)
        # angles between vectors differing in size must coincide
        for _ in range(100):
            a_vector = Vec2d(random()/random(), random()/random())
            another_vector = Vec2d(random()/random(), random()/random())
            scale = random()/random()
            orig_angle = angle_between(a_vector, another_vector)
            scaled_angle = angle_between(a_vector * scale, another_vector * scale)
            self.assertAlmostEquals(orig_angle.value, scaled_angle.value, places=5)
            # angles when x and y have different sign:
            x = random()
            if random() > 0.5:
                x *= -1
            y = random()
            if random() > 0.5:
                y *= -1

            # if y < 0 => the smallest angle is for the equivalent of y > 0, so:
            a_vector = Vec2d(x, y)
            angle = a_vector.angle_with_positive_x_axis().value
            self.assertTrue(angle >= 0, "(%.2f, %.2f), angle = %.2f" % (x,y,angle))
            self.assertTrue(angle <= 2 * AngleInRadians.PI, "(%.2f, %.2f), angle = %.2f" % (x,y,angle))
            if x >= 0:
                if y >= 0:
                    # self.assertTrue(angle >= 0, "(%.2f, %.2f), angle = %.2f" % (x,y,angle))
                    self.assertTrue(angle <= AngleInRadians.PI_HALF, "(%.2f, %.2f), angle = %.2f" % (x,y,angle))
                else:
                    # self.assertTrue(angle <= 0, "(%.2f, %.2f), angle = %.2f" % (x,y,angle))
                    self.assertTrue(angle >= AngleInRadians.THREE_HALFS_OF_PI, "(%.2f, %.2f), angle = %.2f" % (x,y,angle))
            else:
                if y >= 0:
                    # self.assertTrue(angle <= 0, "(%.2f, %.2f), angle = %.2f" % (x,y,angle))
                    self.assertTrue(angle >= AngleInRadians.PI_HALF and angle <= AngleInRadians.PI, "(%.2f, %.2f), angle = %.2f" % (x,y,angle))
                else:
                    # self.assertTrue(angle >= 0, "(%.2f, %.2f), angle = %.2f" % (x,y,angle))
                    self.assertTrue(angle >= AngleInRadians.PI and angle <= AngleInRadians.THREE_HALFS_OF_PI, "(%.2f, %.2f), angle = %.2f" % (x,y,angle))


    def test_scaling(self):
        for _ in range(10):
            a_vector = Vec2d(random()/random(), random()/random())
            scale_to = randint(1, 30)
            new_vector = a_vector.scaled_to_norm(new_norm = scale_to)
            self.assertAlmostEqual(new_vector.norm(), scale_to)
