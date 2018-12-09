import numpy as np

a = np.array([1, 2, 3])
print(type(a))
print("a.shape is {}".format(a.shape))
print(a[0], a[1], a[2])
a[0]=5
print(a)

b = np.array([[1,2,3],[4,5,6]])
print("b is {}".format(b))
print("b.shape is {}".format(b.shape))
print(b[0, 0], b[0, 1], b[1, 0])

a = np.zeros((2,2))
print("np.zeros((2,2)) is {}".format(a))

b = np.ones((1,2))
print("np.ones((1,2)) is {}".format(b))

c = np.full((2,2), 7)
print("np.full((2,2), 7) is {}".format(c))

d = np.eye(2)
print("np.eye(2) is {}".format(d))

e = np.random.random((2,2))
print("np.random.random((2,2)) is {}".format(e))

a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print(a)

b = a[:2, 1:3]
print("b = a[:2, 1:3] is {}".format(b))
print(a[0, 1])
b[0, 0] = 77
print("change b[0, 0] = 77 will affect a[0, 1] = {}".format(a[0, 1]))

a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
row_r1 = a[1, :]
row_r2 = a[1:2, :]
print("row_r1 = a[1, :] is {0} {1}".format(row_r1, row_r1.shape))
print("row_r2 = a[1:2, :] is {0} {1}".format(row_r2, row_r2.shape))

col_r1 = a[:, 1]
col_r2 = a[:, 1:2]
print("col_r1 = a[:, 1] = {0} {1}".format(col_r1, col_r1.shape))
print("col_r2 = a[:, 1:2] = {0} {1}".format(col_r2, col_r2.shape))

a = np.array([[1,2], [3, 4], [5, 6]])
print(a)
print("a[[0, 1, 2], [0, 1, 0] is {}".format(a[[0, 1, 2], [0, 1, 0]]))
print("np.array([a[0, 0], a[1, 1], a[2, 0]]) is {}".format(np.array([a[0, 0], a[1, 1], a[2, 0]])))
print("a[[0, 0], [1, 1]] is {}".format(a[[0, 0], [1, 1]]))
print("np.array([a[0, 1], a[0, 1]]) is same as above {}".format(np.array([a[0, 1], a[0, 1]])))

a = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
print("a is {}".format(a))
b = np.array([0, 2, 0, 1])
print("b is {}".format(b))
print("a[np.arange(4), b] is {}".format(a[np.arange(4), b]))

a[np.arange(4), b] += 10
print("a[np.arange(4), b] += 10 is {}".format(a))

a = np.array([[1,2], [3, 4], [5, 6]])

bool_idx = (a > 2)
print(bool_idx)
print("a[bool_idx] is {}".format(a[bool_idx]))
print(a[a > 2])

print("#" * 10 + " dtype "+"#" * 10)
x = np.array([1, 2])
print(x.dtype)

x = np.array([1.0, 2.0])
print(x.dtype)

x = np.array([1, 2], dtype=np.int64)
print(x.dtype)

print("#" * 10 + " +-*/sqrt "+"#" * 10)

x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)

print(x + y)
print(np.add(x, y))

print(x - y)
print(np.subtract(x, y))

print(x * y)
print(np.multiply(x, y))

print(x / y)
print(np.divide(x, y))

print(np.sqrt(x))

x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])

v = np.array([9,  10])
w = np.array([11, 12])

print("#" * 10 + " dot "+"#" * 10)

print(v.dot(w))
print(np.dot(v, w))

print(x.dot(v))
print(np.dot(x, v))

print(x.dot(y))
print(np.dot(x, y))

print("#" * 10 + " sum "+"#" * 10)

x = np.array([[1,2],[3,4]])
print(np.sum(x))
print(np.sum(x, axis=0))  # Compute sum of each column; prints "[4 6]"
print(np.sum(x, axis=1))  # Compute sum of each row; prints "[3 7]"

print("#" * 10 + " T "+"#" * 10)

x = np.array([[1,2], [3,4]])
print(x)
print(x.T)

v = np.array([1,2,3])
print(v)
print(v.T)

print("#" * 10 + " empty_like "+"#" * 10)

x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
y = np.empty_like(x) # Create an empty matrix with the same shape as x

for i in range(4):
    y[i, :] = x[i, :] + v
print(y)

print("#" * 10 + " tile "+"#" * 10)

vv = np.tile(v, (4, 1))   # Stack 4 copies of v on top of each other
print(vv)
y = x + vv  # Add x and vv elementwise
print(y)

y = x + v
print(y)

print("#" * 10 + " reshape "+"#" * 10)

v = np.array([1,2,3])
w = np.array([4,5])
print("np.reshape(v, (3, 1)) is {}".format(np.reshape(v, (3, 1))))
print(np.reshape(v, (3, 1)) * w)

x = np.array([[1,2,3], [4,5,6]])
print("x + v is {}".format(x + v))
print("(x.T + w).T is {}".format((x.T + w).T))

print(x)
print("np.reshape(w, (2, 1)) is {}".format(np.reshape(w, (2, 1))))
print("x + np.reshape(w, (2, 1)) is {}".format(x + np.reshape(w, (2, 1))))
print(x * 2)

print("#" * 10 + " change image resolution "+"#" * 10)

from scipy.misc import imread, imsave, imresize

# Read an JPEG image into a numpy array
img = imread('cat.jpg')
print(img.dtype, img.shape)  # Prints "uint8 (400, 248, 3)"

# We can tint the image by scaling each of the color channels
# by a different scalar constant. The image has shape (400, 248, 3);
# we multiply it by the array [1, 0.95, 0.9] of shape (3,);
# numpy broadcasting means that this leaves the red channel unchanged,
# and multiplies the green and blue channels by 0.95 and 0.9
# respectively.
img_tinted = img * [1, 0.95, 0.9]

# Resize the tinted image to be 300 by 300 pixels.
img_tinted = imresize(img_tinted, (300, 300))

# Write the tinted image back to disk
imsave('cat_tinted.jpg', img_tinted)

print("#" * 10 + " matlab "+"#" * 10)

from scipy.spatial.distance import pdist, squareform
x = np.array([[0, 1], [1, 0], [2, 0]])
print(x)
print(pdist(x, 'euclidean'))
d = squareform(pdist(x, 'euclidean'))
print(d)

print("#" * 10 + " run matplot use frameworkpython!! "+"#" * 10)

import matplotlib.pyplot as plt

x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.plot(x, y_sin)
plt.plot(x, y_cos)
plt.xlabel('x axis label')
plt.ylabel('y axis label')
plt.title('Sine and Cosine')
plt.legend(['Sine', 'Cosine'])
plt.show()

plt.subplot(2, 1, 1)
plt.plot(x, y_sin)
plt.title('Sine')

plt.subplot(2, 1, 2)
plt.plot(x, y_cos)
plt.title('Cosine')

plt.show()

img = imread('cat.jpg')
img_tinted = img * [1, 0.95, 0.9]
plt.subplot(1, 2, 1)
plt.imshow(img)

plt.subplot(1, 2, 2)
plt.imshow(np.uint8(img_tinted))
plt.show()