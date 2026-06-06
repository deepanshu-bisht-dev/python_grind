'''Write a program that takes a list of numbers and removes 
all duplicates using a set.'''

def remove_duplicates(numbers):
    ''' 
    Remove duplicates from a list using set.
    
    Parameter : (list) : A list of integer or floats.
    Returns : (list) : A new list with duplicates removed.
    '''
    return list(set(numbers))

num = [1,2,3,4,2,3,5,4,6,5,6,8]
print("Original List :", num)
print("Without Duplicates :", remove_duplicates(num))