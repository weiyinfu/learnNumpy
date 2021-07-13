import numpy as np

a = np.random.randint(0, 10,10)
print(np.clip(a, 2, 6))
print(np.clip(2.5,2,6))