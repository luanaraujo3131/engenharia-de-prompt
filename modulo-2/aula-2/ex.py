# Simple Calculator - Object-Oriented Refactor

import math
from typing import Callable, Any

class Calculator:
    """A simple calculator class with basic operations and constants."""

    def __init__(self):
        self.operations = {
            'add': self._create_binary_op(lambda a, b: a + b, '+'),
            'subtract': self._create_binary_op(lambda a, b: a - b, '-'),
            'multiply': self._create_binary_op(lambda a, b: a * b, '*'),
            'divide': self._create_binary_op(self._safe_divide, '/'),
            'pi': self._create_constant(math.pi, 'Pi'),
            'e': self._create_constant(math.e, 'E'),
        }

    def _create_binary_op(self, func: Callable[[float, float], Any], symbol: str) -> Callable[[], None]:
        """Create a handler for binary operations."""
        def handler():
            try:
                a = float(input(f"Enter first number: "))
                b = float(input(f"Enter second number: "))
                result = func(a, b)
                print(f"{a} {symbol} {b} = {result}")
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
        return handler

    def _safe_divide(self, a: float, b: float) -> Any:
        """Perform safe division with zero check."""
        return a / b if b != 0 else "Error: Division by zero"

    def _create_constant(self, value: float, name: str) -> Callable[[], None]:
        """Create a handler for constant values."""
        def handler():
            print(f"{name} = {value}")
        return handler

    def run(self):
        """Run the interactive calculator loop."""
        print("Welcome to the Calculator!")
        print("Available operations: add, subtract, multiply, divide, pi, e, exit")

        while True:
            operation = input("\nEnter operation: ").lower().strip()

            if operation == 'exit':
                print("Goodbye!")
                break
            elif operation in self.operations:
                self.operations[operation]()
            else:
                print("Invalid operation. Please try again.")

if __name__ == "__main__":
    calc = Calculator()
    calc.run()