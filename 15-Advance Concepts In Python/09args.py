'''*args collects any extra positional arguments passed to a function into a tuple. The name args is just a 
convention, you could use any valid variable name preceded by a single asterisk(eg. *values,*numbers).
'''
def my_function(*args):
    print(type(args))
    print(args)

my_function(1,2,3,"hello", 4, 8, "deepanshu")

def sum(*args):
    total = 0
    for items in args:
        total += items
    return total

print(sum(12,34,56,47.8,56,67,567,35,24,45,67,7))
    