import sympy as sp
import matplotlib.pyplot as plt
 

class Plotter :
    

    def __init__ (self, function):
        self.function =  function


    def plotw (self) :
        x = sp.Symbol('x')
        function = x**2
        sp.plot(function, (x, -10, 10), title='Plot of $f(x) = x^2$', xlabel='$x$', ylabel='$f(x)$', line_color='blue', show=True)





s = Plotter ("x^2")
s.plotw()
