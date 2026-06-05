'''Convert the tuple to a list, change its first element to 50,
and convert it back to a tuple'''
coordinates = (10,20)
coordinates = list(coordinates)

coordinates[0]= 50

coordinates = tuple(coordinates)

print(coordinates)