'''You can handle multiple types of exceptions using multipleexcept blocks or by specifying a tuple of exception
 types in a single except block.'''

try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(result)
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Invalid input! Please enter a number.")