# The array object in NumPy is called ndarray.

import numpy as np
arr = np.array((1,2,3,4,5))

print(arr)
print(type(arr))

# nested array: are arrays that have arrays as their elements.
# 0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.

arr = np.array(42)
print(arr)

# Một mảng mà có mảng 0-D là phần tử của mình thì được gọi là mảng 1 chiều hay mảng 1-D

arr = np.array([1,2,3,4,5])
print(arr)

# Một mảng mà có mảng 1-D là phần tử của mình thì được gọi là mảng 2-D array
# Chúng thường được dùng để đại diện cho ma trận

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)

# Một mảng mà có mảng 2-D(ma trận) là phần tử của mình thì được gọi là mảng 3-D

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr)

# Các mảng Numpy cung cấp thuộc tính NDIM trả về một số nguyên cho chúng ta biết có bao nhiêu kích thước mà mảng có.

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)