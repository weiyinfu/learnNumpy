import numpy as np
import matplotlib.pyplot as plt
# 基于R语言的语法创建数组，这句话会把所有的东西展平，它就是flatten多个数组
print(np.r_[1, 2, 3, (4, 5, 6), [8, 9, 10]])
a=[[1,2,3],[4,5,6],7,8,[[9,10]]]
print(np.r_[a])
a = np.array([1, 2, 3])
b = np.take(a, [1, 0])
print(b)

x = np.linspace(-np.pi, np.pi)
y = np.sin(x)

plt.step(x, y)
plt.plot(x, y, c='grey', alpha=0.5)
plt.show()
