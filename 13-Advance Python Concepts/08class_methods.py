'''A class method is marked with the @classmethod decorator. It takes the class itself(cls) as its first parameter,
rather than the instance(self). Class methods are often used for:
- Modifying class attributes - They can change the state of the class, which affects all instances of the class.
- Factory methods: They can be used as alternative constructors to create instances of the class in different ways.
'''

class Animal :
    species = "Mammal" # CLass Attribute

    @classmethod
    def set_species(cls, new_species):
        cls.species = new_species  # Modifies class attribute
 
    @classmethod
    def get_species(cls):
        return cls.species
 
print(Animal.get_species()) 
Animal.set_species("Reptile")
print(Animal.get_species())  
 
# You can also call class methods on instances, but it's less common:
a = Animal()
print(a.get_species()) # Reptile