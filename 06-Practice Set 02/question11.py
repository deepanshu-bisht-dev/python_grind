# Take a user input string and check if it is a palindrome (same forwards and backwards).
string = str(input("Enter the string"))

if( string == string[::-1]):
    print("The given string is palindrome")
else :
    print("The given string is not a palindrome.")