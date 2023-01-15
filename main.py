def get_name() -> str:
    return input('What is your name? ')


def get_age() -> float:
    return float(input('What is your age? '))


def print_hi(name, age) -> str:
    print(f'Hi, {name}. How are you? \nWe know you are {age} years old')  # Press Ctrl+F8 to toggle the breakpoint.


# How to identify the start point of the whole code
# Similar to PSVM for java
if __name__ == '__main__':
    user_name = get_name()
    user_age = get_age()
    print_hi(user_name, user_age)
