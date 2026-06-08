# Class - Class basically is a blueprint or a template used for creating multiple objects.

# Object - Specific instance created from a tempelate(class).

class Employee:
    company = "HP"

    def get_salary(self): # self is important here because self is referring to the object of the class which is being created.

        return 34000
    
e1 = Employee()
print(e1.get_salary())

e2 = Employee()
print(e2.get_salary())

print(e2.company)
