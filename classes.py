# Classes work as the blueprint for creating objects
# They have attributes, constructors and methods

# Class Example - A class called person (will be inherited by student class)
class Person:

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
    def __init__(self):
        # Class attributes
        super().__init__()
        self.current_class = 'Year 1'
        self.grade = 'A'

    # Class methods
    def update_grade(self, new_grade):
        self.grade = new_grade


# These methods can be called and used in other python files using the following syntax
# Eg: From classes import update_grade
# Check grade.py class
# Also check py_objects.py
