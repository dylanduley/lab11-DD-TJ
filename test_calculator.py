# https://github.com/dylanduley/lab11-DD-TJ
# Partner 1: Dylan Duley
# Partner 2: Ty Jackson

import unittest
from calculator import *


class TestCalculator(unittest.TestCase):
    ######## Partner 2
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-4, 1), -3)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(7, 2), 5)
        self.assertEqual(subtract(-2, 3), -5)
        self.assertEqual(subtract(5, 5), 0)
    ##########################

    ######## Partner 1
    def test_multiply(self):
        self.assertEqual(multiply(6, 6), 36)
        self.assertEqual(multiply(4, 4), 16)
        self.assertEqual(multiply(9, 3), 27)

    def test_divide(self):
        self.assertEqual(div(5, 20), 4)
        self.assertEqual(div(-2, 8), -4)

        with self.assertRaises(ZeroDivisionError):
            div(0, 12)
    ##########################

    ######## Partner 2
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(2, 8), 3)
        self.assertAlmostEqual(logarithm(10, 100), 2)
        self.assertAlmostEqual(logarithm(3, 27), 3)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(1, 10)
    ##########################

    ######## Partner 1
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(10, 4), 10.77, places=2)
        self.assertAlmostEqual(hypotenuse(12, 5), 13.0)
        self.assertAlmostEqual(hypotenuse(8, 6), 10.0)

    def test_sqrt(self):
        self.assertAlmostEqual(square_root(16), 4.0)
        self.assertAlmostEqual(square_root(3), 1.73205080757)

        with self.assertRaises(ValueError):
            square_root(-5)
    ##########################


# Do not touch this
if __name__ == "__main__":
    unittest.main()