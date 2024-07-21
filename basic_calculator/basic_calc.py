"""
basic_calc.py

This module defines a basic calculator class for evaluating mathematical expressions using the sympy library.
The calculator validates the given expression before attempting to evaluate it. 

Classes:
    BasicCalc: A class to validate and evaluate mathematical expressions.
"""

import sympy as sp

class BasicCalculator :
    """
    A basic calculator class for evaluating mathematical expressions.
    """
    expression = ""

    def __init__(self, expr ) :
        """
        Initializes the calculator with a given expression.
        
        :param expr: A string representing the mathematical expression.
        """
        self.expression = expr
        self.result = None


    @property
    def expression (self) :
        return self.__expression
    
    @expression.setter
    def expression (self, expression) :
        if (not self.is_valid_expression(expression)) :
            raise ValueError ("Invalid expression") 
        self.__expression = expression


    @staticmethod
    def is_valid_expression(expression):
        """
        Validates the given mathematical expression.
        
        :param expr: A string representing the mathematical expression.
        :return: True if the expression is valid, False otherwise.
        """
        try :
            sp.sympify(expression)
            print("11111111111")
            return True
        except :
            return False
        
    def evaluate_expression (self):
        """
        Calculates the result of the stored mathematical expression if it is valid.
         
        :return: The evaluated result of the expression formatted to three decimal places,
                 or a string "invalid expression".
        """
        if (self.is_valid_expression(self.__expression)) :
            res = sp.sympify(self.__expression).evalf()
            self.result = format(res, ".3f")
            return self.result
        else :
            return "Invalid expression"
        

        


expr = "8+gff"
calculator = BasicCalculator(expr)
# result = calculator.evaluate_expression()
# print(f"Result: {result}")   















