# The with statement provides a cleaner way to work with files.
# It automatically closes the file, even if errors occur.

try :
    with open("17-File IO/deep.txt","r") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("File not found")


try: 
    with open("17-File IO/abhiraj.txt","a") as file :
        string = '''Abhiraj is kinda cute too.'''
        file.write(string) 
except FileNotFoundError:
    print("File not found")
      