# Classes work as the blueprint for creating objects
# They have attributes, constructors and methods

# Class Example - A class called person (will be inherited by student class)
class Person(object):

    # Class constructor
    def __init__(self):
        # Instantiate class variables
        self.f_name = 'Daniel'
        self.l_name = 'Githiomi'
        self.age = 21

    # Class methods
    def birthday(self):
        self.age += 1


# Student class - A class that will inherit the person class above
# class className(inherited_class): - inheritance syntax
class Student(Person):

    # Class constructor
    def __init__(self, first_name='Dhosio'):  # Constructor with a parameter with a default value
        # Class attributes
        super().__init__()
        self.f_name = first_name
        self.current_class = 'Year 1'
        self.grade = 'A'

    # Class methods
    def update_grade(self, new_grade):
        self.grade = new_grade

    # Method to concatenate details
    def details(self):
        return f'First name: {self.f_name} {self.l_name}. I am {self.age} years old. My grade is {self.grade}'


# Creating an object from a class
# Syntax: <variable_name> = <class_name>()
daniel = Person()  # Will create a person object
dhosio = Student('Dhosio')  # Will create a student object with a 'first_name' argument

# These methods can be called and used in other python files using the following syntax
# Eg: From classes import update_grade
# Check grade.py class
# Also check py_objects.py
