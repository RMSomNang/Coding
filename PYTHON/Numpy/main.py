import numpy as np

# arr = np.array([1,2,3,4,5,6])

# print(str(arr.shape) + "\n")
# print(arr.reshape(2,3))

# newarr = arr.flatten()
# print(newarr)

# arr = np.array([1,2,3,4,5,6,7,8,9,10])
# newarr = arr[0:1]
# print(newarr)

# arr2d = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

# newarr2d = arr2d[0]

# print(newarr2d)

arr = np.array([1,2,3,4,5,6,7,8,9])
newarr = arr.reshape(3,3)
print(newarr)

print(newarr[0:2,1:3])
print(newarr[1,:])