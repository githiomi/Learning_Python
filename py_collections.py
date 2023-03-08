# These are built in container data type
# They include:
# lists - using []. It is mutable. Can store duplicates. Accessed using indexes,
# tuple - using(). It is immutable. Ordered. Can have duplicates. Accessed using indexes,
# sets - using{}. It is unordered. Doesn't allow for duplicates. Cannot be accessed using indexes,
# dictionaries - using{}. Made of key:value pairs. It is mutable. Can be accessed using indexes.


# From the collection module in python
from collections import namedtuple, deque

# They have specialised data structure that used to cover the shortcomings of the 4 collections above
# 1. Named tuple - returns a tuple with a named value to help access values
# All named tuple functions/methods begin with an underscore
# Syntax -> <name_of_tuple> = 'namedtuple' (<name_of_tuple>',  iterable) --- Iterables can be string, list or dict
title = namedtuple('nameOfTheTuple', 'itemName1, itemName2')
content = title('Daniel', 'Githiomi')

# Example
point = namedtuple('point_tuple', 'f_name, l_name, age')
# Acts like a class and then assigns the elements of the 2nd argument below
person = point('Daniel', 'Githiomi', 21)

# Print the person named tuple
print("Person ----- ", person)
# To access the individual elements
print("Person age ----- ", person.age)

# Using a list to enter values into a tuple
new_content = title._make(['Dhosio', 'Hoes'])

print(content)
print(new_content)

# Named Tuple methods
# To get elements by index
print(person[1])  # This will get the second element
# You can also print is a dictionary
print(person._asdict())
# To get the fields inside the tuple
print(person._fields)

# 2. Deque - an optimised list to improve insertion and deletion
my_list = ['a', 'b', 'c', 'd']
my_deque = deque(my_list)

# Deque methods
# To insert a value to the end
my_deque.append('e')
# To insert at the beginning
my_deque.appendleft('z')
# To remove the last element (right)
my_deque.pop()
# To remove the first element (left)
my_deque.popleft()
# To add multiple elements from a string/list/tuple to the deque at the end
new_list = ['3', '4', '5', '6', '7', '8']
my_deque.extend(new_list)
# To add at the beginning use -> extendLeft() but will be in reverse order
my_deque.extendleft('hello')
print(my_deque)
# To change the arrangement of elements, we use the 'rotate' method
my_deque.rotate(1)  # Will shift all the elements one space to the right
print(my_deque)
my_deque.rotate(-5)  # Will shift all elements 5 spaces to the left
print(my_deque)

# Deques can also have a fixed length
# This will force that when elements are added, the elements at the beginning must be removed to create space
new_deque = deque(my_list, maxlen=4)
# To add a new element, 'a' will be removed to ensure that the length remains at 4

# 3. Chainmap - A dictionary that create a single view for multiple mappings/dictionaries
dict_one = {'f_name': 'Daniel', 'l_name': 'Githiomi'}
dict_two = {'nf_name': 'Dhosio', 'nl_name': 'Hoes'}

# chainmap = Chainmap(dict_one, dict_two)
# print(chainmap)
