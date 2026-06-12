def say_hello():
    print("Hello!")

# In case I want to modify this functiion in a clean and readable way, I can do it by using DECORATOR...

def decorator(func):
    def wrapper():
        print("I am about to execute a function...")
        func()
        print("I have executed this function...")
    return wrapper

# Decorator is a function that takes a function, it creates a neww function inside its body(wrapper), then it returns that new function.
f = decorator(say_hello)
f()
"""This is how f will look like :
   def f():
    print("I am about to execute a function...")
    print("Hello!")
    print("I have executed this function...")"""