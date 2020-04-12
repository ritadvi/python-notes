import numpy as np

# Arrays - Attributes

# Define a See for reproducibility
np.random.seed(0)

# Defie a three-dimensional array, with max values < 10
x3 = np.random.randint(10, size=(3, 4, 5))

# Number of Dimensions (3) - array.ndim
print("x3 ndim: ", x3.ndim) 

# Dimensions size (3, 4, 5) - array.shape
print("x3 shape:", x3.shape)

# Array size ( 3 x 4 x 5 = 60) - array.sixe
print("x3 size: ", x3.size)