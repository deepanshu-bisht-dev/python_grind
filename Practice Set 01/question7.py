# Print the multiplication table of a number (entered by user).

n = int(input("Enter the number whose table you want"))

for i in range(1,11):
    print(n,"X",i,"=",n*i)