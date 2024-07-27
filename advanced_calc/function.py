"""A utility class to handle functions"""

import sympy as sp
from sympy.core.sympify import SympifyError
from heapq import merge
from sympy.calculus.util import continuous_domain, function_range


class Function:
    """A class to handle functions"""

    def __init__(self, expression):
        """Initialize the function with an expression.

        Parameters
        ==========
            expression : `str`
                The expression of the function
            fvars : `list`
                The arguments of the function
        """
        from advanced_calc.derivative import Derivative

        self.expression = expression
        self.fvars = self.__expression.free_symbols
        self.diff = Derivative()
        self.range = function_range(
            self.__expression, sp.Symbol("x")
            if len(self.fvars) == 0
            else self.fvars[0], sp.S.Reals)
        self.domain = continuous_domain(
            self.__expression, sp.Symbol("x")
            if len(self.fvars) == 0
            else self.fvars[0], sp.S.Reals)

    @property
    def expression(self):
        """Get the expression of the function.

        Returns
        =======
            str: The expression of the function
        """
        return self.__expression

    @expression.setter
    def expression(self, expression):
        """Set the expression of the function.

        Parameters
        ==========
            expression : `str`
                The expression of the function

        Raises
        ======
            ValueError
                If the expression is invalid
        """
        if not self.is_valid_expression(expression):
            raise ValueError("Invalid expression")
        self.__expression = sp.sympify(expression)

    @property
    def fvars(self):
        """Get the arguments of the function.

        Returns
        =======
            list
                The arguments of the function
        """
        return self.__fvars

    @fvars.setter
    def fvars(self, fvars):
        """Set the arguments of the function

        Parameters
        ==========
            fvars : `list`
                The arguments of the function

        Raises
        ======
            ValueError
                If the arguments are invalid
        """
        if not self.is_valid_vars(fvars):
            raise ValueError("Invalid number of arguments")
        self.__fvars = list(fvars)

    @property
    def range(self):
        """Get the range of the function.

        Returns
        =======
            Interval
                The range of the function
        """
        return self.__range

    @range.setter
    def range(self, rng):
        """Set the range of the function.

        Parameters
        ==========
            rng : `Interval`
                The range of the function
        """
        self.__range = rng

    @property
    def domain(self):
        """Get the domain of the function.

        Returns
        =======
            Interval:
                The domain of the function
        """
        return self.__domain

    @domain.setter
    def domain(self, domain):
        """Set the domain of the function.

        Parameters
        ==========
            expression : Interval
                The domain of the function
        """
        self.__domain = domain

    def evaluate(self, value):
        """Evaluate the function at a given value.

        Parameters
        ==========
            value : `float`
                The value to evaluate the function at

        Returns
        =======
            float
                The value of the function at the given value

        Raises
        ======
            ValueError
                If the value is invalid
        """
        try:
            value = float(sp.simplify(value).evalf())
        except (ValueError, TypeError) as exc:
            raise ValueError("Invalid value") from exc
        if value not in self.domain:
            raise ValueError("Value is not in the domain of the function")

        if len(self.fvars) == 0:
            return round(float(sp.simplify(self.__expression).evalf()), 3)

        return round(
            float(sp.simplify(self.__expression).subs({self.__fvars[0]: value}).evalf()), 3
        )

    @staticmethod
    def is_valid_expression(expression):
        """Check if the expression is valid.

        Parameters
        ==========
            expression (str): The expression of the function

        Returns
        =======
            bool
                True if the expression is valid, False otherwise
        """
        try:
            sp.sympify(expression)
        except (SympifyError, TypeError):
            return False
        return True

    @staticmethod
    def is_valid_vars(fvars):
        """Check if the arguments are valid.

        Parameters
        ==========
            args : `list`
                The arguments of the function

        Returns
        =======
            bool
                True if the arguments are valid, False otherwise
        """
        return len(fvars) <= 1

    def diffrentiate(self, order=1, steps=False):
        """Differentiate the function.

        Parameters
        ==========
            order : `int`, `optional`
                Order of differentiation. Defaults to 1.
            steps : `bool`, `optional`
                Print the steps. Defaults to False.

        Returns
        =======
            Function
                The derivative of the function.
        """
        return Function(
            str(self.diff.diffrentiate(function=self, order=order, steps=steps))
        )

    def slope(self, value):
        """Calculate the slope of the function at a given value.

        Parameters
        ==========
            value : `float`
                The value at which to calculate the slope.

        Returns
        =======
            float
                The slope of the function at the given value.
        """
        return self.diffrentiate().evaluate(value)

    def critical_points(self, interval=None):
        """Calculate the critical points of the function.

        Parameters
        ==========
            interval : `list`, `optional`
                The interval to calculate the critical points.
                Defaults to None.

        Returns
        =======
            list
                The critical points of the function.
        """
        if len(self.fvars) < 1:
            return []
        if not interval:
            interval = self.domain
        critical_points = []
        critical_points += sp.singularities(
            self.expression,
            self.fvars[0],
            domain=interval
            )
        critical_points += sp.solveset(
            self.diffrentiate().expression,
            self.fvars[0],
            domain=interval
            )
        return critical_points

    def extrema(self, interval=None):
        """Calculate the extrema of the function.

        Parameters
        ==========
            interval : `list`, `optional`
                The interval to calculate the extrema.
                Defaults to None.

        Returns
        =======
            tuple
                The minimum and maximum values of the function.
        """
        if not interval:
            interval = self.domain
        symb = sp.Symbol("x") if len(self.fvars) == 0 else self.fvars[0]
        mx = sp.maximum(self.expression, symb, interval)
        mn = sp.minimum(self.expression, symb, interval)
        return mx, mn

    def intervals_of_increase_decreasing(self, interval=None):
        """Calculate the intervals of increase of the function.

        Returns
        =======
            dict
                The intervals of increase and decrease of the function.
        """
        symb = sp.Symbol("x") if len(self.fvars) == 0 else self.fvars[0]
        critical_points = self.critical_points(interval=interval)
        interval_points = []
        if not interval:
            interval = self.domain
        if isinstance(interval, sp.Union):
            for interval in interval.args:
                interval_points.append(interval.start)
                interval_points.append(interval.end)
        else:
            interval_points = [interval.start, interval.end]
        interval_points = sorted(list(set(merge(critical_points, interval_points))))

        signs = {"Constant":[],"Increasing" : [], "Decreasing":[]}
        for i in range(1, len(interval_points)):
            if sp.is_strictly_increasing(self.expression, interval=sp.Interval(
                interval_points[i - 1]+1, interval_points[i]-1), symbol=symb):
                signs["Increasing"] += [interval_points[i - 1], interval_points[i]]
            elif sp.is_strictly_decreasing(self.expression, interval=sp.Interval(
                interval_points[i - 1]+1, interval_points[i]-1), symbol=symb):
                signs["Decreasing"] += [interval_points[i - 1], interval_points[i]]
            else:
                signs["Constant"] += [[interval_points[i - 1], interval_points[i]]]

        return signs

    def inflection_points(self, interval=None):
        """Calculate the inflection points of the function.

        Parameters:
            interval : `list`, `optional`
                The interval to calculate the inflection points.
                Defaults to None.

        Returns
        =======
            list
                The inflection points of the function.
        """
        if not interval:
            interval = self.domain
        return self.diffrentiate().critical_points(interval=interval)

    def concavity(self, interval=None):
        """Calculate the concavity of the function.

        Parameters
        ==========
            interval : `list`, `optional`
                The interval to calculate the concavity.
                Defaults to None.

        Returns
        =======
            dict
                The concavity of the function.
        """
        if len(self.fvars) == 0:
            return "Constant function"
        if not interval:
            interval = self.domain
        intervals = self.diffrentiate().intervals_of_increase_decreasing(interval=interval)
        concavity = {"Linear": [], "Concave Up": [], "Concave Down": []}
        for key, value in intervals.items():
            if key == "Increasing":
                concavity["Concave Up"] += [value]
            elif key == "Decreasing":
                concavity["Concave Down"] += [value]
            else:
                concavity["Linear"] += [value]
        return concavity

    def asymptotes(self):
        """Calculate the asymptotes of the function."""
        asymptotes = {}
        if len(self.fvars) == 0:
            return "No asymptotes"
        undefined_points = sp.singularities(self.expression, self.fvars[0])
        if undefined_points is not sp.EmptySet:
            for point in undefined_points:
                asymptotes["vertical_asymptotes"] = (
                    f"{self.fvars[0]} -> {point}",
                    f"f({self.fvars[0]}) -> {sp.limit(self.expression, self.fvars[0], point)}",
                )
        asymptotes["horizontal_asymptote"] = [(
                    f"{self.fvars[0]} -> {sp.oo}",
                    f"f({self.fvars[0]}) -> {sp.limit(self.expression, self.fvars[0], sp.oo)}",
                )]
        asymptotes["horizontal_asymptote"].append((
                    f"{self.fvars[0]} -> {-sp.oo}",
                    f"f({self.fvars[0]}) -> {sp.limit(self.expression, self.fvars[0], -sp.oo)}",
                ))
        return asymptotes

    def plot(self):
        """Plot the function."""
        from plot.plot import Plotter
        Plotter.plot(func= self)


if __name__ == "__main__":
    f = Function("ln(x)")
    print(f.evaluate(1))
