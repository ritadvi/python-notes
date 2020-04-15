import numpy as np

# Arrays - Manipulation

x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


# Acess a slice of an array  x[start:stop:step] (stop not included)
# [0 2 4]
x[0:6:2]

# first x (5) elements
# in a multidmensional array x[:2, :3] - first 2 rows and first 3 columns
x[:5]


# Elements from index five (inclusive) to end
x[5:]

# Elements from index 4 (inclusive) to 6 (not inclusive)
x[4:6]

# Every other element
# [0, 2, 4, 6, 8]
# in a multidemensional array x2[:3, ::2] first 3 rows, every other column
x[::2] 

# Every other element backwards
# [10, 8, 6, , 4, 2, 0]
(x[::-2]

# Reverse an array, every element from last to first
x[::-1]

# Single row in a multidemnsional array x[0,:] equivalent to x[0]
x[0,:]

# Single column in a multidimensional array
x[:,0]

# Copying arrays - if Copy is not scepecified and a new array is created based on an existing one, 
# the two arrays will be forever linked (as Views)
# changes in a first array will affect also the second and vice versa
# use copy to avoid this


# Create a new array based on a view
x2_sub = x2[:2, :2]

# Copy
x2_sub_copy = x2[:2, :2].copy()

# Concatenation of arrays
# For one dimensional concatenates in the same one dimension, 
# for multiple dimensions adds it keeping the different dimensions
# [1, 2, 3, 3, 2, 1]

x = np.array([1, 2, 3]) 
y = np.array([3, 2, 1])
np.concatenate([x, y])



# Concatenation - Vertical stack 
# (add all arrays at the column ends - attempts to keep same number of rows)

x = np.array([1, 2, 3]) 
grid = np.array([[9, 8, 7],
                 [6, 5, 4]])
np.vstack([x, grid])

# [[1, 2, 3],
#  [9, 8, 7],
#  [6, 5, 4]]

# Concatenation - Horizontal stack 
# (add all arrays at the row end - attempts to keep same number of columns)
y = np.array([[99]
    [99]]
    ) 
np.hstack([grid, y])

#[[ 9,  8,  7, 99],
# [ 6,  5,  4, 99]]

# Split - For each method we can pass a list of indices to give the initial split points
# N split points lead to N + 1 subarrays

x = [1, 2, 3, 99, 99, 3, 2, 1] 
# one array from [0-3[, other from [3,5[ and last from [5:] 
# [1 2 3] [99 99] [3 2 1]
x1, x2, x3 = np.split(x, [3, 5])

# Horizontal Split - splits horizontally at a column index
grid = array([[ 0,  1,  2,  3],
               [ 4,  5,  6,  7],
               [ 8,  9, 10, 11],
               [12, 13, 14, 15]])

# upper with rows [0,2[, lower with rows [2,:]
upper, lower = np.vsplit(grid, [2])

# Vertical Split - splits vertically at a row index
# left with columns [0,2[, right with columns [2,:]
left, right = np.hsplit(grid, [2])

# Sort the array or X.sort()
np.sort(X) 

# Returns the indexes that would sort the array
np.argsort(X)

 # sort each column of X 
 np.sort(X, axis=0)

 # sort each row of X 
 np.sort(X, axis=1)



