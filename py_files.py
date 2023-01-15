# Files are the external storage locations for data
# Types of file in python - Binary & Text

# Must first import the OS module
import os

# The os module has a number of functions such as:
# 1. Check if a file exists
#   if os.path.exists("<file_directory>")

# 2. Removing a file
#   os.remove("<file_directory>")

# 3. Deleting a folder
#   os.rmdir("<folder_directory>")

# File handling - Operation that can be performed on files
# The operations are: CRUD - Create\Read\Update\Delete

# Modes - "r" - read (default), "w" - write, "a" - append, "x" - create
# You can add "t" or "b" to specify the file type. Eg: file = open("my_file.txt", "rt")

# Working with files in python -
# 1. Create File - still uses the open() method
# Cannot create a file with the same name
new_file_dir = "files/new_file.txt"

# Check if file exists
if os.path.exists(new_file_dir):
    print("Path already exists")
else:
    new_file = open(new_file_dir, "x")
    new_file.write("This is a new file")
    new_file.close()

# 2. Open file
# Syntax -> open(<file_name>, <mode>)
file_dir = "files/my_file.txt"

# 3. Work on the file - Read/Write/Update/Delete

# Reading Function
# Reading Characters syntax - use the read() function
file = open(file_dir, "r")
print(f'Read all --- {file.read()}')
file.close()

# To add character limit
my_file = open("files/my_file.txt", "r")
print(f'Read 5 Characters --- {my_file.read(5)}')  # Will read the fist 5 characters of the file
my_file.close()

# Reading lines
# <file_name>.readline() - Will read the file and give line by line output
# <file_name>.readline(x) - Will read the line with the specified int (x)
# <file_name>.readlines() - Will read the file lines separately

# Reading a full file using a loop
file = open(file_dir, "r")
counter = 1
for each_line in file:
    print(f'Line {counter} -> {each_line}')
    counter += 1
file.close()

# Writing function - Can either be appended (add content to a file) or write (will overwrite content)
# Syntax - <file_name>.write()
file_two = open(file_dir, "w")
file_two.write("Hello world!")
file_two.close()

# 4. Close the file
# Syntax -> <file_name>.close()
file.close()

# Deleting a file
# To delete the file
print(f'Deleting file ---- {file_dir}')
os.remove(file_dir)
