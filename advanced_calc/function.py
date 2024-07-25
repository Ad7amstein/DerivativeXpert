"""A utility class to handle functions"""

from sympy import sympify, simplify, solve, denom, oo, limit
from sympy.core.sympify import SympifyError


class Function:
    """A class to handle functions"""

    def __init__(self, expression):
        """Initialize the function with an expression

        Args:
            expression (str): The expression of the function
            fvars (list): The arguments of the function
        """
        from advanced_calc.derivative import Derivative

        self.expression = expression
        self.fvars = self.__expression.free_symbols
        self.diff = Derivative()

    @property
    def expression(self):
        """Get the expression of the function.

        Returns:
            str: The expression of the function
        """
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
        """Get the arguments of the function.

        Returns:
            list: The arguments of the function
        """
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
            return round(float(simplify(self.__expression).evalf()), 3)

        return round(
            float(simplify(self.__expression).subs({self.__fvars[0]: value}).evalf()), 3
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
            bool: True if the arguments are valid, False otherwise
        """
        return len(fvars) <= 1

    def diffrentiate(self, order=1, steps=False):
        """Differentiate the function.

        Args:
            order (int, optional): Order of differentiation. Defaults to 1.
            steps (bool, optional): Print the steps. Defaults to False.

        Returns:
            Function: The derivative of the function.
        """
        return Function(
            str(self.diff.diffrentiate(function=self, order=order, steps=steps))
        )

    def slope(self, value):
        """Calculate the slope of the function at a given value.

        Args:
            value (float): The value at which to calculate the slope.

        Returns:
            float: The slope of the function at the given value.
        """
        return self.diffrentiate().evaluate(value)

    def critical_points(self, interval=None):
        """Calculate the critical points of the function.

        Args:
            interval (list, optional): The interval to calculate the critical points.
            Defaults to None.

        Returns:
            list: The critical points of the function.
        """
        if len(self.fvars) < 1:
            return None
        critical_points = []
        diff1 = self.diffrentiate()
        if diff1.expression.is_rational_function():
            denominator = denom(diff1.expression)
            critical_points = solve(denominator, self.fvars[0])
        critical_points += solve(diff1.expression, self.fvars[0])
        if not critical_points:
            return None
        return critical_points

    def extrema(self, interval=None):
        """Calculate the extrema of the function.

        Args:
            interval (list, optional): The interval to calculate the extrema.
            Defaults to None.

        Returns:
            tuple: The minimum and maximum values of the function.
        """
        critical_points = self.critical_points()
        start = interval[0]
        end = interval[1]
        values = [self.evaluate(start), self.evaluate(end)]
        if critical_points:
            for i in critical_points:
                if end >= i >= start:
                    values.append(self.evaluate(i))
        mn, mx = min(values), max(values)
        return mn, mx

    def intervals_of_increase_decreasing(self):
        """Calculate the intervals of increase of the function.

        Returns:
            dict: The intervals of increase and decrease of the function.
        """
        critical_points = self.critical_points()
        if critical_points is None:
            if len(self.fvars) < 1:
                return {"Constant": [[-oo, oo]]}
            critical_points = [oo]
        else:
            critical_points.append(oo)
        signs = {}
        prv = -oo
        for cr_point in critical_points:
            signs[
                (
                    "Increasing"
                    if self.diffrentiate().evaluate((prv + cr_point) / 2) > 0
                    else "Decreasing"
                )
            ] = [[prv, cr_point]]
            prv = cr_point

        return signs

    def inflection_points(self, interval=None):
        """Calculate the inflection points of the function.

        Args:
            interval (list, optional): The interval to calculate the inflection points.
            Defaults to None.

        Returns:
            list: The inflection points of the function.
        """
        return self.diffrentiate().critical_points()

    def concavity(self, interval=None):
        """Calculate the concavity of the function.

        Args:
            interval (list, optional): The interval to calculate the concavity.
            Defaults to None.

        Returns:
            dict: The concavity of the function.
        """
        if len(self.fvars) == 0:
            return "Constant"
        diff2 = self.diffrentiate(order=2)
        intervals = self.diffrentiate().intervals_of_increase_decreasing()
        print(intervals)
        concavity = {}
        for key, value in intervals.items():
            if key == "Increasing":
                concavity["Concave Up"] = value
            elif key == "Decreasing":
                concavity["Concave Down"] = value
            else:
                if diff2.expression > 0:
                    concavity["Concave Up"] = value
                elif diff2.expression < 0:
                    concavity["Concave Down"] = value
                else:
                    return "Linear Function (No Concavity)"
        return concavity

    def asymptotes(self):
        """Calculate the asymptotes of the function."""
        asymptotes = {}
        critical_pts = self.critical_points()
        if critical_pts:
            for cr_point in critical_pts:
                asymptotes["vertical_asymptotes"] = (
                    f"{self.fvars[0]} -> {cr_point}",
                    f"f({self.fvars[0]}) -> {limit(self.expression, self.fvars[0], cr_point)}",
                )

        asymptotes["horizontal_asymptote"] = [(
                    f"{self.fvars[0]} -> {oo}",
                    f"f({self.fvars[0]}) -> {limit(self.expression, self.fvars[0], oo)}",
                )]
        asymptotes["horizontal_asymptote"].append((
                    f"{self.fvars[0]} -> {-oo}",
                    f"f({self.fvars[0]}) -> {limit(self.expression, self.fvars[0], -oo)}",
                ))
        return asymptotes


if __name__ == "__main__":
    f = Function("log(x)")
    print(f.asymptotes())
    # f1 = Function("3")
    # #0
    # print(f1.inflection_points())
    # print(f1.concavity())
    # print("------------------------------------------")
    # f1 = Function("x")
    # #0
    # print(f1.inflection_points())
    # print(f1.concavity())
    # print("------------------------------------------")
    # f1 = Function("x^2")
    # #2
    # print(f1.inflection_points())
    # print(f1.concavity())
    # print("------------------------------------------")
    # f1 = Function("x^3")
    # #6x
    # print(f1.inflection_points())
    # print(f1.concavity())
    # print("------------------------------------------")
    # f1 = Function("sqrt(x)")
    # #2
    # print(f1.inflection_points())
    # print(f1.concavity())
    # print("------------------------------------------")
    # f1 = Function("log(x)")
    # #2
    # print(f1.inflection_points())
    # print(f1.concavity())
    # print(f1.extrema(critical_points=f1.critical_points(), interval=[100, -100]))
    # print(f1.extrema(critical_points=f1.critical_points(), interval=[1,2]))
    # print(f1.intervals_of_increase_decreasing(critical_points=f1.critical_points()))
    # print(-999999999+oo)
