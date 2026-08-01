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
    # Partner 1 will add test_multiply here.
    # Partner 1 will add test_divide here.
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
    # Partner 1 will add test_log_invalid_argument here.
    # Partner 1 will add test_hypotenuse here.
    # Partner 1 will add test_sqrt here.
    ##########################


if __name__ == "__main__":
    unittest.main()