import numpy as np

"""
int与float数值范围相当，但是float无法精确表达全部int的范围
"""
a = [1599396360, 1599396390]
b = [999934223.9234, 0.9999345]
a = np.array(a, dtype=np.float32)
b = np.array(b, dtype=np.float32)
print(a.astype(np.int32), b.astype(np.float))
