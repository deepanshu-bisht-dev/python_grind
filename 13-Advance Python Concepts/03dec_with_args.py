# Decorators can themselves work with arguments..
def repeat(n):
    def decorator(func):
        def wrapper(a):
            for i in range(n):
                func(a)
        return wrapper
    return decorator

@repeat(7)
def say_hello(a):
    print(f"Hello {a}")
          
'''It will replace say_hello fumction with this
   def decorator(func):
        def wrapper(a):
            for i in range(n):
                say_hello(a)
        return wrapper
    '''
say_hello("Deepanshu!")

''' This is how it will be interpreted:
  for i in range(7):
    say_hello("Deepanshu!")
'''