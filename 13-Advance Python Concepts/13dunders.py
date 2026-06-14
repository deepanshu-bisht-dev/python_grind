'''__add__ , __sub__ , __mul__ , etc. - Operators Overloading
These methods allow you to define how your objects behave with standard arithmetic and comparison operators. '''

class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self,other):
        return Vector( self.x + other.x, self.y + other.y )
    def __sub__(self,other):
        return Vector( self.x - other.x, self.y - other.y )
    def __mul__(self, scalar):
        return Vector( self.x * scalar, self.y * scalar)
    def __str__(self):
        return f"Vector({self.x},{self.y})"
    

v1  = Vector(2,3)
v2  = Vector(4,5)
v3 = v1 + v2 # calls __add__
print(v3)
v4 = v1 - v2  # calls __sub__
print(v2)
v5 = v1 * 5  # calls __mul__
print(v5)