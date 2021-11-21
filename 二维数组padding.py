import numpy as np

a = np.ones((3, 3, 1))
b = np.pad(a, [(2, 2), (2, 2), (0, 0)])
print(b.shape)
