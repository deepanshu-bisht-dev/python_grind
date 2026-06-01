# Write a program that counts how many vowels are in a given string.

string = "My name is Deepanshu Bisht and I am 19 years old."
sum = 0
vowels = ['a','e','i','o','u']

for char in string.lower():
    if (char in vowels):
        sum +=1

print(f"The number of vowels in the given string is {sum}")
 
