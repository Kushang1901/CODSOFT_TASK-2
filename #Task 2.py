# Simple Calculator in Python

def calculate(operation, num1, num2):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        return num1 / num2 if num2 != 0 else 'Error: Division by zero is not allowed.'

def main():
    print("Welcome to the Simple Calculator")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Choose the operation (add, subtract, multiply, divide): ").lower()

    result = calculate(operation, num1, num2)
    print(f"The result is: {result}")

if __name__ == "__main__":
    main()
