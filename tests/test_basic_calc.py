"""Test functions for the DerivativeXpert package."""

import unittest
from basic_calculator.basic_calc import BasicCalculator
from sympy.abc import x


class TestBasicCalculator(unittest.TestCase):
    """Test cases for the Function class."""

    def test_expression(self):
        """Test the expression property."""
        function = BasicCalculator("1+6")
        self.assertEqual(function.expression, 1+6)

    def test_evaluation(self):
        """Test the evaluate method."""
        function = BasicCalculator("1+1")
        self.assertEqual(function.evaluate_expression(), 2.000)
        function = BasicCalculator("3^2")
        self.assertEqual(function.evaluate_expression(), 9.000)


if __name__ == '__main__':
    unittest.main()