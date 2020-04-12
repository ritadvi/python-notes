# Import numpy
import numpy as np

# ARRAYS  - Initialize
# unlike Python lists, NumPy is constrained to arrays that all contain the same type
# unlike Python lists, NumPy arrays can explicitly be multidimensional

# Integer Array
np.array([1, 4, 2, 5, 3])

# Float Array - If types do not match, NumPy will upcast if possible (here, integers are upcast to floating point)
np.array([3.14, 4, 2, 3])

# Array - Explicitly set the data type
np.array([1, 2, 3, 4], dtype='float32')

# Initialize a multidimensional array
# nested lists result in multidimensional arrays 
# [[2 3 4]
#  [4 5 6]
#  [6 7 8]]
np.array([range(i, i + 3) for i in [2, 4, 6]])

# Create Arrays from scratch

# Create a length-10 integer array filled with zeros 
# [0 0 0 0 0 0 0 0 0 0 0]
np.zeros(10, dtype=int)

# Create a 3x5 floating-point array filled with 1s 
#[ [1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.] ] 
np.ones((3, 5), dtype=float)

# Create a 3x5 array filled with a specific value
#[ [3.14 3.14 3.14 3.14 3.14]
#  [3.14 3.14 3.14 3.14 3.14]
#  [3.14 3.14 3.14 3.14 3.14] ] 
np.full((3, 5), 3.14)

# Create a range array with a start (0), non included end (20) and stepsize (2)
# (similar to the built-in range() function) 
# [ 0,  2,  4,  6,  8, 10, 12, 14, 16, 18]
np.arange(0, 20, 2)

# Create an array of an amount of values (5) evenly spaced between start (0) and included end (1)
# [ 0. , 0.25, 0.5 , 0.75, 1. ]
np.linspace(0, 1, 5)

# Create a 3x3 random array of uniformly distributed # random values between 0 and 1
# [[ 0.99844933, 0.52183819, 0.22421193], 
#  [ 0.08007488, 0.45429293, 0.20941444],
#  [ 0.14360941, 0.96910973, 0.946117 ]]
np.random.random((3, 3))

# Create a 3x3 array of random integers in the interval [0, 10[ - start included, end not incuded
# if end is not mentioned, start is used as the highest limit (not included)
# [ [2, 1, 5],
#   [5, 4, 7],
#   [0, 5, 0] ]
np.random.randint(0, 10, (3, 3))