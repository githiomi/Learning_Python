# Arrays - A data structure with an ordered series of elements

# A list and array store data the same way but an array ONLY HOLDS ONE DATA TYPE but
# a list can hold any data type

# Creating an array
# must import the array module
import array as arr
# or from array import *

# Method 1
# nameOfArray = moduleAlias.constructor('dataType', ['Array', 'Elements'])
array = arr.array('i', [1, 2, 3, 4, 5])

# use 'i' for int, 'd' for float

# Method 2 - using import *
# nameOfArray = constructor('dataType', ['Array', 'Elements'])
# array_two = array('i', [1, 2, 3, 4, 5])


# Accessing array elements
# Starts from 0. Length of array = index + 1
print(array[2])  # 3

# Negative index (-i) will start from the end (right)
print(array[-1])  # 5

# Array operations
# len() will return the int number of elements
print(len(array))  # 5

# Add elements to an array
# append() - add an element to the end of the array
array.append(6)

# extend([7, 8, 9]) - will add more than one element to the end of the array
array.extend([8, 9, 10])

# insert(x, y) - will insert a new element (y) at the specified index (x)
array.insert(8, 7)

# Removing elements from an array
# pop(x) - removes and returns the popped element
array.pop()  # Will remove the last element from the array
array.pop(5)  # Will remove the element at the specified index (5)

# remove(y)
array.remove(5)  # Removes the element specified in the parentheses. Will remove the first occurrence of 5

# Array concatenation - Can only be for arrays of the same data type
array_one = arr.array('i', [9, 8, 7, 6, 5])
array_two = arr.array('i', [2, 4, 6, 8, 0])
empty_array = arr.array('i')  # To create an empty array

empty_array = array_one + array_two  # Will concatenate array 1 and array 2 and store it in the empty array

# Slicing an array
# Done using : to return the elements in the given range
print(array[2:5])  # Start:End but will not include the last element (Start:End-1)

# Iteration in array
# For loop
for x in array:
    print(x)

for z in array[2:5]:
    print(z)

# While loop
temp = 0
while temp < array[3]:  # when temp < 4
    print(array[temp])
    temp += 1  # increase the temp counter

tempo = 0
while tempo < len(array):
    print(array[tempo])
    tempo += 1  # increase the tempo counter
