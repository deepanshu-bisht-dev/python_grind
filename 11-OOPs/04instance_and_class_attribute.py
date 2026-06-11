class Employee:
    company = "Asus" #This is a classs attribute.
    def __init__(self,salary,name,bond,company):
        self.salary = salary
        self.name = name
        self.bond = bond
        self.company = company

    def get_salary(self):
        return self.salary
    def get_info(self):
        print(f"The name of the employee is {self.name}, his salry is {self.salary}. His bond is for {self.bond} years.")

e1 = Employee(340000,"Deepanshu Bisht", 12, "Tesla") 
print(e1.get_salary()) 
e1.get_info()
print(e1.company) # If instance attribute is availiable always the instance attribute is printed.
print(Employee.company)

#  Object Introspection - Using this we can find out all the attributes and methods a particular object has.

print(dir(e1))