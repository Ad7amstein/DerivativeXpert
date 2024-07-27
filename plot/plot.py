"""A module to plot a function."""

import sympy as sp
from advanced_calc.function import Function


class Plotter:
    """A class to plot a function."""

    def __init__(self):
        """Initialize the class."""

    @staticmethod
    def plot(func):
        """Plot the function.

        Parameters
        ==========
            func : `Function`
                The function to plot.

        Raises
        ======
            ValueError:
                If the function is not provided.
                If the function is not an instance of Function.
        """
        if not func or not func.expression:
            raise ValueError("No function to plot.")
        if not isinstance(func, Function):
            raise ValueError("The function must be an instance of Function.")

        fun_str = str(func.expression)
        x = sp.Symbol("x")
        try:
            symb = func.fvars[0]
        except IndexError:
            symb = x
        sp.plot(
            func.expression,
            (symb, -100, 100),
            title=f"Plot of $f({symb}) = {fun_str}$",
            xlabel=f"${symb}$",
            ylabel=f"$f({symb})$",
            line_color="blue",
            show=True,
        )


if __name__ == "__main__":
    function = Function("x^2")
    Plotter.plot(function)
