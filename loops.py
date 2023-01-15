import random as random

# Loops - These are statements that is executed multiple times
# Types of loops - Infinite (Will not end). Finite (Will end)

# Categories - Post-test and Pre-Test
# Python only has pre-test loops

# 1. While loop - When the number of iterations is unknown
limit = 9
counter = 0

while counter <= 3:
    print(f'Number: {counter}')
    counter += 1

print(f'Outside of the loop. Goodbye\n')

# 2. For loop - When the number of iterations is known. Must have a boolean, the initial value and the
# increment/decrement
fruits = ['Apples', 'Mangoes', 'Oranges']

for fruit in fruits:
    print(f'Current fruit: {fruit}')


# 3. Nested loops
# Simply having one loop inside another loop


# Example of while loop
# A guessing game - imported random to help guess a random number
int_limit = 10
to_be_guessed = int(limit * random.random()) + 1
guessed_number = 0

while guessed_number != to_be_guessed:
    guessed_number = int(input('\nEnter a number: '))

    if guessed_number > 0:

        if guessed_number > to_be_guessed:
            print(f'{guessed_number} is too large')
        elif guessed_number < to_be_guessed:
            print(f'{guessed_number} is too small')

    else:
        # If a negative number is input
        print(f'Dont give up. {guessed_number} was the expected number!')
        break

# When the number is guessed correctly
print(f'You guessed {guessed_number} correctly. Congratulations.')


# Example of for loop
# To print the factorial of a number
fact_num = int(input('\nEnter a number: '))
factorial = 1

# Check number validity
if fact_num < 0:
    print('Number must be positive')
elif fact_num == 0:
    print('Must be greater than zero')
else:
    # For loop
    for i in range(1, fact_num + 1):  # Will create a range from 1 to the number itself. Without +1, it's not included
        factorial *= i

print(f'Factorial of {fact_num} is {factorial}')
