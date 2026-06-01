'''Take the string "  i love python programming  " and:

>Remove extra spaces from both ends
>Convert it to title case
>Count how many times "o" appears '''

string = "  i love python programming  "
print(string.strip())
print(string.title())
print(string.count("o"))