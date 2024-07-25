"""Main program for DerivativeXpert."""

import sys
from basic_calculator.basic_calc import BasicCalculator
from advanced_calc.function import Function

def basic_calculator():
    """Basic calculator function."""
    while True:
        try:
            exp= input("Enter the exepression or 'm' to main menu:")
            if (exp== "m"):
                return
            basicCalculator = BasicCalculator(exp)
        except:
            print("oooopppps, Invalid expression")
            continue
        print(basicCalculator.evaluate_expression())



def advanced_calculator():
    """Advanced calculator function."""
    while True:
        try:
            fun= input("Enter the function or 'm' to main menu:")
            if (fun== "m"):
                return
            function = Function(fun)
        except:
            print("oooopppps, Invalid Function")
            continue
        print("""
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
""")
        choice= input("Enter the choice or 'm' to main menu:")
        if (choice== "1"):
            x= input("Enter x: ")
            try:
                print(function.evaluate(x))
            except ValueError as e :
                print(str(e))
                
        elif choice =="2":
            try:
                order= int(input("Enter the order of derivative you want: "))
            except:
                print("Invalid number, please enter correct number.")
            print(function.diffrentiate(order=order).expression)
        elif choice =="3":
            function.plot()
        elif choice =="4":
            try:
                order= int(input("Enter the order of derivative you want to plot: "))
            except:
                print("Invalid number, please enter correct number.")
            function.diffrentiate(order=order).plot()
        elif choice =="5":
            try:
                point= int(input("Enter the point(x): "))
            except:
                print("Invalid point, please enter correct number(x).")
            function.slope(point= point)
        # elif choice =="6":
        # elif choice =="7":
        # elif choice =="8":
        # elif choice =="9":

def main():
    """Main function for DerivativeXpert."""
    print("\t\t**DerivativeXpert**\n")

    print("""DerivativeXpert:
          is the ultimate tool for basic and advanced calculus,
          including plotting, derivatives, limits, and more.
          It provides a comprehensive suite of features to assist with various calculus operations,
          making it an essential tool for students and professionals alike.""")

    while True:
        print("\nDerivativeXpert is a command-line tool that provides the following features:")
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
