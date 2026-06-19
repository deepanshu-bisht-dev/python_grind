# If we are operating on read mode and an error occurs showing FileNotFound . We can manage that error by using except function.
try:
    f = open("ram.txt","r")
    content = f.read()
    print(content)
    f.close()
except FileNotFoundError:
    print("The file path is incorrect")
