'''Create a set my_set = {1, 2, 3, 3, 4} and print it.
 (What happens to duplicate 3?)

Add 5 to the set, remove 2, and check if 4 is in the set.'''

my_set = {1,2,3,3,4}

print(my_set)
# Sets data type will remove all the duplicates and wil print the unique, unordered collection.

my_set.add(5)
print(my_set)

my_set.remove(2)
print(my_set)

if 4  in my_set:
    print("Yes it is.")
else:
    print("No,it is not")