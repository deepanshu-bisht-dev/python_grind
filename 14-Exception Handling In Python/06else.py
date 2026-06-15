'''The else block is optional and is executed only if no exception occurs within the try block. It's useful for
code that should run only when the try block succeeds.'''

try :
    a = int(input("Enter a number"))
    b = 900/a
except Exception as e:
    print(e)
else :
    print("Hey, there  are no errors, your code can run smoothly.")
