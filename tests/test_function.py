"""Test functions for the DerivativeXpert package."""

import unittest
from advanced_calc.function import Function
from sympy.abc import x


class TestFunction(unittest.TestCase):
    """Test cases for the Function class."""

    def test_expression(self):
        """Test the expression property."""
        function = Function("x**2")
        self.assertEqual(function.expression, x**2)

    def test_evaluation(self):
        """Test the evaluate method."""
        function = Function("x**2")
        self.assertEqual(function.evaluate(2), 4.000)
        function = Function("x**3")
        self.assertEqual(function.evaluate(2), 8.000)


if __name__ == '__main__':
    unittest.main()