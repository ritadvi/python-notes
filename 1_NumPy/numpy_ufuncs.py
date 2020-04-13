import numpy as np


# Computation on NumPy arrays can be very fast, or it can be very slow. 
# The key to making it fast is to use vectorized operations, 
# generally implemented through NumPy universal functions (ufuncs). 

# to do a vectorized operation, simply performing an operation on the array, 
# which will then be applied to each element (one by one).

# Computations using vectorization through ufuncs are nearly always more efficient than 
# their counterpart implemented through Python loops, especially as the arrays grow in size. 
# Any time you see such a loop in a Python script, 
# you should consider whether it can be replaced with a vectorized expression.


# Reduce - repeatedly applies a given operation to the elements of an array until only a single result remains.
# calling reduce on the add ufunc returns the sum of all elements in the array:

x = np.arange(1, 6) 
# Sum all values (equal to np.sum(x))
# out = 15
np.add.reduce(x)
# Multiply all values
np.multiply.reduce(x)

# To store all intermediate values (like a running sum) use Accumulate
# [ 1, 3, 6, 10, 15]
np.add.accumulate(x)

# Whenever possible, make sure that you are using the NumPy version of aggregates 
# when operating on NumPy arrays 
np.max(x) 
np.min(x) 
np.sum(x)

# find the minimum value within each column by specifying axis=0:
array.min(axis=0)

# find the maximum value within each row by specifying axis=1:
array.min(axis=1)

# most aggregates have a NaN-safe counterpart that computes 
# the result while ignoring missing values

# np.sum  / np.nansum 
#np.prod / np.nanprod

# BOOLEAN Arrays

# Count number of True entries in a Boolean array

 # how many values less than 6?
np.count_nonzero(x < 6)

# False is interpreted as 0, and True is inter‐ preted as 1:
np.sum(x < 6)

# how many values less than 6 in each row? 
np.sum(x < 6, axis=1)

 #Any values greater than 8? 
 np.any(x > 8)

 # are all values less than 10? 
 np.all(x < 10)

 # are all values in each row less than 8? 
np.all(x < 8, axis=1)

 # count values between an interval
np.sum((x > 0.5) & (x < 1))

# Masking operations

# select values from an array based on a condition
# extract values from x where x < 5
x[x < 5]

# a mask can be set and reused

# construct a mask of all rainy days 
rainy = (inches > 0)

# median for all days in inches where inches > 0
np.median(inches[rainy])
