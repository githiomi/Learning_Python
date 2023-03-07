# Lambdas are anonymous functions that are short term functions with only one expression

# Normal function
def add_five(num):
    return num + 5


# Lambda notation
# Syntax -> <function_name> = 'lambda' <expression>
add_three = lambda x: x + 3

print(add_three(4))


# they can also be used in other functions
def add_val(num, val):
    # Lambda
    lam_func = lambda x: x * 2  # Function to double the number
    return lam_func(num) + val  # After doubling, add the value


print(add_val(10, 5))

# Multiple parameter lambdas
lambda_sum = lambda x, y, z: x + y + z
print(lambda_sum(2, 3, 4))

# They can also be used inside map and filter functions
# Inside map
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

mapped_list = list(map(lambda x: x * 2, nums))
filtered_list = list(filter(lambda y: y % 2 == 0, nums))

print(mapped_list)
print(filtered_list)
