x=10 #Global Variable - They are accessible everywhere in the program.

def my_func():
    x = 5 #Local Variable - They get destroyed as the function is halted.
    print(x)
   
my_func()
print(x)
    

