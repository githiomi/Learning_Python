# This is used to try and catch errors if any exist to prevent program crashing
# Example to convert string to int

# Get input from user and convert to int
user_input = input("Enter something: ")

try:
    # Initial code to do if no error occurs
    new_int = int(user_input)
    print(f'Converted to: {new_int}')
except:
    # Code that will be executed when an error occurs
    print(f'Cannot convert {user_input} into an int')
