"""Test functions for the DerivativeXpert package."""

import unittest
from advanced_calc.function import Function
from sympy.abc import x, y
from sympy import log, sqrt, E, pi, sin, cos, tan, sinh, asec, sympify
from pycodestyle import Checker


class TestFunction(unittest.TestCase):
    """Test cases for the Function class."""

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
        function = Function("x**2")
        self.assertEqual(function.expression, x**2)
        function = Function("ln(E)*log(x)+sqrt(5)/x-1^2")
        self.assertEqual(function.expression, log(E)*log(x)+sqrt(5)/x-1**2)
        function = Function("sin(x)+cos(x)+tan(pi/4)+asec(1)-sinh(x)")
        self.assertEqual(function.expression, sympify(sin(x)+cos(x)+tan(pi/4)+asec(1)-sinh(x)))
        function = Function("5")
        self.assertEqual(function.expression, sympify(5))

        with self.assertRaises(ValueError):
            function = Function("ln(x))")
            function = Function("x++8")
            function = Function("x+2*-3")

    def test_fvars(self):
        """Test the fvars property."""
        function = Function("2")
        self.assertEqual(function.fvars, [])
        function = Function("x**2")
        self.assertEqual(function.fvars, [x])
        function = Function("y+5*y")
        self.assertEqual(function.fvars, [y])
        function = Function("sin(x)+cos(x)+tan(pi/4)+asec(1)-sinh(x)")
        self.assertEqual(function.fvars, [x])

        with self.assertRaises(ValueError):
            function = Function("x**y")
            function = Function("3llam+fawzy-farg")
            function = Function("ln(x)+5*ln(y)")

    def test_evaluation(self):
        """Test the evaluate method."""
        function = Function("2")
        self.assertEqual(function.evaluate(2), 2.000)
        self.assertEqual(function.evaluate(1408), 2.000)
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
