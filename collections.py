# These are built in container data type
# They include:
# lists - using []. It is mutable. Can store duplicates. Accessed using indexes,
# tuple - using(). It is immutable. Ordered. Can have duplicates. Accessed using indexes,
# sets - using{}. It is unordered. Doesn't allow for duplicates. Cannot be accessed using indexes,
# dictionaries - using{}. Made of key:value pairs. It is mutable. Can be accessed using indexes.


# From the collection module in python
from collections import namedtuple, deque, Chainmap

# They have specialised data structure that used to cover the shortcomings of the 4 collections above
# 1. Named tuple - returns a tuple with a named value to help access values
title = namedtuple('nameOfTheTuple', 'itemName1, itemName2')
content = title('Daniel', 'Githiomi')

# Using a list to enter values into a tuple
new_content = title._make(['Dhosio', 'Hoes'])

print(content)
print(new_content)


# 2. Deque - an optimised list to improve insertion and deletion
my_list = ['a', 'b', 'c', 'd']
my_deque = deque(my_list)

# To insert a value to the end
my_deque.append('e')
# To insert at the beginning
my_deque.appendLeft('z')
# To remove the last element
my_deque.pop()
# To remove the first element
my_deque.popLeft()


# 3. Chainmap - A dictionary that create a single view for multiple mappings/dictionaries
dict_one = {'f_name': 'Daniel', 'l_name': 'Githiomi'}
dict_two = {'nf_name': 'Dhosio', 'nl_name': 'Hoes'}

chainmap = Chainmap(dict_one, dict_two)
print(chainmap)
