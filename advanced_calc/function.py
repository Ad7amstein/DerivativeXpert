"""A utility class to handle functions"""

from sympy import *
from sympy.abc import x, y


class Function:
    """A class to handle functions"""

    def __init__(self, expression):
        """Initialize the function with an expression

        Args:
            expression (str): The expression of the function
        """
        self.expression = expression
        self.args = self.__expression.args

    @property
    def expression(self):
        """Get the expression of the function"""
        return self.__expression

    @expression.setter
    def expression(self, expression):
        """Set the expression of the function
        
        Args:
            expression (str): The expression of the function
        """
        if not self.is_valid_expression(expression):
            raise ValueError("Invalid expression")
        self.__expression = simplify(expression)

    @property
    def args(self):
        """Get the arguments of the function"""
        return self.__args

    @args.setter
    def args(self, args):
        """Set the arguments of the function
        
        Args:
            args (list): The arguments of the function
        """
        if not self.is_valid_args(args):
            raise ValueError("Invalid arguments")
        self.__args = args

    def evaluate(self, value):
        """Evaluate the function at a given value
        
        Args:
            value (float): The value to evaluate the function at
        
        Returns:
            float: The value of the function at the given value
        """
        value = sympify(value)
        return self.__expression.subs({x: value}).evalf()

    @staticmethod
    def is_valid_expression(expression):
        """Check if the expression is valid
        Args:
            expression (str): The expression of the function
        Returns:
            bool: True if the expression is valid, False otherwise
        """
        return True

    @staticmethod
    def is_valid_args(args):
        """Check if the arguments are valid
        Args:
            args (list): The arguments of the function
        Returns:
            bool: True if the arguments are valid, False otherwise"""
        return True


f1 = Function("ln(x)")
print(f1.evaluate("E"))
