array = (1,2,3,4,5,6)

print(f"Our Array is: {array} and Arrays Type is: {type(array)}")
array = list(array)
print(f"Our Array is: {array} and Arrays Type is: {type(array)}")
array.remove(3)
array = tuple(array)
print(f"Our Array is: {array} and Arrays Type is: {type(array)}")
