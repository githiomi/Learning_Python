# Classes work as the blueprint for creating objects
# They have attributes, constructors and methods
# Math import to get the square root function
import math as mth


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
        return f'Full name: {self.f_name} {self.l_name}. I am {self.age} years old. My grade is {self.grade}'


# Creating an object from a class
# Syntax: <variable_name> = <class_name>()
daniel = Person()  # Will create a person object
dhosio = Student('Dhosio')  # Will create a student object with a 'first_name' argument

print(dhosio.details())
dhosio.birthday()  # To increase the age of the student by one
dhosio.update_grade("A+")  # To update the rade of the user to the new input
print(dhosio.details())


# These methods can be called and used in other python files using the following syntax
# Eg: From classes import update_grade
# Check grade.py class
# Also check py_objects.py


# DEFAULT PYTHON CLASS METHODS
# Use a class called points
class Point(object):

    # Class constructor
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.coordinates = (self.x, self.y)

    # Method to move the point
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    # INBUILT METHODS TO FOR OBJECTS - So that we don't have to access each object's attributes
    # They will override the inbuilt class methods
    # To add object instances
    def __add__(self, other_object):  # Syntax: def __add__(self, <other-object-instance>)
        # Create a new point object and return it
        return Point(self.x + other_object.x, self.y + other_object.y)

    # Subtract
    def __sub__(self, other_object):
        return Point(self.x - other_object.x, self.y - other_object.y)

    # Multiply
    def __mul__(self, other_object):
        # Will not create a new point object because multiplication returns a scalar value
        return self.x - other_object.x, self.y - other_object.y

    # When trying to convert an object to a string readable format
    # This is similar to a toString() function in JAVA
    def __str__(self):
        # Format the return string to display any content from the object
        return f'Coordinates: ({str(self.x)}, {str(self.y)})'

    # To override the len() method
    def __len__(self):
        squared_sum = self.x ** 2 + self.y ** 2
        return mth.sqrt(squared_sum)

    # Length method to get the magnitude of a point from the origin
    # Magnitude is gotten by getting the square root of the sum of the square of the point
    def length(self):
        squared_sum = self.x ** 2 + self.y ** 2
        return mth.sqrt(squared_sum)

    # INBUILT COMPARATOR METHODS - To compare object instances of the class
    # These methods return a boolean value
    # Check the length() method created above
    # Greater than
    def __gt__(self, other_object):
        # Can use either length() or __len__() because we have overridden the default __len__() method
        return self.__len__() > other_object.length()

    # Greater than or equal to
    def __ge__(self, other_object):
        return self.length() >= other_object.__len__()

    # Less than
    def __lt__(self, other_object):
        # Alternative syntax of __len__() is len()
        return len(self) < other_object.length()

    # Less than or equal to
    def __le__(self, other_object):
        return self.length() <= other_object.length()

    # Check equality
    def __eq__(self, other_object):
        # We check this manually as Python is known to have errors with float values
        return self.x == other_object.x and self.y == other_object.y


# Creating points
point_1 = Point(1, 5)
point_2 = Point(2, 4)
point_3 = Point(3, 6)

# Test the code
print(point_1 == point_2)  # Uses the __eq__ function
print(point_2 > point_3)  # Uses the __gt__ function
print(point_1 <= point_3)  # Uses the __le__ function
