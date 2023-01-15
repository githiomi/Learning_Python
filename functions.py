# These are blocks of related lines of code that aare meant to achieve a certain result
# Function syntax - def <function_name>(<any_parameters>):
def print_name(user_name):
    return f'My name is {user_name}'


# Call the function and pass parameters
name = 'Dhosio'
function_result = print_name(name)
print(function_result)


# Optional parameters
# Setting default parameters in functions
def function_example(age, user_name='Daniel'):  # This is to set a default optional parameter value
    print(f'{user_name}, you are {age} years old')


# Method call
function_example(21)  # This will change the value of the optional parameter
# If 'Githiomi' is not given, then 'Daniel' will be used

# Python decorators
# They are design patterns that allows a user to add new functionality to an object without changing its structure
# It wraps another functions and returns a callable
