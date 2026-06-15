def is_greater_than_9(x):
    if x>9:
        return True
    else:
        return False
    
a = [2,3,5,6,45,65,32,4,3,45,5,6,46,75,7,67,78,89,42345,3]
new = list(filter(is_greater_than_9,a))
print(new)
