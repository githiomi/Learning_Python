# Recursion is the act of a function calling itself within its body to solve a problem
# Recursion is a function calling another function which is itself

# Example - To get the factorial of a number
# Algorithm ->
# 1. Get the number
# 2. Multiply the current number by the number below itself (number - 1)
# 3. Therefore, call the same function on the (number - 1)


def number_factorial(number):
    # Create a base case - This is what terminates the function from recusing forever
    if number == 1:
        return 1

    # If the number is not reduced to 1, then
    return number * (number_factorial(number - 1))
