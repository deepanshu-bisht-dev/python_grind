class Animal :  #Super Class (Parent Class)
    def __init__(self,name):
        self.name = name
    def speak(self):
        print("Generic Animal Sound")

class Dog(Animal):    #Sub Class (Parent Class)
    def speak(self):
        print("Woof!")

class Cat(Animal):     #Sub Class (Parent Class)
    def speak(self):
        print("Meow!")
# Creating objects

my_dog = Dog("Bruno")
my_cat = Cat("Jerry")

#  They both have a 'name' attribute (inherited from Animal):
print(my_dog.name)
print(my_cat.name)
# They both have a 'speak' method, but it behaves differently:
my_dog.speak()
my_cat.speak()
        
