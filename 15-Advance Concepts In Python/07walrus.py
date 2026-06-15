'''It is used in conditional expressions,list comprehensions, reading files.
In conditional expressions, the most common use case is within if statements, while loops , and its comprehensions,
where you need to both test a condition and use the value that was tested. '''

# Without Walrus Operator 
'''data = input("Enter a value (or 'quit' to exit):")
while data != "quit":
    print(f"You entered {data}")
    data = input("Enter a value (or 'quit' to exit):")
'''
# With walrus operator:
while (data := input("Enter a value (or 'quit' to exit):")) != "quit":
    print(f"You entered {data}")

# In the "with walrus" example the input is assigned to data and compared to "quit"  in a single expression.