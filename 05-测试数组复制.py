import numpy as np

"""
pandas的
"""


def test1():
    a = np.random.random(3)
    b = np.array(a)  # np.array会复制一份数据
    b[0] = 100
    print(a)


def test2():
    # 这个操作很危险，是一种不确定的行为
    a = np.random.random(7)
    b = a[::2]
    b[:] = 100
    print(a)


def test3():
    # 和test2一样，这个操作也是一个不确定行为
    a = np.random.random(7)
    a[::2] = 100
    print(a)


test2()
