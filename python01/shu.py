import numpy
from numpy import *

a = int(input("Enter number of rows : "))
b = int(input("enter number of columns"))
b1 = int(input("enter number of rows"))
m1 = matrix(input("enter elements of first matrix : "))
m2 = matrix(input("enter element of second matrix : "))
n = m1.reshape(a,b)
m = m2.reshape(b1,a)
mn=numpy.zeros((a,b1))# it define a matrix having row,col(a,b1) with zero initial values
s = 0
for i in range(a):
    pass
    for j in range(b1):
        pass
        for k in range(b):
            s += n[i,k] * m[k,j]
        mn[i,j] = s
        s = 0
print("Answer is : ")
for i in range(a):
    pass
    for j in range(b1):
        print(mn[i,j], end=" ")
    print()
