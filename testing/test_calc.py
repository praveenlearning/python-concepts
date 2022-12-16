import math
import unittest

import calc


class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10, 15), 25)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(math.inf, math.inf), math.inf)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 15), -5)
        self.assertEqual(calc.subtract(20, 14), 6)
        self.assertEqual(calc.subtract(math.inf, 100), math.inf)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 15), 150)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(math.inf, math.inf), math.inf)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(38.5, 7), 5.5)
        self.assertRaises(ValueError, calc.divide, 10, 0)
