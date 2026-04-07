## Calculadora Simples

def sum(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b
def pi():
    return 3.14159626535897932384626433832795
def e():
    return 2.7182818284590452353602874713527

def main():
    while True:
        operation = input("Enter the operation (sum, subtract, multiply, divide, pi, e, exit): ")
        if operation == "sum" or operation == "Sum":
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            print(f"The result of {a} + {b} is: {sum(a, b)}")
        elif operation == "subtract" or operation == "Subtract":
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            print(f"The result of {a} - {b} is: {subtract(a, b)}")
        elif operation == "multiply" or operation == "Multiply":
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            print(f"The result of {a} * {b} is: {multiply(a, b)}")
        elif operation == "divide" or operation == "Divide":
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            print(f"The result of {a} / {b} is: {divide(a, b)}")
        elif operation == "pi" or operation == "Pi":
            print(f"Pi: {pi()}")
        elif operation == "e" or operation == "E":
            print(f"E: {e()}")
        elif operation == "exit" or operation == "Exit":
            print("The end of the program!")
            break
        else:
            print("Invalid operation. Please try again.")
        print()

if __name__ == "__main__":
    main()

