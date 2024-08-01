# The OS module in Python provides functions for interacting with the operating system

import os

# Get the current working directory
# print(os.getcwd())

# Change the current working directory
# print(os.chdir('/'))

# Create directory
# print(os.mkdir('Folders'))
# directory, mode = 'folder', 0o666
# path = os.path.join(rf"{os.getcwd()}\folders", directory)
# os.makedirs(path, mode)

# List all directories and files | Default None
# print(os.listdir('/'))

# Remove dirs and files
# print(os.remove(rf"{os.getcwd()}\Folders\folder\file.txt"))

# Remove dirs
# os.rmdir(rf"C:\Users\x\Downloads\python-training\Advanced-Python\Folders\folder")

# This function gives the name of the operating system dependent module imported.
# print(os.name)

# To rename a file
# file = os.rename('Folders\B.txt', 'Folders\A.txt')

# Check if a dir or file is exists
# print(os.path.exists('Folders\A.txt'))

# Get the size of bytes in a file
# print(os.path.getsize('Folders\A.txt'))