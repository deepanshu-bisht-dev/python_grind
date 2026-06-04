# # For writing a table of 5 inside a list we can --

table = []
for i in range(1,11):
    table.append(5*i)

print(table)

# Rather than using this long method we can do it via list comprehension.

table = [5*i for i  in range(1,11)]
print(table)