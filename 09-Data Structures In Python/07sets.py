# Sets are unordered collection of elemens but here all the elements are unique(no duplicates)
set = {23,34,45,56}
print(set)
print(type(set))

a = {3,5,4,5,7,9}
print(a) # The output will automatically remove duplicate values.

# Few set methods 
b = {5,7,9,0,3}
b.add(8)
print(b)

b.remove(5)
print(b)

b.discard(6)
print(b)

b.pop()
print(b)