'''Static methods are marked with the @staticmethod decorator. They are similar to regular functions, except they
 are defined within the scope of a class.

They don't take self or cls as parameters.
They are useful when a method is logically related to a class but doesn't need to access or modify the instance or
class state.
Often used for utility functions that are related to the class'''

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

print(MathUtils.add(3, 5))  

#Can also be called on an instance
m = MathUtils()
print(m.add(4,5)) # 9