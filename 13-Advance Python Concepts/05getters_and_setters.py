'''Using @property (Pythonic Approach)
Python provides a more elegant and concise way to implement getters and setters using the @property decorator. 
This allows you to access and modify attributes using the usual dot notation (e.g., p.name) while still having 
the benefits of getter and setter methods.'''

class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):  # Getter
        return self._name

    @name.setter
    def name(self, new_name):  # Setter
        self._name = new_name 

p = Person("Alice")
print(p.name)  

p.name = "Bob"  
print(p.name)  
 