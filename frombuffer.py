import numpy as np

a = np.random.random((2, 3))
b = np.frombuffer(a.tobytes())
b = b.reshape(a.shape)
print(np.all(a == b))
