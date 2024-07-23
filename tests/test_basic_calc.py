"""Test BasicCalculator for the DerivativeXpert package."""

import unittest
from basic_calculator.basic_calc import BasicCalculator
from sympy import log, sqrt, E, pi, sin, cos, tan, sinh, asec,ln, sympify, simplify
from pycodestyle import Checker

# python -m unittest tests/test_basic_calc.py 

class TestBasicCalculator(unittest.TestCase):
    """Test cases for the BasicCalculator class."""

    def setUp(self):
        """Set up the test cases."""
        self.basic_calc = BasicCalculator("ln(E^2)+3")

    def test_docs(self):
        """Test the docstrings."""
        self.assertIsNotNone(BasicCalculator.__doc__)
        self.assertIsNotNone(BasicCalculator.__init__.__doc__)
        self.assertIsNotNone(BasicCalculator.expression.__doc__)
        self.assertIsNotNone(BasicCalculator.expression.__doc__)
        self.assertIsNotNone(BasicCalculator.is_valid_expression.__doc__)
        self.assertIsNotNone(BasicCalculator.evaluate_expression.__doc__)

    def test_pycodestyle(self):
        """Test the pycodestyle."""
        files = ["basic_calculator/basic_calc.py"]
        for file in files:
            checker = Checker(file)
            file_errors = checker.check_all()
            self.assertEqual(file_errors, 0)

    def test_expression(self):
        """Test the expression property."""
        self.assertEqual(self.basic_calc.expression, ln(E**2)+3)
        self.basic_calc.expression = "ln(E)*log(3)+sqrt(5)/2-1^2"
        self.assertEqual(self.basic_calc.expression, ln(E)*log(3)+sqrt(5)/2-1**2)
        self.basic_calc.expression = "sin(30)+cos(30)+tan(pi/4)+asec(1)-sinh(30)"
        self.assertEqual(self.basic_calc.expression,simplify (sin(30)+cos(30)+tan(pi/4)+asec(1)-sinh(30))) 

        with self.assertRaises(ValueError):
            self.basic_calc.expression = "ln(2))"
            self.basic_calc.expression = "8++8"
            self.basic_calc

    def test_evaluation(self):
        """Test the evaluate method."""
        basic_calc = BasicCalculator("1+1")
        self.assertAlmostEqual(basic_calc.evaluate_expression(), 2.000, places=3)
        basic_calc = BasicCalculator("sin(30)**2 + cos(30)^2")
        self.assertAlmostEqual(basic_calc.evaluate_expression(), 1.000, places=3)
        basic_calc = BasicCalculator("ln(E**2)")
        self.assertAlmostEqual(basic_calc.evaluate_expression(), 2.000, places=3)
        basic_calc = BasicCalculator("sin(pi)+cos(pi)+tan(pi/4)+asec(1)-sinh(pi)")
        self.assertAlmostEqual(basic_calc.evaluate_expression(), -11.549 , places=3)
        basic_calc = BasicCalculator("3^2")
        self.assertAlmostEqual(basic_calc.evaluate_expression(), 9.000, places=3)

# python -m unittest tests/test_basic_calc.py
if __name__ == '__main__':
    unittest.main()