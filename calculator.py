# Simple calculator to perform basic arithmetic operations

def calculator():
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            result = "Cannot divide by zero!"
        else:
            result = num1 / num2
    else:
        result = "Invalid operator!"

    print(f"Result: {result}")

if __name__ == "__main__":
    calculator()
