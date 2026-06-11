class Animal :  #Super Class (Parent Class)
    def __init__(self,name):
        self.name = name
    def speak(self):
        print("Speaking Now:")

class Dog(Animal):    #Sub Class (Parent Class)
    def speak(self):
        super().speak()
        print("Woof!")

class Cat(Animal):     #Sub Class (Parent Class)
    def speak(self):
        super().speak()
        print("Meow!")

# Creating objects
my_dog = Dog("Bruno")
my_cat = Cat("Jerry")

my_dog.speak()
my_cat.speak()