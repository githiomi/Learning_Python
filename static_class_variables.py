# This is an example to show classes that have class variables within them
# Class variables are those that belong to the class and not instances (Objects)

class Person(object):
    # Create a class called person

    # This is a class variable that can be accessed by all object instances
    persons = []  # A list called persons that will hold the person objects

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.persons.append(self)  # A method to add each object create to the persons list

    @classmethod
    # This is a class method with the decorator that can perform action on the class as a whole and not just an
    # object instance
    def num_of_persons(cls):  # Pass in 'cls' which refers to the class itself
        return len(cls.persons)  # Will return the number of objects in the persons list

    # Override the print method of the class
    def __str__(self):
        return f'My name is {self.name} and I am {self.age} years old!'


# Class variables can be called without having to create any instance of the class
# Create a few people and store them in the persons list
daniel = Person('Daniel', 21)
dhosio = Person('Dhosio', 20)
githiomi = Person('Githiomi', 19)

# To access the persons in the list
print(Person.persons[0])
