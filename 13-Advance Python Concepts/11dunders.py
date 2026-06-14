'''__str__ and __repr__ - String Representation
__str__ - This method should turn a human readable, informal  string representation of an object. It can be used by using
str() function and print().
__repr__ - This method should turn an ambiguous, official string representation of the object. Ideally this string
should be a valid python expression that could be used to recreate the object. It's used by the repr() function
and in the interactive interpreter when you just type the object's name and press Enter.
'''
class person :
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Person({self.name},{self.age})" #User friendly
    def __repr__(self):
        return f"Person(name = '{self.name}' age = '{self.age}')" # Unambiguous for debugging
p = person("Amit",30)
print(str(p))
print(repr(p))
print(p)
        
