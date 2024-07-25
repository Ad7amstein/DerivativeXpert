"""A utility class to handle functions"""

from sympy import sympify, simplify
from sympy.core.sympify import SympifyError


class Function:
    """A class to handle functions"""

    def __init__(self, expression):
        """Initialize the function with an expression

        Args:
            expression (str): The expression of the function
            fvars (list): The arguments of the function
        """
        self.expression = expression
        self.fvars = self.__expression.free_symbols

    @property
    def expression(self):
        """Get the expression of the function"""
        return self.__expression

    @expression.setter
    def expression(self, expression):
        """Set the expression of the function

        Args:
            expression (str): The expression of the function

        Raises:
            ValueError: If the expression is invalid
        """
        if not self.is_valid_expression(expression):
            raise ValueError("Invalid expression")
        self.__expression = sympify(expression)

    @property
    def fvars(self):
        """Get the arguments of the function"""
        return self.__fvars

    @fvars.setter
    def fvars(self, fvars):
        """Set the arguments of the function

        Args:
            fvars (list): The arguments of the function

        Raises:
            ValueError: If the arguments are invalid
        """
        if not self.is_valid_vars(fvars):
            raise ValueError("Invalid number of arguments")
        self.__fvars = list(fvars)

    def evaluate(self, value):
        """Evaluate the function at a given value

        Args:
            value (float): The value to evaluate the function at

        Returns:
            float: The value of the function at the given value

        Raises:
            ValueError: If the value is invalid
        """
        try:
            value = float(simplify(value).evalf())
        except ValueError as exc:
            raise ValueError("Invalid value") from exc

        if len(self.fvars) == 0:
            return round(
                float(simplify(self.__expression).evalf()),
                3
            )

        return round(
            float(simplify(self.__expression).subs(
                {self.__fvars[0]: value}).evalf()),
            3
        )

    @staticmethod
    def is_valid_expression(expression):
        """Check if the expression is valid
        Args:
            expression (str): The expression of the function
        Returns:
            bool: True if the expression is valid, False otherwise
        """
        try:
            sympify(expression)
        except (SympifyError, TypeError):
            return False
        return True

    @staticmethod
    def is_valid_vars(fvars):
        """Check if the arguments are valid
        Args:
            args (list): The arguments of the function
        Returns:
            bool: True if the arguments are valid, False otherwise"""
        return len(fvars) <= 1

    def slope(self, value):
        """Calculate the slope of the function at a given value.
        """

    def critical_points(self, interval=None):
        """Calculate the critical points of the function.
        """

    def extrema(self, interval=None):
        """Calculate the extrema of the function.
        """

    def intervals_of_increase(self):
        """Calculate the intervals of increase of the function.
        """

    def intervals_of_decrease(self):
        """Calculate the intervals of decrease of the function.
        """

    def concavity(self, interval=None):
        """Calculate the concavity of the function.
        """

    def inflection_points(self, interval=None):
        """Calculate the inflection points of the function.
        """

    def asymptotes(self):
        """Calculate the asymptotes of the function.
        """

if __name__ == "__main__":
    f1 = Function("ln(x)")
    print(f1.evaluate("E"))
    f2 = Function("2")
    print(f2.evaluate(0))
