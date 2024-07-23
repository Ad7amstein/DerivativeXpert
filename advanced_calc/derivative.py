"""This module contains the Derivative class to calculate the derivative of a function"""
import sympy as sp
from advanced_calc.function import Function
from plot.plot import Plotter


class Derivative:
    """Derivative class to calculate the derivative of a function"""
    def __init__(self, function= None):
        self.function = function
        self.diff = None


    def diffrentiate(self, function= None, order=1):
        """Differentiate the function"""
        if function:
            self.function = function
        while order>0:
            self.diff= sp.Derivative(self.function.expression,
                                     self.function.fvars[0], evaluate=True)
            print(self.diff)
            if len(self.diff.free_symbols) < 1:
                break
            self.function = Function(str(self.diff))
            order-=1
        return self.diff

    def evaluate(self, value):
        """Evaluate the derivative at a given value"""
        return self.function.evaluate(value)

    def plot(self):
        """Plot the derivative of the function"""
        Plotter.plot(function=self.function)


f = Function("5*x")
Plotter.plot(function=f)

d = Derivative(f)
print(d.diffrentiate(order=20))
print(d.evaluate(3))
print(d.plot())

# print(d.diffrentiate())
# print(d.evaluate(3))
# print(d.plot())
