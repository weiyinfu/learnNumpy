import numpy as np


def corrcoeff(a, b):
    aa = np.array(a) - np.mean(a)
    bb = np.array(b) - np.mean(b)
    return np.dot(aa, bb) / (np.linalg.norm(aa) * np.linalg.norm(bb))


def median_corrcoeff(a, b):
    aa = np.array(a) - np.median(a)
    bb = np.array(b) - np.median(b)
    return np.dot(aa, bb) / (np.linalg.norm(aa) * np.linalg.norm(bb))


def test():
    a = [1, 2, 3]
    b = [4, 5, 8]
    print(corrcoeff(a, b), np.corrcoef(a, b)[0, 1], median_corrcoeff(a, b))


test()
