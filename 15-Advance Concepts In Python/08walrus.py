'''In list comrehension you can avoid repeated calculations or function calls within a list comprehension.'''
numbers = [1, 2, 3, 4, 5]
'''without walrus operator: calculate x*2 twice
results = [x * 2 for x in numbers if x * 2 > 5]
print(results)'''
# with walrus operator: calculate x*2 only once
results = [y for x in numbers if (y := x * 2) > 5]
print(results)