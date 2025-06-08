#The key function for working with files in Python is the open() function.
#The open() function takes two parameters; filename, and mode.
# There are four different methods (modes) for opening a file:
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists

                                           
# In addition you can specify if the file should be handled as binary or text mode
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)

# To open a file for reading it is enough to specify the name of the file:
f = open("demofile.txt")

# The code above is the same as:
f = open("demofile.txt", "rt")

# Because "r" for read, and "t" for text are the default values, you do not need to specify them.

# The open() function returns a file object, which has a read() method for reading the content of the file:
f = open("demofile.txt")
print(f.read())

# If the file is located in a different location, you will have to specify the file path, like this:
f = open("D:\\myfiles\welcome.txt")
print(f.read())

# You can also use the with statement when opening a file:
with open("demofile.txt") as f:
  print(f.read())

# Then you do not have to worry about closing your files, the with statement takes care of that.
# It is a good practice to always close the file when you are done with it.














                                         
