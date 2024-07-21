

# import sympy as sp
# import matplotlib.pyplot as plt
 
# def plotw () :
#     # x^2
#     x = sp.Symbol('x')
#     sp.plot("x^2", (x, -10, 10), title=f'Plot of $f(x) = "x^2"$', xlabel='$x$', ylabel='$f(x)$', line_color='blue', show=True)




# plotw()





import sympy as sp
import matplotlib.pyplot as plt

# Define the symbolic variable and function
x = sp.Symbol('x')
f = x**2

# Create the plot
sp.plot(f, (x, -10, 10), title='Plot of $f(x) = x^2$', xlabel='$x$', ylabel='$f(x)$', line_color='blue', show=True)

