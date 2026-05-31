# Syntax to perform string slicing is string[start:stop:step]

text =  ("Hello Deepanshu")
print(text[0:10])
print(text[3:13])
print(text[0:15:2]) # step means to skip (n-1) step. In this case its (2-1) ie. 1.
print(text[:12]) # It is same as [0:12]
print(text[3:]) #It is same as [3:end of the string]
print(text[::2])