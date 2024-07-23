"""A module to plot a function."""

from advanced_calc.function import Function
import sympy as sp
from sympy.abc import x


class Plotter:
    """A class to plot a function."""

    def __init__(self, func):
        """Initialize the class.

        Args:
            function (str): The function to plot.
        """
        self.function = func

    @staticmethod
    def plot(instance=None, func=None):
        """Plot the function."""
        if not func and not instance.function:
            raise ValueError("No function to plot.")
        if not func:
            func = instance.function

        fun_str = str(func.expression)
        sp.plot(
            func.expression,
            (x, -100, 100),
            title=f"Plot of $f(x) = {fun_str}$",
            xlabel="$x$",
            ylabel="$f(x)$",
            line_color="blue",
            show=True,
        )


if __name__ == "__main__":
    function = Function("x^2")
    plt = Plotter(function)
    Plotter.plot(plt)
    Plotter.plot(plt)
