from numpy import *
arr = array([1,3,5,7,9])
arr2 = array([2,4,6,8,0])
arr3 = arr + arr2
print(sin(arr3))
print(arr3)
print(concatenate([arr,arr2]))
arr = arr2.copy()#it is a deep copy that is not link with first one. / if i use .view() it is shallow copy that is linked
arr[1] = 2
print(arr)
print(arr2)
print(id(arr))
print(id(arr2))