import numpy as np
from numpy import fft


def biginteger_mul(a: str, b: str) -> str:
    a = np.array([int(i) for i in a])
    b = np.array([int(i) for i in b])
    # 首先对齐
    sz = len(a) + len(b)
    a = np.pad(a, (sz - len(a), 0))[::-1]
    b = np.pad(b, (sz - len(b), 0))[::-1]
    aa = fft.fft(a)
    bb = fft.fft(b)
    cc = aa * bb
    c = fft.ifft(cc)
    d = []
    left = 0
    for i in range(len(c)):
        now = int(np.round(c[i].real + left))
        d.append(now % 10)
        left = now // 10
    if left:
        d.append(left)
    return ''.join(str(i) for i in d)[::-1].lstrip('0')


def test(a: str, b: str):
    mine = biginteger_mul(a, b)
    ans = str(int(a) * int(b))
    if mine != ans:
        print(f"found badcase a={a} b={b}", mine, ans)
        return False
    return True


def big_test():
    cas_list = np.random.randint(1, 1000, (1234, 2))
    for a, b in cas_list:
        if not test(str(a), str(b)):
            break
    print("全部通过")


# big_test()
print(test("6546464645411451465465341234415664646", "56461312123412341234123412156"))
