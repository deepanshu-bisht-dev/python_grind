'''Write a program using match case that simulates a simple calculator.
Ask the user for two numbers and an operation (+, -, *, /).
Perform the operation using match case.'''

a = int(input("Enter first number"))
b = int(input("Enter second number"))
operation = input("Choose operation")

match operation:
    case "+":
        print(a+b)
    case "-":
        print(a-b)
    case "*":
        print(a*b)
    case "a/b":
        print(a/b)