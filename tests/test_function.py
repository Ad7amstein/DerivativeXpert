"""Test functions for the DerivativeXpert package."""

import unittest
from advanced_calc.function import Function
from sympy.abc import x
from sympy import log, sqrt, E, pi, sin, cos, tan, sinh, asec, sympify
from pycodestyle import Checker


class TestFunction(unittest.TestCase):
    """Test cases for the Function class."""

    def setUp(self):
        """Set up the test cases."""
        self.function = Function("x**2")

    def test_docs(self):
        """Test the docstrings."""
        self.assertIsNotNone(Function.__doc__)
        self.assertIsNotNone(Function.__init__.__doc__)
        self.assertIsNotNone(Function.expression.__doc__)
        self.assertIsNotNone(Function.expression.__doc__)
        self.assertIsNotNone(Function.fvars.__doc__)
        self.assertIsNotNone(Function.fvars.__doc__)
        self.assertIsNotNone(Function.evaluate.__doc__)

    def test_pycodestyle(self):
        """Test the pycodestyle."""
        files = ["advanced_calc/function.py"]
        for file in files:
            checker = Checker(file)
            file_errors = checker.check_all()
            self.assertEqual(file_errors, 0)

    def test_expression(self):
        """Test the expression property."""
        self.assertEqual(self.function.expression, x**2)
        self.function.expression = "ln(E)*log(x)+sqrt(5)/x-1^2"
        self.assertEqual(self.function.expression, log(E)*log(x)+sqrt(5)/x-1**2)
        self.function.expression = "sin(x)+cos(x)+tan(pi/4)+asec(1)-sinh(x)"
        self.assertEqual(self.function.expression, sympify(sin(x)+cos(x)+tan(pi/4)+asec(1)-sinh(x)))

        with self.assertRaises(ValueError):
            self.function.expression = "ln(x))"
            self.function.expression = "x++8"
            self.function.expression = "x+2*-3"

    def test_fvars(self):
        """Test the fvars property."""
        self.function.expression = "x**2"
        self.assertEqual(self.function.fvars, [x])
        self.function.expression = "sin(x)+cos(x)+tan(pi/4)+asec(1)-sinh(x)"
        self.assertEqual(self.function.fvars, [x])

        with self.assertRaises(ValueError):
            self.function.expression = "x**y"
            self.function.expression = "3llam+fawzy-farg"
            self.function.expression = "ln(x)+5*ln(y)"

    def test_evaluation(self):
        """Test the evaluate method."""
        function = Function("x**2")
        self.assertEqual(function.evaluate(2), 4.000)
        function = Function("x**3")
        self.assertEqual(function.evaluate(2), 8.000)
        function = Function("ln(x)+5*ln(x)-sqrt(x)/E^x")
        self.assertAlmostEqual(function.evaluate(7), 11.673, places=3)
        function = Function("x^2+5*x-3")
        self.assertAlmostEqual(function.evaluate(0), -3.000, places=3)
        function = Function("sin(x)+cos(x)+tan(pi/4)+asec(1)-sinh(x)")
        self.assertAlmostEqual(function.evaluate(pi), -11.549, places=3)


if __name__ == '__main__':
    unittest.main()
