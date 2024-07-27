"""Main program for DerivativeXpert."""

import sys
from basic_calculator.basic_calc import BasicCalculator
from advanced_calc.function import Function
from sympy import pretty


def basic_calculator():
    """Basic calculator function."""
    while True:
        try:
            exp = input("Enter the exepression or 'm' to main menu: ")
            if exp == "m":
                return
            basic_calc = BasicCalculator(exp)
        except ValueError as e:
            print(f"oooopppps, {str(e)}")
            continue
        print(pretty(basic_calc.evaluate_expression()))


def advanced_calculator():
    """Advanced calculator function."""
    fun = ""
    while True:
        if fun == "":
            try:
                fun = input("Enter the function or 'm' to main menu: ")
                if fun == "m":
                    return
                function = Function(fun)
            except ValueError as e:
                print(f"oooopppps, {str(e)}")
                continue
        print(
            """
1- Evaluate at point
2- Find Derivative (1,2,..)
3- Plot
4- Plot Derivatives
5- Slope
6- Critical points
7- Interval of increasing and decreasing
8- Inflection points
9- Concavity
10- Asymptotes
11- Domain and Range
12- Extrema
"""
        )
        choice = input("Enter the choice or 'm' to main menu: ")
        if choice == "1":
            x = input("Enter x: ")
            try:
                print(pretty(function.evaluate(x)))
            except ValueError as e:
                print(str(e))
            except TypeError as e:
                print(str(e))
        elif choice == "2":
            try:
                order = int(input("Enter the order of derivative you want: "))
            except ValueError:
                print("Invalid order, Please enter correct number.")
                continue
            print(pretty(function.diffrentiate(order=order).expression))
        elif choice == "3":
            try:
                function.plot()
            except ValueError as e:
                print(str(e))
        elif choice == "4":
            try:
                order = int(input("Enter the order of derivative you want to plot: "))
            except ValueError:
                print("Invalid order, please enter correct number.")
                continue
            try:
                function.diffrentiate(order=order).plot()
            except ValueError as e:
                print(str(e))
        elif choice == "5":
            point = input("Enter the point(x): ")
            try:
                print(pretty(function.slope(value=point)))
            except ValueError as e:
                print(f"Invalid point, {str(e)}")
        elif choice == "6":
            critical_points = function.critical_points()
            if len(critical_points) == 0:
                print("No critical points found.")
            else:
                print("Critical points: \n")
                print(pretty(critical_points))
        elif choice == "7":
            print("Interval of increasing and decreasing: ")
            print(pretty(function.intervals_of_increase_decreasing()))
        elif choice == "8":
            inflection_points = function.inflection_points()
            if inflection_points is None:
                print("No inflection points found.")
            else:
                print("Inflection points: ", inflection_points)
        elif choice == "9":
            print("Concavity: ")
            print(pretty(function.concavity()))
        elif choice == "10":
            print("Asymptotes: ")
            print(pretty(function.asymptotes()))
        elif choice == "11":
            print("Domain: ", pretty(function.domain))
            print("Range: ", pretty(function.range))
        elif choice == "12":
            mx, mn = function.extrema()
            print("Maximun: ", pretty(mx))
            print("Minimum: ", pretty(mn))
        elif choice.lower() == "m":
            return
        else:
            print("Invalid choice, please enter correct choice.")


def main():
    """Main function for DerivativeXpert."""
    print("\t\t**DerivativeXpert**\n")

    print(
        """DerivativeXpert:
          is the ultimate tool for basic and advanced calculus,
          including plotting, derivatives, limits, and more.
          It provides a comprehensive suite of features to
          assist with various calculus operations,
          making it an essential tool for students and professionals alike."""
    )

    while True:
        print(
            "\nDerivativeXpert is a command-line tool that provides the following features:"
        )
        print("\n1. Basic Calculator: Perform basic arithmetic operations.")
        print("2. Advanced Calculator: Perform advanced calculus operations.")
        print("3. Exit: Exit the program.")
        choice = input("\nChoose the calculator: 1/2/3: ")
        if choice == "3":
            sys.exit("Exiting DerivativeXpert...")
        if choice == "1":
            basic_calculator()
        elif choice == "2":
            advanced_calculator()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
