# Similar to the map function and can be used together
# Filter takes 2 parameters - A function and an iterable (list)
# Syntax -> filter(func(), list)

# Sample list
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Example of a filter function - To check if elements in a list are even
def is_even(num):
    return num % 2 == 0


# This will filter the list of nums and put only even (true) values in the list
filtered_even_list = list(filter(is_even, nums))


def add_value(num):
    # A function that will add a certain value to the initial number
    return num + 3


# We can then use the map function to create a new list that adds a value to the filtered list of nums
val_added_list = list(map(add_value, filtered_even_list))
# Which can also be written as
new_val_added_list = list(map(add_value, filter(is_even, nums)))
# or using list comprehension
comp_list = list(add_value(num) for num in nums if is_even(num))

print(val_added_list)
print(new_val_added_list)
print(comp_list)
