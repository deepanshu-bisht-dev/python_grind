# Create student class that take name and marks of 3 subjects as arguments in constructor. Then create a method to print the average

class student:

    def __init__(self, name , marks):
            self.name = name
            self.marks = marks

    def avg(self):
        sum = 0 
        for i in self.marks:
            sum+=i
        print(f"The score of {self.name} is ", sum/3)    

                
s1 = student("Abhiraj", [98,97,95])
s1.avg()
