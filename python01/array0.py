from array import *
num = array("i", [])
n = int(input("Enter length of Array : "))
for     i in range  (n):
    x = int(input("enter value : "))
    num.append(x)
for e in range(n):
    print(num[e], end=" ")
