# This class will be used to implement codes and methods from the person and student classes
# To import the classes module
import classes as cs

# Call the method from the Person class to increase the person age then print
# Create a student object
# student = cs.Student()  # When empty, it will use the default value in the constructor parameters
student = cs.Student('Daniel')

# Print out student details
print(student.details())

# Manipulate the student object
# This will go to classes and call the update_grade() method
print(f'Grade before update: {student.grade}')
student.update_grade('D')  # This will change the student grade
print(f'Grade after update: {student.grade}')
