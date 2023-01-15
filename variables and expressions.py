# There are 5 major datatypes in python
# Variable in python can be changed and the datatype can also change

# 1. Numbers
my_int = 5  # Integers
my_float = 13.2  # Floats
my_complex = 25j  # Complex numbers - Alphanumeric values

# 2. Strings
my_string = "Daniel"  # Double quotes
my_string_single = 'Dhosio'  # Single quotes

# 3. Boolean
my_boolean = True
her_boolean = False

# 4. Sequence Types
# Lists
my_list = [1, "two", 3, 4.5, True]  # List - A collection of arrays that is changeable and ordered (have indexes)
# To change the values in a list
my_list.append(30)  # this will add the value to the end of the list
my_list.insert(3, 'Dhosio')  # this will add the value to the specified index in the list

# Tuples
my_tuple = (0, 1, 2, 3, 4, 4)  # Tuples - Immutable (Cannot be changed)

# To check the number of occurrences of an element in a tuple
my_tuple.count(4)

# 5. Dictionaries
my_dict = {"one": 1, "two": 2, "three": 3, "four": 4}  # They map unique keys to specific values
dict_two = dict({'five': 5, 'six': 6, 'seven': 7, 'eight': 8})  # Other method to create dictionaries

# To access elements in a dict
one = my_dict['one']
three = my_dict.get('three')

# To update values in a dict
my_dict['four'] = 5

# To add a new value to the dictionary
my_dict['five'] = 5

# 6. Sets - A collection that is unordered and has no duplicate values
my_set = {10, 20, 30, 40, 50, 50}
# NB - a set has not index values to access objects

# Useful functions
# Using slices to get part of a sequence
print(my_list[1:5])  # Will print from the first to fifth index (Element 2 to 6)
print(my_list[1:5:2])  # Will print from the first to fifth index and skip every other element (start:end:skip)

# How to reverse a sequence
print(my_list[::-1])  # Just prints a reversed copy. Doesn't affect original array

# Values in a dictionary are accessed using their unique keys
print(my_dict["one"])  # Will print the value with the unique key of "one


# Convert an integer to a string
new_string = str(my_int)
print(new_string)

# Finding elements in a string or list
# Syntax - <variable_name>.find(x) - Will return the int index of the specified element (x)
print(my_string.find('a'))  # Will return 2 - The index of 'a' in 'Daniel'

# Count will return the number of elements present in the string or list
# Syntax - <variable_name>.count(x) - Will return the int number of the specified element (x)
print(my_string.count('d'))

# How to split a string into a list of elements
# Syntax - <string_name>.split(x) - Will split the string based on the delimiter (x)
new_string = "Hello world this is a new string"
print(new_string.split())  # Will split based on the spaces between words
# Split based on a delimiter
print(new_string.split('.'))

# String slice operator
# Syntax - <string_name>[start:stop(+1):step] - a blank will default to the start or the end
print(my_string[2:])  # Start at index 2 to the end
print(my_string[:3])  # Start from the beginning to index 3
print(my_string[::3])  # From beginning to end but stepping by 3


# How to change the value of a global variable
global_string = 'This is a string'
print(global_string)


def change_value():
    # print(f'---- {global_string}')  # Will print out 'This is a string'

    # To change its value
    global global_string  # Telling python to change the global variable
    global_string = 'This is by Daniel'
    print(f'Changed global variable: {global_string}')

    # Local variable
    local_string = 'This is a local variable'
    print(local_string)  # Will print out 'This is a local variable'


# Method call
change_value()

# How to delete a variable
del global_string  # Telling python to delete the global variable. The variable will not exist after this

# Type Conversion
# Change the data type of variable using the following
int()
str()
float()
tuple()
list()
set()
dict()
