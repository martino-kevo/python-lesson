import os

try:
    with open('working_with_files/names.txt') as file:
        print(file.read())
        # print(f"{file.readline()}")
except FileNotFoundError:
    print("\nThe file you want to read doesn't exist.")

lines_to_write = ['ab\n', 'ba\n', 'qw\n', 'lo\n', 'gh']

# with open('working_with_files/kel.txt', "w") as file:
#     file.writelines(lines_to_write)

try:
    with open('working_with_files/kel.txt') as file:
        print(file.read())
except FileNotFoundError:
    print("\nThe file you want to read doesn't exist.")

if os.path.exists('working_with_files/kel.txt'):
    os.remove('working_with_files/kel.txt')
