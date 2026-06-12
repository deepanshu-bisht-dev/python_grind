# Rather than calling the f we can directly alter our function using decorator by this:
def decorator(func):
    def wrapper():
        print("I am about to execute a function...")
        func()
        print("I have executed this function...")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()