'''
The try-except block is the fundamental construct for handling exceptions.
- The try block contain the code that might raise an exception.
- The except block contains the code that wil be executed if the specific exception occurs within the try block.
'''
while True:

    try:
        a = int(input("Enter number 1 : "))
        b = int(input("Enter number 2 : "))
        print(f"The sum of the given numbers is {a+b}")

    except Exception as e:
        print("Some error occured.",e)

    
