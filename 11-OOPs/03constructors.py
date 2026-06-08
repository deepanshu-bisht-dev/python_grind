# Constructor basically is a special method that automatically runs whenever you create a new object from a class.
class Employee:
    def __init__(self,salary,name,bond):
        self.salary = salary
        self.name = name
        self.bond = bond

    def get_salary(self):
        return self.salary
    def get_info(self):
        print(f"The name of the employee is {self.name}, his salry is {self.salary}. His bond is for {self.bond} years.")

e1 = Employee(340000,"Deepanshu Bisht", 12) 
print(e1.get_salary()) 
e1.get_info()