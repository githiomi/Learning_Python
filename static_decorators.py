# Static variables or methods are used by all objects of that class and therefore have access to them,
# They are always defined at the top. After class definition but above the constructor

class Animal(object):
    # A parent class animal
    animals = []  # A list of Animal objects that can be accessed by all objects of the class

    # Constructor
    def __init__(self, animal_name):
        self.name = animal_name
        # To create a new Animal and add it to the list
        self.animals.append(self)

    # Class methods
    # To print method
    def __str__(self):
        return f'Animal name: {self.name}'

    # DECORATORS - Show special methods in a class
    # They are placed directly above a method definition - @classmethod, @staticmethod
    @classmethod
    # They are used to access and manipulate class methods and attributes
    # Syntax: def <method_name>(cls): - The cls here refers to the class itself
    def number_of_animals(cls):
        return len(cls.animals)

    @staticmethod
    # Syntax: def <method_name>(x): - Doesn't need to pass in the class (cls) and can have any parameters (x)
    # Static methods cannot make use of class variables and methods
    def eat(eat_num):
        # Eat a certain number of times a day
        for _ in eat_num:
            print('I am eating')


# Creating an animal object
animal_one = Animal('Animal One')

# To access static class attributes or methods
# Syntax: <class-name>.<attr_name>
print(Animal.animals)  # Will access the static class list attribute
# Will print out the string representation of the object
print(animal_one)

# Calling a class method - The number_of_animals() method
print(Animal.number_of_animals())  # No need to pass in arguments
