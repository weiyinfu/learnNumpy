import numpy as np

primary_key = (1, 1, 2, 2, 3, 3)
second_key = (2, 3, 1, 3, 4, 6)
ind = np.lexsort((second_key, primary_key))  # 注意此处的顺序
a = np.array(list(zip(primary_key, second_key)))
print(a[ind])
