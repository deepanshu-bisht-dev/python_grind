class Dog : # We define a class called Dog.
    species = "Canis famialris" #A class attribute shared by all dogs.

    def __init__(self,name,breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(F"{self.name} says Woof! ")

my_dog = Dog("Buddy","Golden Retriever")
another_dog = Dog("Lucy", "Labrador")

# We can access their attributes
print(my_dog.name)
print(my_dog.breed)
print(another_dog.name)
print(another_dog.breed)

# We can make them perform actions too...
my_dog.bark()
another_dog.bark()      
        