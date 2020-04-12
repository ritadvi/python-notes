import numpy as numpy
import pandas as pd

# Read csv
data = pd.read_csv('data/president_heights.csv') 


heights = np.array(data['height(cm)']) 

print("Mean height: ", heights.mean()) 
print("Standard deviation: ", heights.std())
print("Minimum height: ", heights.min())
print("Maximum height: ", heights.max())
