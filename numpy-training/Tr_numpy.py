# import numpy as np
# from numpy import random

# arr = np.array([[[True, False], [1E2, -2E3], ["X", "Y"]], [['A', 'B'], [2, 3], [1, 3]], [['M', 'J'], [2, 3], [1, 3]]])

# To get the number of dimensions by ndim
# num_of_dimensions = arr.ndim

# Indexes
# ----------------------------------------
# get_x = arr[0][-1][0]
# get_2 = arr[1, 1, 0]

# Slicing [start:end:step]
# ----------------------------------------
# print(arr[::2])

# Data Types in NumPy
# ----------------------------------------
# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type ( void )

# arr_1 = np.array([1, 2], dtype='i') # or int
# arr_2 = np.array(['A', 'B'], dtype='str') # or S
# arr_3 = np.array([True, False], dtype='bool') # bool
# arr_4 = np.array([{'x': 1}]) # Object
# arr_5 = np.array([2.5j]) # complex128
# print(arr_1.dtype())

# arr = np.array([1.2, 2.4], dtype='f')
# Create a new arr and change the DT to Int
# new_arr = arr.astype('i')
# new_arr = arr.astype(int)
# print(new_arr)


# Copy in Numpy [ # Not affected ]
# ----------------------------------------
# arr = np.array([1, 2, 4], dtype='int')
# cp_arr = arr.copy() # Not affected in the both
# arr[0] = 100
# cp_arr[0] = 200


# View in Numpy [ # affected ]
# ----------------------------------------
# arr = np.array([1, 2, 4], dtype='int')
# view_arr = arr.view() # Affected in the both
# arr[0] = 100
# view_arr[0] = 200


# Shape in Numpy (  Dimensions, Length  )
# ----------------------------------------
# arr = np.array([ ['J', 1], [ 'X', 'Y'], [2, False] ])
# get_shape = arr.shape # (3, 2)


# Create an arr with 10 Dimensions 
# new_arr = np.array([1, 2, 3], ndmin=10)


# Reshape convert an arr to specified dimensions [ Elements must be equal in both shapes ]
# ----------------------------------------
# arr = np.array([1, 2, 3, 4, 5, 6])
# new_arr = arr.reshape(2, 3, -1)
# one_dim = new_arr.reshape(-1)


# BY using flatten we can flatten a matrix to one dimension in python.
# ----------------------------------------
# arr = np.array([1, 2, 3])
# one_dim = arr.flatten(order='A')


# NumPy Array Iterating
# ----------------------------------------
# for x in arr:
#     for x in x:
#         print(x)

# iterates on every elements and convert them to string
# The flags=['buffered'] ensures the iteration can handle different data types.
# for i in np.nditer(arr[::2], flags=['buffered'], op_dtypes=['S']): print(i)


# BY using ndenumerate you can get the index and elem
# for index, elem in np.ndenumerate(arr):
#     print(index, elem)


# Numpy Joins
# ----------------------------------------
# Axis 0 is vertical (down). Like: 1, 4, 7
# [[1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]]


# Axis 1 (across the columns): Like 1, 2, 3
# -> [[1, 2, 3], 
# ->  [4, 5, 6],
# ->  [7, 8, 9]]


# Numpy concatenate and stack
# ----------------------------------------
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# arr_conc = np.concatenate((arr1, arr2)) # should be equal in shapes and dimensions
# arr_stack = np.stack((arr1, arr2), axis=1)


# hstack | used to stack arrays in sequence horizontally
# ----------------------------------------
# arr_hstack = np.hstack((arr1, arr2))


# vstack | used to stack arrays in sequence vertically 
# ----------------------------------------
# arr_vstack = np.vstack((arr1, arr2))
# arr_dstack = np.dstack((arr1, arr2))


# NumPy Splitting and Searching 
# ----------------------------------------
# arr = np.array([11, 22, 33, 44, 55, 65, 77, 88, 99, 100], dtype='int')
# # arr_split = np.array_split(arr, 1, axis=0)

# arr_where = np.where(arr%2 != 0) # get the  odd numbers 
# arr_where = np.where(arr >= 88)

# arr = np.array([1, 3, 6, 8])
# Add the input to sorted output
# where_should_i_put_2_and_4 = np.searchsorted(arr, [2, 4], side='right') # Side means start by search by right


# Numpy Sort
# ----------------------------------------
# arr1 = np.array([[1, 3, 4, 2], [1, 3, 4, 2]])
# arr2 = np.array(['B', 'C', 'D', 'A'])
# arr_sort1 = np.sort(arr1, axis=1) # New arr
# arr_sort2 = np.sort(arr2) # New arr


# Numpy Filter
# ----------------------------------------
# arr = np.array([41, 142, 143, 44, 100])
# get_true = [False, True, True, False, True] # Return only index true
# new_arr = arr[get_true]

# filtered_arr = []

# for i in arr:
#     if i >= 100 and i % 2 == 0: filtered_arr.append(True)
#     else: filtered_arr.append(False)

# new_arr1 = arr[filtered_arr]

# get_even = arr % 2 == 0 # Directly


# Numpy random
# ----------------------------------------
# arr = np.array(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
# print(random.randint(10)) # Generate a random int from 0 to 10
# print(random.randint(100, size=(3, 10))) # Generate a random int from 0 to 100 with specified shapes and dimensions
# print(random.rand()) # Generate a random float from 0 to 1
# print(random.rand(3, 3)) # Generate a random float from 0 to 1 with specified shapes shapes and dimensions
# print(random.choice([1, 100, -1])) # Get random choice from an arr
# print(random.choice(arr, size=(3, 2))) # Get random choice from an arr with specified shapes shapes and dimensions


# Numpy Random Data Distribution
# ----------------------------------------
# The probabilities in numpy.choice beginning with 0 and ending 1 and must The sum of all probability numbers should be 1.
# [0.0, 0.0, 0.6, 0.4]
# the First  one, second there is no choice to take it
# x = random.choice([3, 5, 7, 9], p=[0.1, 0.2, 0.2, 0.5], size=(3, 10))


# Numpy Permutations
# ----------------------------------------
# arr = np.array([1, 2, 3, 4, 5])
# random.shuffle(arr) # shuffle the main arr (changes to the original array)
# new_arr = random.permutation(arr) # ( DONT NOT changes to the original array)


# 
# ----------------------------------------

