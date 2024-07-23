"""This module contains the Derivative class
to calculate the derivative of a function"""

import sympy as sp
from advanced_calc.function import Function
from plot.plot import Plotter


class Derivative:
    """Derivative class to calculate the derivative of a function"""

    def __init__(self, function=None):
        self.function = function
        self.diff = None

    def diffrentiate(self, function=None, order=1, steps=False):
        """Differentiate the function"""
        if function:
            self.function = function
        if len(self.function.fvars) > 0:
            symb = self.function.fvars[0]
        end = order
        while order > 0:
            self.diff = sp.Derivative(
                self.function.expression, symb, evaluate=True
            )
            if steps:
                print(f"Derivative of order {end-order+1}: {self.diff}")
            self.function = Function(str(self.diff))
            order -= 1
        return self.diff

    def evaluate(self, value):
        """Evaluate the derivative at a given value"""
        return self.function.evaluate(value)

    def plot(self):
        """Plot the derivative of the function"""
        Plotter.plot(function=self.function)


f = Function("x^5")
Plotter.plot(function=f)

d = Derivative(f)
print(d.diffrentiate(order=20, steps=True))
print(d.evaluate(3))
print(d.plot())