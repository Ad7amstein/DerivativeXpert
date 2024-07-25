"""Main program for DerivativeXpert."""

import sys
from basic_calculator.basic_calc import BasicCalculator


def basic_calculator():
    """Basic calculator function."""

def advanced_calculator():
    """Advanced calculator function."""

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
