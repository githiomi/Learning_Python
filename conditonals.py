# Variables
x = 10
y = 20

# If Else statements
if x < y:
    print(f'{x} is less than {y}')
elif x > y:
    print(f'{x} is greater than {y}')
else:
    print('They are equal')

# Logical Operators
# And - Both must be true for the result to be true. If one is false, it will all be false
print(x < y and y > x)

# Or - Either one of the conditions need to be true. If only one is true, it will all be true
print(x < y or y <= x)

# Not - Will change the return value (false to true || true to false)
bool_not = (x < y and y > x)  # Will initially return true
print(not bool_not)


# Identity operators - Used to compare objects
list_one = [1, 2, 3]
list_two = [1, 2, 3]

print(list_one == list_two)  # Will return true because the content in the lists are the same

# is - will return true if the objects being compared are of the same object type
my_var = list_one

print(my_var is list_one)  # Will return true because they are the same object type
print(list_one is list_two)  # Will return false because they are NOT of the same object type

# is not - will return true if the objects being compared are NOT of the same object type
print(list_one is not list_two)  # Will return true because they are NOT of the same object type


# Membership operators - Used to check if a sequence is present in an object
# in
print(10 in list_one)  # Will return true because 10 is in the list

# not in
print(10 not in list_two)  # Will return false because 10 is in the list
