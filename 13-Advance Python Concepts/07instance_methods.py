'''Instance methods are the default type of method in python classes. They require an instance of the class to 
be called, and they aurtomatically recieve the instance as the first argument(self).'''


class Dog:
    def __init__(self,name):
        self.name = name

    def sound(self):
        return f"{self.name} says woof!"
    
dog = Dog("Buddy")
print(dog.sound())
