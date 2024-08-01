# The python sys module has functions and variables to manipulate the python runtime Environment
import sys

# Get the version of Python Interpreter and some additional information
# print(sys.version)

# stdin is used to get an input from the cmd and print it as output
# for i in sys.stdin:
#     if i.lower().strip() == 'q': break
#     print(f'output is {i}')

# Print to the console
# sys.stdout.write(f"{1e6}")


# exits the program 
# if 10 > 9: sys.exit('10 is less than 9')
# else: print('Acceptable')

# Print a dictionary of all the modules that have been imported by the current Python interpreter
# print(sys.modules)


# Get the reference count of a given object
# print(sys.getrefcount(87984))

