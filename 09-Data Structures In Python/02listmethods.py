marks = [25,45,56,78,96]
marks.append(98)
print(marks) # This method will append the given element in the list.
marks.pop()
print(marks) 
marks.insert(3,23) # This will insert an elemnt in the list.
print(marks)
marks.remove(25)
print(marks)
marks.sort()
print(marks)
marks.reverse()
print(marks)

extra_marks = [87,45,67,89,67,90,89]
marks.extend(extra_marks)
print(marks)