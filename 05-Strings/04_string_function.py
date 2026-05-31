# Strings are immutable. Changing the original string is just perception , strings do not really change.\
# Common string methods :
text = "Hello World"
print(text.upper()) # Change the whole case to uppercase.
print(text.lower()) # Change the whole case to lowercase.
print(text.capitalize()) # Capitalize the first letter of the string.
print(text.title()) # Capitalize the first letter of each word in the string.

# Removing Whitespaces -
s = " hello world "
print(s.strip()) # Remove unwanted spaces from right and left of the string.
print(s.lstrip()) # Remove space from left side.
print(s.rstrip()) # Remove space from right side.

# Finding and Replacing -
x = "Python is fine"
print(x.find("is"))
print(x.replace("fine","awesome"))

# Splitting and Joining-
name = "apple,banana,orange"
fruits= name.split(",")
print(fruits)
new_text = ",".join(fruits)
print(new_text)

# Checking String Properties -
texts = "Python123"
print(texts.isalpha())
print(texts.isdigit())
print(texts.isalnum())
print(texts.isspace())

# Useful built in string function
len(texts)
print(len(texts))

# ord() and chr() - character encoding