#  Positional Arguments
def create_profile(name,age):
    return f"My name is {name} and I am {age} years old."

print(create_profile("Deepanshu",29))
print(create_profile("Amit",23))
print(create_profile("Abhiraj",29))
print(create_profile("Sameer",69))
print(create_profile("Ayush",26))
print(create_profile("Vaibhav",26))

# Default Arguments

def add(a,b,c=34):
    return(a+b+c)
print(add(34,45))  

# Keywords Arguments

def about(name, id):
    return(f"My name is {id} and my id is {name}")

print(about(id="Deepanshu",name =34))

