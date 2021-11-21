import numpy as np

a = np.random.lognormal(0, 1, (1000,))
import matplotlib.pyplot as plt

plt.hist(a, bins=200)
plt.show()