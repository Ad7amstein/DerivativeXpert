

import sympy as sp
# from sympy import Derivative
from advanced_calc.function import Function


class Derivative:

    def __init__(self, function= None):
        self.function = function
        self.diff = None

    def diffrentiate(self, function= None):
        if function == None:
            function= self.function
        self.diff= sp.Derivative(function.expression, function.fvars[0], evaluate=True)
        return self.diff
    
    def evaluate(self, value):
        return Function(str(self.diffrentiate())).evaluate(value)
    
    


f = Function("x**3")
d = Derivative(f)
print(d.diffrentiate())
print(d.evaluate(3))



    

    