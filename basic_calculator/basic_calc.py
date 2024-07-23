"""
basic_calc.py

This module defines a basic calculator class
for evaluating mathematical expressions using the sympy library.
The calculator validates the given expression before attempting to evaluate it.

Classes:
    BasicCalc: A class to validate and evaluate mathematical expressions.
"""

import sympy as sp


class BasicCalculator:
    """
    A basic calculator class for evaluating mathematical expressions.
    """

    def __init__(self, expr):
        """
        Initializes the calculator with a given expression.

        :param expr: A string representing the mathematical expression.
        """
        self.expression = expr
        self.result = None

    @property
    def expression(self):
        """get the expression"""
        return self.__expression

    @expression.setter
    def expression(self, expression):
        """set the expression"""
        if not self.is_valid_expression(expression):
            raise ValueError("Invalid expression")
        self.__expression = sp.simplify(expression)

    @staticmethod
    def is_valid_expression(expression):
        """
        Validates the given mathematical expression.

        :param expr: A string representing the mathematical expression.
        :return: True if the expression is valid, False otherwise.
        """
        try:
            sp.sympify(expression)
        except (sp.SympifyError, TypeError):
            return False
        free_sym = list(sp.sympify(expression).free_symbols)
        return len(free_sym) == 0

    def evaluate_expression(self):
        """
        Calculates the result of the mathematical expression if it is valid.
        :return:
           evaluated result of the expression formatted to three decimal,
           or a string "invalid expression".
        """
        return round(float(self.__expression.evalf()), 3)

# pycodestyle path
# black
expr = "sin(pi)+cos(pi)+tan(pi/4)+asec(1)-sinh(pi)"
calculator = BasicCalculator(expr)
result = calculator.evaluate_expression()
print(f"Result: {result}")
