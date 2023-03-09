# Context Managers will be used in shared memory and resources

# Normally, you open a file, write to it and then close it
file = open('files/context_file.txt', 'w')  # Opened in 'w' (write) mode which creates a new file
file.write("This is a line that will be added to the context_file file")
file.close()  # And then close the file

# A file must be closed and at times, if an error occurs during writing, then the 'close()' method will not be reached
# This can be resolved by:
closeable_file = open('files/context_file.txt', 'r')  # This has been opened in write mode
# To fix the closability issue, we can use the 'try, finally' syntax
try:
    closeable_file.write("This will be written to the file")
finally:
    closeable_file.close()

# But using a context manger, the 'try, finally' syntax can be replaced with:
with open('files/context_file.txt', 'r') as context_file:
    context_file.write("This will be written to the new file using a context manager")


# We can also make our own context manager
class File(object):
    def __init__(self, filename, method):
        self.file = open(filename, method)

    def __enter__(self):
        print("Entering")
        # This is the first method that will be fired
        return self.file

    def __exit__(self, type, value, traceback):
        print("Exiting")
        # This will be called when there is an error
        # But whatever is in this block will be run even if an error occurs.
        # Which makes it the best place to close a file
        self.file.close()
        # To ignore exceptions and tell the compiler that all is well, we can do so by:
        return True


# We can then use our newly created context manager as follows:
with File('files/context_file.txt', 'w') as modified_context:
    # We can then write to the file like normal
    modified_context.write("This will be written to the file using the new modified context file")

# We can also create context managers using generators
# Requires an import : contextlib
import contextlib as cntlib


@cntlib
def file_context_manager(filename, method):
    new_file = open(filename, method)
    # the yield keyword tells the program to pause
    yield new_file
    # You can then close the file
    new_file.close()
