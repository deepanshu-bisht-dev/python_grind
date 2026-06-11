'''Create a class Person with a constructor (__init__) that accepts name and age as arguments 
and stores them as instance attributes. Create an object and print the person’s name and age.'''

class Person :
    def __init__(self,name,age):
        self.name = name
        self.age = age

person_1 = Person("Deepanshu",19)
print(person_1.name,person_1.age)
