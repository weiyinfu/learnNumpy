import numpy as np
from PIL import Image
from matplotlib import pyplot as plt


# get the dft_matrix
def dft_matrix(N):
    i, j = np.meshgrid(np.arange(N), np.arange(N))
    omega = np.exp(-2j * np.pi / N)
    w = np.power(omega, i * j)
    return w


def dft2d(image):
    h, w = image.shape
    output = dft_matrix(h).dot(image).dot(dft_matrix(w))
    return output


img = Image.open("haha.jpg").convert("L")
img_data = np.array(img)
plt.imshow(img_data,cmap='Greys_r')
plt.show()
x = dft2d(img_data)
print(x)
