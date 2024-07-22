"""Test functions for the DerivativeXpert package."""

import unittest
from basic_calculator.basic_calc import BasicCalculator
from sympy.abc import x

# python -m unittest tests/test_basic_calc.py 

class TestBasicCalculator(unittest.TestCase):
    """Test cases for the BasicCalculator class."""

    def test_expression(self):
        """Test the expression property."""
        basic_calc = BasicCalculator("1+6")
        self.assertEqual(basic_calc.expression, 1+6)

        basic_calc = BasicCalculator("0+6")
        self.assertEqual(basic_calc.expression, 0+6)

        basic_calc = BasicCalculator("2+-6")
        self.assertEqual(basic_calc.expression, 2+-6)

        basic_calc = BasicCalculator("36")
        self.assertEqual(basic_calc.expression, 36)

    def test_evaluation(self):
        """Test the evaluate method."""
        basic_calc = BasicCalculator("1+1")
        self.assertEqual(basic_calc.evaluate_expression(), 2.000)
        basic_calc = BasicCalculator("3^2")
        self.assertEqual(basic_calc.evaluate_expression(), 9.000)

    def test_is_valid_expression(self):
        """Test the evaluate method."""
        basic_calc = BasicCalculator("1+1")
        self.assertEqual(basic_calc.is_valid_expression("1+1"), True)
        basic_calc = BasicCalculator("3^jj2")
        self.assertEqual(basic_calc.is_valid_expression("3^hh2"), True)


if __name__ == '__main__':
    unittest.main()