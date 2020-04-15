import numpy as np

a = 2 + np.arange(7)

print(a)

print("min: ", np.min(a))
print("max: ", np.max(a))
print("max - min:", np.max(a)-np.min(a))
print("a2 ", a[2])
print("a2 - min ", a[2] - a.min())
np.set_printoptions(precision=8)
print(2/6)

print((a[2] - a.min())/(a.max()-a.min()))

b = np.random.random(5)

print(b)

