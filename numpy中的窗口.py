import matplotlib.pyplot as plt
import numpy as np

"""
这些窗口都是0~1之间的值
"""
for window in (np.hanning, np.hamming, np.bartlett, np.blackman):
    w = window(30)
    plt.plot(w, label=window.__name__)
plt.legend()
plt.show()
