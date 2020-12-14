from numpy import *
arr = array([
    [1,2,3],
    [4,5,6]
])
print(arr.flatten())
print(arr.ndim)
print(arr.size)
print(arr.shape)
#print(arr.reshape(2,2,3))
#print(arr.resize(12,6))#fdkljfljaldj
m = matrix(arr)
print(m)
print(diagonal(m))
# we can add and also even multiply matrix through "*" only.
arr2=arr.copy()
arr3 = arr*arr2
print(arr3)