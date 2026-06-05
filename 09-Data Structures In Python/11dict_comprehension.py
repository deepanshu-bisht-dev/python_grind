# Just like list comprehension we can do dict comprehension too.

table = {i:5*i for i in range(1,11) }

print(table)

square = {x:x**2 for x in range(1,10)}
print(square)