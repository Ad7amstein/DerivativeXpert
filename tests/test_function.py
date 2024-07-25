"""Test functions for the DerivativeXpert package."""

import unittest
from advanced_calc.function import Function
from sympy.abc import x, y
from sympy import log, sqrt, E, pi, sin, cos, tan, sinh, asec, sympify, simplify, exp
from pycodestyle import Checker
import sympy as sp


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
            # self.assertEqual(file_errors, 0)

    def test_expression(self):
        """Test the expression property."""
        function = Function("x**2")
        self.assertEqual(function.expression, x**2)
        function = Function("ln(E)*log(x)+sqrt(5)/x-1^2")
        self.assertEqual(function.expression, log(E) * log(x) + sqrt(5) / x - 1**2)
        function = Function("sin(x)+cos(x)+tan(pi/4)+asec(1)-sinh(x)")
        self.assertEqual(
            function.expression,
            sympify(sin(x) + cos(x) + tan(pi / 4) + asec(1) - sinh(x)),
        )
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

    def test_slope(self):
        """Test the slope method."""

        function = Function("2")
        self.assertEqual(function.slope(8), 0)

        function = Function("x**2")
        self.assertEqual(function.slope(2), 4)
        self.assertEqual(function.slope(-1), -2)

        function = Function("x**3")
        self.assertEqual(function.slope(2), 12)
        self.assertEqual(function.slope(0), 0)

        function = Function("3*x + 2")
        self.assertEqual(function.slope(5), 3)

        function = Function("sin(x)")
        self.assertAlmostEqual(function.slope(0), 1, places=5)
        self.assertAlmostEqual(function.slope(pi / 2), 0, places=5)

        function = Function("exp(x)")
        self.assertAlmostEqual(function.slope(0), 1, places=5)
        self.assertAlmostEqual(function.slope(1), 2.718, places=5)

        function = Function("log(x)")
        self.assertAlmostEqual(function.slope(1), 1, places=5)
        self.assertAlmostEqual(function.slope(2), 1 / 2, places=5)

    def test_critical_points(self):
        """Test the critical_points method."""

        function = Function("2")
        self.assertEqual(function.critical_points(), None)

        function = Function("x")
        self.assertEqual(function.critical_points(), None)

        function = Function("x**2")
        self.assertEqual(function.critical_points(), [0])

        function = Function("x**2 + 2*x + 1")
        self.assertEqual(function.critical_points(), [-1])

        function = Function("x**3 - 3*x**2 + 2*x")
        self.assertEqual(
            function.critical_points(), [1 - sp.sqrt(3) / 3, 1 + sp.sqrt(3) / 3]
        )

        function = Function("sin(x)")
        self.assertEqual(
            function.critical_points(interval=[0, 2 * sp.pi]),
            [sp.pi / 2, 3 * sp.pi / 2],
        )

        function = Function("exp(x)")
        self.assertEqual(function.critical_points(), None)

        function = Function("log(x)")
        self.assertEqual(function.critical_points(), None)

    def test_extrema(self):
        """Test the extrema method."""

        function = Function("2")
        self.assertEqual(function.extrema(interval=[0, 3]), (2.0, 2.0))

        function = Function("x")
        self.assertEqual(function.extrema(interval=[0, 3]), (0.0, 3.0))

        function = Function("x**2")
        self.assertEqual(function.extrema(interval=[-1, 2]), (0.0, 4.0))

        function = Function("x**2 - 4*x + 4")
        self.assertEqual(function.extrema(interval=[0, 4]), (0.0, 4.0))

        function = Function("sin(x)")
        self.assertEqual(function.extrema(interval=[0, 2 * sp.pi]), (-1.0, 1.0))

        function = Function("exp(x)")
        self.assertEqual(function.extrema(interval=[0, 1]), (1.0, 2.718))

        function = Function("log(x)")
        self.assertEqual(function.extrema(interval=[1, sp.exp(1)]), (0.0, 1.0))

    # def test_intervals_of_increase_decreasing(self):
    #     """Test the extrema method."""

    #     function = Function("2")
    #     self.assertEqual(function.intervals_of_increase_decreasing(), {})

    #     function = Function("x")
    #     self.assertEqual(function.intervals_of_increase_decreasing(), {})

    #     function = Function("x**2")
    #     self.assertEqual(function.intervals_of_increase_decreasing(), {})

def test_inflection_points(self):
    """Test the inflection_points method."""

    function = Function("2")
    self.assertEqual(function.inflection_points(), [])

    function = Function("x")
    self.assertEqual(function.inflection_points(), [])

    function = Function("x**2")
    self.assertEqual(function.inflection_points(), [])

    function = Function("x**3 - 3*x**2 + 2*x")
    self.assertEqual(function.inflection_points(), [1])

    function = Function("x**4 - 4*x**3 + 6*x**2")
    self.assertEqual(function.inflection_points(), [1, 2])

    function = Function("sin(x)")
    self.assertEqual(
        sorted(function.inflection_points(interval=[0, 2*sp.pi])), 
        [sp.pi/2, 3*sp.pi/2]
    )

    function = Function("exp(x)")
    self.assertEqual(function.inflection_points(), [])

    function = Function("log(x)")
    self.assertEqual(function.inflection_points(), [])
  
    # def test_concavity(self):
    #     """Test the inflection_points method."""

    #     function = Function("2")
    #     self.assertEqual(function.concavity(), "Constant")

    #     function = Function("x")
    #     self.assertEqual(function.concavity(), {})

    #     function = Function("x**2")
    #     self.assertEqual(function.concavity(), {})
if __name__ == "__main__":
    unittest.main()
