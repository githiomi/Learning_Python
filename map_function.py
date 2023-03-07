# The map function is an inbuilt python function that takes a function and an iterable
# It returns an interator that performs the function given to all items in the iterable
# Syntax - map(function, iterable)

def make_even(num):
    # A function that takes in a number and returns an even number by adding 1 to odd numbers
    if num % 2 == 0:
        return num
    else:
        return num + 1


def square_num(num):
    return num ** 2


# List of random iterable numbers
nums = [231, 435, 468, 123, 798, 345, 890, 912, 329]
ints = [3, 6, 9, 12, 20]

# Get the result of the map function and put the result in a new list
# Must use list() or will return a map object - used by python to save memory
even_list = list(map(make_even, nums))
sqrd_nums = list(map(square_num, ints))

# Map function is similar to a LIST COMPREHENSION
new_even_list = [make_even(num) for num in nums]
new_sqrd_nums = [square_num(x) for x in ints if x % 2 == 0]  # this will square the number if it is even
# Take each num in nums and pass it to the map_function() function

print(even_list)
print(new_even_list)

print(sqrd_nums)
print(new_sqrd_nums)
