import os

# r - Read
# a - Append
# w - Write
# x - Create

# Read - error if file doesn't exists

file = open("working_with_files/names.txt")
# print(file.read())
# print(file.read(4))

# print(file.readline())
# print(file.readline())

# print(file.readlines())

# for each_line in file:
#     print(each_line)

# file.close()

try:
    file = open("working_with_files/names.txt")
    print(file.read())
except FileNotFoundError:
    print("The file you want to read doesn't exist")
finally:
    file.close()

# Append - adds to the end of the file and creates the file if it doesn't exist

file = open("working_with_files/names.txt", "a")
file.write("Neil\n")
file.close()

file = open("working_with_files/names.txt")
print(file.read())
file.close()

# Write - overwrites the file

file = open("working_with_files/context.txt", "w")
file.write("I deleted all of the context")
file.close()

file = open("working_with_files/context.txt")
print(file.read())
file.close()

# Two ways to create a new file

# Opens a file for writing, creates the file if it doesn't exist
file = open("working_with_files/name_list.txt", "w")
file.close()

# Creates a specified file, but returns an error if file exists
if not os.path.exists("working_with_files/dave.txt"):
    file = open("working_with_files/dave.txt", "x")
    file.close()

# Delete a file

# avoid an error if the file doesn't exist
if os.path.exists("working_with_files/dave.txt"):
    os.remove("working_with_files/dave.txt")
else:
    print("The file you wish to delete doesn't exist")


# Using the "with" keyword
with open("working_with_files/more_names.txt") as file:
    content = file.read()

with open("working_with_files/names.txt", "w") as file:
    file.write(content)
