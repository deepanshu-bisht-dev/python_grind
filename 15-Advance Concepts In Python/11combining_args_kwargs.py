'''You can use both *args and **kwargs in the same function definition. The order is important: *args
must come before **kwargs. You can also include regular positional and keyword parameters.'''
def my_function(a, b, *args, c=10, **kwargs):
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"args: {args}")
    print(f"c: {c}")
    print(f"kwargs: {kwargs}")

my_function(1, 2, 3, 4, 5, c=20, name="Bob", country="USA")

my_function(1,2)
