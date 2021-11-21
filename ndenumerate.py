import numpy as np

a = np.random.random((2, 2, 3))

for index, value in np.ndenumerate(a):
    print(index, value, type(index), type(value))
