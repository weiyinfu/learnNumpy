from typing import List

import numpy as np


def broadcast(a: List[int], b: List[int]):
    if len(a) < len(b):
        a, b = b, a
    # 较短的数组左边补一
    b = [1] * (len(a) - len(b)) + b
    c = np.max(a, b, axis=0)
    # 检查是否合理
    for i in range(len(c)):
        if c[i] % a[i] != 0 or c[i] % b[i] != 0:
            raise Exception("无法广播")
    return c  # 最终结果的形状
