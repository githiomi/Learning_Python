# Pandas import
# import pandas as pd

# Hashmap or Hash table
# This is a data structure that maps keys to its value pairs
# It implements the abstract array data type
# Makes use of a hash function that computes an index value to be matched to a value

# Normal dictionary
my_dict = {'f_name': 'Daniel', 'l_name': 'Githiomi', 'age': 21}

# Nested dictionaries
nested_dict = {
    'Employees': {
        'Daniel': {'id': '001', 'name': 'Daniel Githiomi', 'role': 'Developer'},
        'Ava': {'id': '002', 'name': 'Ava Chum', 'role': 'Project Manager'}
    }
}

# Accessing dictionary values
print(my_dict.keys())  # Will return all the keys
print(my_dict.values())  # Will return all the values

# Using key values
print(my_dict['l_name'])  # Will print the value that corresponds to the key 'l_name'

# Using get
print(my_dict.get('age'))  # Will print the value that corresponds to the key 'age'

# Using for loop
# To get all the keys
for x in my_dict:
    print(x)

# To get all the values
for z in my_dict.values():
    print(z)

# To get the key:value pairs
for k, v in my_dict.items():
    print(f'Key: {k} --- Value: {v}')

# Update the values on a dictionary
my_dict['age'] = 23  # Will change 21 to 23

# Adding a new key:value pair
my_dict['phone'] = '23057118407'

# Deleting values from a dictionary
# Using pop('x') - will remove the key:value pair with the specified key 'x'
my_dict.pop('phone')

# Using .popitem() - will remove the key:value pair at the end of the dictionary
my_dict.popitem()  # This will remove the age key:value pair

# To print out the updated dictionary
print(my_dict)

# Using delete - Will delete the key:value pair with the specified key
del my_dict['l_name']

# Converting a dictionary to a data frame
# A Data Frame - A 2D data structure that has columns of various types
# Example data frame - pandas (needs to be imported)
new_data_frame = pd.DataFrame(nested_dict['Employees'])
print(new_data_frame)
