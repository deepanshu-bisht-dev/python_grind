'''**kwargs collect any extra keyword arguments passed to a function into a dictionary. Again, kwargs is the
conventional name, but you could use any valid variable name preceded by two asterisk(eg. **data,**marks).'''

def my_function(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(f"{key}:{value}")

my_function(name = "Alice", age = 30, city = "New York")