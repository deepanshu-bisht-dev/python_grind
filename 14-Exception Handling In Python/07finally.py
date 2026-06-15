'''The finally block is also optional and is always executed, regardless of whether an exception occurred or not.
It's typically used for cleanup operations, such as closing files or releasing resources.'''

try:
    a = int(input("Enter number 1 : "))
    b = int(input("Enter number 2 : "))
    print(f"The sum of the given numbers is {a+b}")

except Exception as e:
    print("Some error occured.",e)

finally :
    print("I am good")