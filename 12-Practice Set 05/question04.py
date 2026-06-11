'''Create a base class Animal with a method sound() that prints "Some sound".
   Create a derived class Dog that overrides sound() to print "Bark!".
   Create an object of Dog and call sound().'''

class Animal :
    def sound(self):
        print("Some sound")

class Dog(Animal):
    def sound(self):
        super().sound()
        print("Bark")

a = Animal()
a.sound()

b = Dog()
b.sound()