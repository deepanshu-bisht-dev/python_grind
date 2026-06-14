'''__init__ - Object Initialization Method'''

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
     
p = Person("Amit",30)
print(p.name,p.age)