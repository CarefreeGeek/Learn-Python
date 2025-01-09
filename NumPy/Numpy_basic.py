import numpy as np

# x = np.array([1, 2, 3, 4, 5])
# print(x)


# creating an array in numpy

# arr = np.array([1, 2, 3, 4, 5])
# print(arr)
# print(type(arr))

# <--- output --->
# [1 2 3 4 5]
# <class 'numpy.ndarray'>


# creating an array in numpy using tuple

# arr = np.array((1, 2, 3, 4, 5))
# print(arr)

# <--- output --->
# [1 2 3 4 5]


# Create a 0-D array with value 42

# arr = np.array(42)
# print(arr)

# Create a 2-D array containing two arrays with the values 1,2,3 and 4,5,6:

# arr = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr)
# <--- output --->

# Create a 3-D array with two 2-D arrays, both containing two arrays with the values 1,2,3 and 4,5,6:

# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         for k in range(len(arr[i][j])):
#             print(arr[i][j][k], end=" ")
#         print()
#     print()

# <--- output --->
# 1 2 3 
# 4 5 6 

# 1 2 3
# 4 5 6
# ------or---------

# [   [   [1 2 3]
#         [4 5 6]   ]
#     [   [1 2 3]
#         [4 5 6]   ]   ]

# Check how many dimensions the arrays have:

# a = np.array(42)
# b = np.array([1, 2, 3, 4, 5])
# c = np.array([[1, 2, 3], [4, 5, 6]])
# d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)

# Create an array with 5 dimensions and verify that it has 5 dimensions

# arr = np.array([1, 2, 3, 4], ndmin=5)
# print(arr)
# print('number of dimensions :', arr.ndim)



# ............................................................................................................

#                               numpy array indexing


#       1D array indexing.............
# arr = np.array([1, 2, 3, 4])
# print(arr[0])
# print(arr[1])
# print(arr[2] + arr[3])

# <--- output --->
# 1
# 2
# 7

#       2D array indexing.............
# arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
# print('2nd element on 1st row: ', arr[0, 1])
# print('5th element on 2nd row: ', arr[1, 4])
# print('Last element from 2nd dim: ', arr[1, -1])
# <--- output --->
# 2
# 10
# 10

#       3D array indexing.............
# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# print(arr[0, 1, 2])
# <--- output --->
# 6
# ............................................................................................................




#                   numpy array slicing

#          1D array slicing.............
# arr = np.array([1, 2, 3, 4, 5, 6, 7])
# print(arr[1:5])
# print(arr[:5])
# print(arr[4:])
# print(arr[-3:-1])
# print(arr[1:5:2])
# print(arr[::2])
# <--- output --->
# [2 3 4 5]
# [1 2 3 4 5]
# [5 6 7]
# [5 6]
# [2 4]
# [1 3 5 7]


#          2D array slicing.............
# arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# print(arr[1, :])  
# print(arr[:, 1])  
# print(arr[0, 1:])  
# print(arr[1:, 1:])  
# print(arr[:, 1:4])  
# print(arr[0:2, :])

# <--- output --->
# [ 6  7  8  9 10]
# [2 7]
# [2 3 4 5]
# [[ 7  8  9 10]]
# [[2 3 4] [7 8 9]]
# [[ 1  2  3  4  5] [ 6  7  8  9 10]]



#          3D array slicing.............
# arr = np.array([[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], [[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]])
# print(arr[0, :, :]) 
# print(arr[:, 0, :]) 
# print(arr[:, :, 0]) 
# print(arr[0, 0, :]) 
# print(arr[:, 1:, :]) 
# print(arr[:, :, 1:]) 
# print(arr[0, :, 1:]) 
# print(arr[0, 1:, 1:])
# <--- output --->
# [[ 1  2  3  4  5] [ 6  7  8  9 10]]
# [[ 1  2  3  4  5] [11 12 13 14 15]]
# [[ 1  6] [11 16]]
# [1 2 3 4 5]
# [[[ 6  7  8  9 10]] [[16 17 18 19 20]]]
# [[[ 2  3  4  5] [ 7  8  9 10]] [[12 13 14 15] [17 18 19 20]]]
# [[ 2  3  4  5] [ 7  8  9 10]]
# [[ 7  8  9 10]]



#                   Numpy data types

# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# V - fixed chunk of memory for other type ( void )

# # Create a numpy array with different data types
# arr = np.array([1, 2, 3, 4, 5])
# print(arr)
# print(arr.dtype)
# # output
# # [1 2 3 4 5]
# # int64

# arr = np.array([True, False, True, False, True])
# print(arr)
# print(arr.dtype)
# # output
# # [ True False  True False  True]
# # bool

# arr = np.array(['apple', 'banana', 'cherry'])
# print(arr)
# print(arr.dtype)
# # output
# # ['apple' 'banana' 'cherry']
# # <U6

# arr = np.array(['apple', 'banana', 'cherry'])
# print(arr)
# print(arr.dtype)
# # output
# # ['apple' 'banana' 'cherry']
# # <U6


#                                   Creating Arrays With a Defined Data Type

# arr = np.array([1, 2, 3, 4], dtype='S')
# print(arr)
# print(arr.dtype)
# # output
# # [b'1' b'2' b'3' b'4']
# # |S1

# arr = np.array([1, 2, 3, 4], dtype='i4')
# print(arr)
# print(arr.dtype)
# # # output
# # [1 2 3 4]
# # int32

# arr = np.array(['a', '2', '3'], dtype='i')
# # output
# # ValueError: invalid literal for int() with base 10: 'a'


#                           Converting Data Type on Existing Arrays

# arr = np.array([1.1, 2.1, 3.1])
# newarr = arr.astype('i')
# print(newarr)
# print(newarr.dtype)
# # output
# # [1 2 3]
# # int32

# arr = np.array([1.1, 2.1, 3.1])
# newarr = arr.astype(int)
# print(newarr)
# print(newarr.dtype)
# # output
# # [1 2 3]
# # int64

# arr = np.array([1, 0, 3])
# newarr = arr.astype(bool)
# print(newarr)
# print(newarr.dtype)
# # output
# # [ True False  True]
# # bool



