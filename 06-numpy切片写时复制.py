import numpy as np

n = 10
a = np.random.random(n)
b = np.zeros(n, dtype=np.bool)
happen = b[a < 0.9]
happen[0] = True  # 此处执行写操作之后会发生写时复制
print(b)
b[a < 0.9] = True
print(b)
