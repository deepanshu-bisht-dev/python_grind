''' Write a program that asks the user for a number 
and prints whether it is positive, negative, or zero.'''

a = int(input("Enter a number"))

if(a>0):
    print("Given number is positive")
elif(a==0):
    print("Given no. is zero")
else:
    print("Given number is negative")