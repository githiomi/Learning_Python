# Objects are items created from class blueprints that can be used in the real world program

# To create objects we need classes (These can be from other modules)
# Eg: creating student objects from the 'classes' module
# Start by importing the module
import classes as cs

# Create a student object
# Syntax: <variable_name> = <module_name>.<class_name>()
student = cs.Student('Student One')  # Create a student object with a name argument into the constructor


# Print out the student details
print(student.details())

# Manipulate the student object
print(f'Grade before update: {student.grade}')
student.update_grade('D')  # This will change the student grade
print(f'Grade after update: {student.grade}')
