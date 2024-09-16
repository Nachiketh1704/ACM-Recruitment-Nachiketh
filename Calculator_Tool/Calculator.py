import math
import re

class Calculator:
    def __init__(self):
        pass

    def calculate(self, expression):
        try:
            return self._eval(expression)
        except Exception as e:
            return str(e)

    def _eval(self, expression):
        expression = expression.replace(' ', '')
        return self._parse_expression(expression)

    def _parse_expression(self, expression):
        while '(' in expression:
            expression = self._handle_parentheses(expression)
        expression = self._handle_exponents(expression)
        expression = self._handle_multiplication_division(expression)
        result = self._handle_addition_subtraction(expression)
        return result

    def _handle_parentheses(self, expression):
        pattern = re.compile(r'\([^\(\)]+\)')
        while '(' in expression:
            match = pattern.search(expression)
            if match:
                sub_expr = match.group()[1:-1]
                result = self._parse_expression(sub_expr)
                expression = expression[:match.start()] + str(result) + expression[match.end():]
        return expression

    def _handle_exponents(self, expression):
        while '^' in expression:
            parts = re.split(r'(\^)', expression, maxsplit=1)
            left = parts[0].rstrip()
            right = parts[2].lstrip()
            base = float(self._handle_multiplication_division(left))
            exponent = float(self._handle_addition_subtraction(right))
            result = math.pow(base, exponent)
            expression = expression[:parts[0].rfind(parts[0].split()[-1])] + str(result) + expression[parts[0].rfind(parts[0].split()[-1]) + len(parts[0].split()[-1]) + 1:]
        return expression

    def _handle_multiplication_division(self, expression):
        parts = re.split(r'(\*|/)', expression)
        result = float(parts[0])
        i = 1
        while i < len(parts):
            op = parts[i]
            num = float(parts[i + 1])
            if op == '*':
                result *= num
            elif op == '/':
                if num == 0:
                    raise ZeroDivisionError("Division by zero is not allowed")
                result /= num
            i += 2
        return result

    def _handle_addition_subtraction(self, expression):
        parts = re.split(r'(\+|-)', expression)
        result = float(parts[0])
        i = 1
        while i < len(parts):
            op = parts[i]
            num = float(parts[i + 1])
            if op == '+':
                result += num
            elif op == '-':
                result -= num
            i += 2
        return result

if __name__ == "__main__":
    calc = Calculator()
    while True:
        try:
            expr = input("Enter a mathematical expression (or 'exit' to quit): ")
            if expr.lower() == 'exit':
                break
            print("Result:", calc.calculate(expr))
        except Exception as e:
            print("Error:", e)
