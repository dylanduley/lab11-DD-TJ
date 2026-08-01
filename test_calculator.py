import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

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

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(10, 4), 10.77)
        self.assertAlmostEqual(hypotenuse(12, 5), 13.0)
        self.assertEqual(hypotenuse(8, 6), 10)

    def test_sqrt(self):
        self.assertAlmostEqual(square_root(16), 4.0)
        self.assertAlmostEqual(square_root(3), 1.73205080757)
        with self.assertRaises(ValueError):
           square_root(-5)

# Do not touch this
if __name__ == "__main__":
    unittest.main()